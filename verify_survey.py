#!/usr/bin/env python3
"""Stdlib-only citation audit. Evidence retrieval is NOT semantic entailment.
Run: python3 verify_survey.py [--offline] [--refresh]
Original draft and bibliography are never modified.
"""
import argparse, datetime, difflib, hashlib, html, json, re, time
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / 'sources'

class Page(HTMLParser):
    def __init__(self, raw):
        super().__init__(); self.meta = {}; self.parts = []; self.skip = 0
        self.feed(raw)
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ('script', 'style'): self.skip += 1
        if tag == 'meta':
            k = d.get('name', d.get('property', ''))
            self.meta.setdefault(k, []).append(d.get('content', ''))
        if tag in ('p','div','section','h1','h2','h3','h4','li','tr'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip = max(0,self.skip-1)
        if tag in ('p','div','section','h1','h2','h3','h4','li','tr'): self.parts.append('\n')
    def handle_data(self, s):
        if not self.skip: self.parts.append(s)
    def text(self):
        return '\n'.join(re.sub(r'\s+', ' ', x).strip() for x in ''.join(self.parts).splitlines() if x.strip())

def norm(s):
    return re.sub(r'[^a-z0-9]', '', html.unescape(s).lower())

def bib_entries(s):
    # Brace-delimited fields used by this draft; nested braces are supported.
    entries = {}
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,]+),', s):
        pos=m.end(); start=pos; depth=1
        while pos < len(s) and depth:
            if s[pos]=='{': depth+=1
            elif s[pos]=='}': depth-=1
            pos+=1
        body=s[start:pos-1]; fields={}; i=0
        while i<len(body):
            f=re.search(r'(\w+)\s*=\s*\{',body[i:])
            if not f: break
            a=i+f.end(); b=a; d=1
            while b<len(body) and d:
                if body[b]=='{': d+=1
                elif body[b]=='}': d-=1
                b+=1
            fields[f.group(1).lower()]=body[a:b-1]; i=b
        entries[m.group(2).strip()]={'type':m.group(1),**fields}
    return entries

def fetch(url, name, args):
    path=CACHE/(name+'.html'); info=CACHE/(name+'.json')
    if path.exists() and not args.refresh:
        return path.read_text(), json.loads(info.read_text())
    if args.offline: raise RuntimeError('No cached source: '+url)
    last=None
    for attempt in range(3):
        try:
            with urlopen(Request(url,headers={'User-Agent':'AcademicCitationAudit/1.0'}),timeout=45) as r:
                raw=r.read().decode('utf-8','replace')
                record={'requested_url':url,'resolved_url':r.url,'http_status':r.status,
                        'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                        'sha256':hashlib.sha256(raw.encode()).hexdigest()}
            path.write_text(raw); info.write_text(json.dumps(record,indent=2)); return raw,record
        except Exception as e: last=e; time.sleep(attempt+1)
    raise RuntimeError(str(last))

def main():
    p=argparse.ArgumentParser(); p.add_argument('--offline',action='store_true'); p.add_argument('--refresh',action='store_true'); args=p.parse_args()
    if args.offline and args.refresh: p.error('--offline and --refresh are incompatible')
    CACHE.mkdir(exist_ok=True)
    draft=(ROOT.parent/'survey_draft.tex').read_text(); bib=bib_entries((ROOT.parent/'references_original.bib').read_text())
    citations=[]
    for m in re.finditer(r'\\cite\w*\{([^}]+)\}',draft):
        citations.append({'line':draft[:m.start()].count('\n')+1,'keys':m.group(1).split(','),'context':draft[max(0,draft.rfind('\n',0,m.start())):draft.find('\n',m.end())].strip()})
    results=[]; fulltexts={}
    for key,b in bib.items():
        row={'key':key,'original':b}
        aid=re.search(r'\d{4}\.\d{4,5}',b.get('url','')+' '+b.get('note',''))
        if not aid: row['status']='UNRESOLVED_NO_ARXIV_ID'; results.append(row); continue
        aid=aid.group(); row['arxiv_id']=aid
        try:
            raw,provenance=fetch('https://arxiv.org/abs/'+aid,key+'_metadata',args); page=Page(raw); meta=page.meta
            title=meta.get('citation_title',[''])[0]; authors=meta.get('citation_author',[])
            row.update({'provenance':provenance,'remote_title':title,'remote_authors':authors,'metadata':meta})
            row['status']='IDENTITY_CHECKED' if title and authors else 'UNRESOLVED_METADATA'
            row['title_match']=norm(b.get('title',''))==norm(title)
            row['title_similarity']=round(difflib.SequenceMatcher(None,norm(b.get('title','')),norm(title)).ratio(),3)
            def canonical_author(a):
                if ',' in a:
                    last,first=a.split(',',1); a=first+' '+last
                return norm(a)
            original=b.get('author','').split(' and ')
            row['author_exact_match']=[canonical_author(a) for a in original]==[canonical_author(a) for a in authors]
            row['author_surname_order_match']=[norm(a.split(',')[0]) for a in original]==[norm(a.split(',')[0] if ',' in a else a.split()[-1]) for a in authors]
            row['original_doi_missing']='doi' not in b
            row['arxiv_first_year']=meta.get('citation_date',[''])[0][:4]
            row['year_matches_arxiv_first_year']=b.get('year')==row['arxiv_first_year']
            row['year_note']='Conference year may legitimately differ from first preprint year.'
            row['observed_dois']=sorted(set(re.findall(r'10\.48550/arXiv\.\d{4}\.\d+',raw,re.I)))
            version=re.search(re.escape(aid)+r'v(\d+)',raw)
            vid=aid+'v'+version.group(1) if version else aid
            row['fulltext_url']='https://arxiv.org/html/'+vid
            try:
                body,prov=fetch(row['fulltext_url'],key+'_fulltext',args); text=Page(body).text()
                if len(text)<3000 or norm(title) not in norm(text): raise RuntimeError('Full text failed identity/length validation')
                fulltexts[key]=text; (CACHE/(key+'.txt')).write_text(text)
                row['fulltext_provenance']=prov; row['fulltext_status']='AVAILABLE'
            except Exception as e: row['fulltext_status']='UNRESOLVED'; row['fulltext_error']=str(e)
        except Exception as e: row.update(status='UNRESOLVED_NETWORK',error=str(e))
        results.append(row); print(key,row['status'],row.get('fulltext_status'),flush=True)
    extra={
      'neurips_record':'https://proceedings.neurips.cc/paper_files/paper/2022/hash/3d719fee332caa23d5038b8a90e81796-Abstract-Conference.html',
      'neurips_bib':'https://proceedings.neurips.cc/paper_files/paper/18582-/bibtex',
      'wang_iclr':'https://proceedings.iclr.cc/paper_files/paper/2026/hash/9d0ee47d732bd526c4a03d4aecc39bc1-Abstract-Conference.html',
      'wang_openreview':'https://api2.openreview.net/notes?id=Gk7gLAtVDO'}
    supplementary={}
    for name,url in extra.items():
        try:
            raw,prov=fetch(url,name,args); supplementary[name]={'provenance':prov}; (CACHE/(name+'.txt')).write_text(Page(raw).text())
        except Exception as e: supplementary[name]={'error':str(e),'url':url}
    claims=[]
    # Transparent, draft-specific consistency screens, not an entailment model.
    # Each rule compares a risky draft expression with verified source wording.
    rules=[
      ('R01','taylor2025school','more serious','reward-tampering','UNSUPPORTED_SEVERITY_RANKING','A tampering mention does not establish a general severity ordering.'),
      ('R02','wilhelm2026activations','token-level classifiers','one decision per generation','GRANULARITY_REVIEW','Distinguish token scores from generation-level decisions and supervision.'),
      ('R03','wang2026thinking','unusually early success','Overthinking','CONFOUNDER_REVIEW','Early success alone is not sufficient; review baseline calibration and overthinking.'),
      ('R04','taylor2025school','generalization from trained low-stakes hacks','supervised fine-tuning','TRAINING_SCOPE_REVIEW','State the SFT setup and restrict generalization to tested models.'),
      ('R05','bergen2026representations','online prediction of later hacks','resampled','EXPERIMENT_SCOPE_REVIEW','Describe the truncation/resampling study; do not imply guaranteed online intervention.'),
      ('R06','baker2025monitoring','faithfulness of the trace','monitorability','CONCEPT_REVIEW','Monitorability does not require complete faithfulness.')]
    semantic_screens=[]
    for rid,key,trigger,anchor,flag,explanation in rules:
        if trigger in draft:
            semantic_screens.append({'rule':rid,'key':key,'draft_trigger':trigger,'source_anchor':anchor,
              'source_anchor_found':anchor.lower() in fulltexts.get(key,'').lower(),
              'flag':flag,'explanation':explanation,'requires_human_review':True})
    manifest=ROOT/'claims.json'
    if manifest.exists():
        for c in json.loads(manifest.read_text()):
            source=fulltexts.get(c['key'],''); hits=[]
            for anchor in c['anchors']:
                # Lexical retrieval only: status never says "supported".
                lines=[x for x in source.splitlines() if anchor.lower() in x.lower()]
                hits.append({'anchor':anchor,'found':bool(lines),'candidate_passages':lines[:3]})
            claims.append({**c,'draft_span_present':c['draft_span'] in draft,'anchor_hits':hits,
                'automatic_status':'EVIDENCE_CANDIDATE_REQUIRES_SEMANTIC_REVIEW' if hits and all(h['found'] for h in hits) else 'MISSING_EVIDENCE_REQUIRES_REVIEW',
                'note':'AI assessment in manifest is an authored review, not a computed entailment result.'})
    used={k.strip() for c in citations for k in c['keys']}
    result={'run_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'draft_sha256':hashlib.sha256(draft.encode()).hexdigest(),
      'limitations':'URL/metadata and lexical evidence retrieval cannot prove semantic support or paper validity; network failure is not a fake reference.',
      'references':results,'citation_occurrences':citations,'missing_bib_keys':sorted(used-set(bib)),
      'uncited_bib_keys':sorted(set(bib)-used),'supplementary':supplementary,'automatic_consistency_screens':semantic_screens,'claims':claims}
    (ROOT/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print('Wrote',ROOT/'results.json')

if __name__=='__main__': main()
