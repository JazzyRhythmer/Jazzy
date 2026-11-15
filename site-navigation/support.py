"""Shared, optional support invitation for the three firmware sites."""
import re
from pathlib import Path
KOFI='https://ko-fi.com/jazzyrhythmer';PATREON='https://www.patreon.com/JazzyRhythmer/'
def invitation(site):
 name={'jazzy':'JAZZY','rhythmer':'RHYTHMER','mpc':'RHYTHMER OS for MPC Sample'}[site]
 first=f'{name} is free and open source, and will always be free.' if site!='mpc' else f'{name} will be free and open source, and will always stay free.'
 heading_id=' id="support-title"' if site=='jazzy' else ''
 return f'''<div class="jr-support-copy"><h2{heading_id}>Support the project</h2><p>{first}</p><p>Your support helps me keep working on this project and other open-source tools.</p><div class="jr-support-actions"><a class="jr-support-tip" href="{KOFI}" target="_blank" rel="noopener noreferrer">Support on Ko-fi ↗</a></div><p class="jr-support-ongoing">You can also <a href="{PATREON}" target="_blank" rel="noopener noreferrer">support my work on Patreon ↗</a>.</p></div>'''

def apply_support(root,site):
 root=Path(root);p=root/'index.html'
 if not p.exists():return
 s=p.read_text()
 if site=='jazzy':
  match=re.search(r'<section\b[^>]*id="support"[^>]*>\s*(?=<div\b)',s)
  if match:
   start=match.end();depth=0
   for tag in re.finditer(r'<div\b[^>]*>|</div\s*>',s[start:]):
    depth+=-1 if tag[0].startswith('</') else 1
    if depth==0:
     s=s[:start]+invitation(site)+s[start+tag.end():];break
 elif site=='mpc':
  s=re.sub(r'<section id="support" class="jr-support-section">.*?</section>','',s,flags=re.S)
  s=re.sub(r'<section id="studio"[^>]*>',lambda m:'<section id="support" class="jr-support-section">'+invitation(site)+'</section>'+m[0],s,count=1)
  # Keep the studio link collection, but avoid repeating a second donation pitch.
  s=s.replace('Want to leave a small tip? <a href="https://ko-fi.com/jazzyrhythmer">Ko-fi ↗</a>','<a href="#support">Support this free project ↑</a>')
 p.write_text(s)
 if site=='rhythmer':
  p=root/'app.js';s=p.read_text();s=re.sub(r'(<div class="support-content">)(?:<section(?: class="jr-support-host")?>).*?</section>',lambda m:m[1]+'<section class="jr-support-host">'+invitation(site)+'</section>',s,count=1,flags=re.S)
  s=s.replace('Help keep Rhythmer free and moving forward.','Free to use. Support is always optional.')
  p.write_text(s)

  p=root/'landing.mjs'
  if p.exists():
   s=p.read_text()
   block='<section class="support-strip jr-home-support">'+invitation(site)+'<a class="text-link" href="#support">Music &amp; studio links →</a></section>'
   s=re.sub(r'<section class="support-strip(?: jr-home-support)?">.*?</section>',lambda m:block,s,count=1,flags=re.S)
   p.write_text(s)
  p=root/'app.js';s=p.read_text().replace('landing.mjs?v=single-break-20261112.1','landing.mjs?v=support-placement3');p.write_text(s)
