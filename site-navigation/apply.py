#!/usr/bin/env python3
"""Apply the same platform/site navigation to static presentation pages only."""
from pathlib import Path
from html.parser import HTMLParser
import re,shutil,sys
SITES={
'jazzy':dict(name='JAZZY',platform='FOR FM-1',root='https://jazzyrhythmer.github.io/jazzy/',logo='jazzy-mark.svg',sections=['','\x23engines','\x23patterns','installer/','manual/','\x23support'],legacy='top'),
'rhythmer':dict(name='RHYTHMER',platform='FOR FM-1',root='https://jazzyrhythmer.github.io/rhythmer/',logo='rhythmer-mark.svg',sections=['\x23home','\x23instrument','\x23companion','\x23install','\x23guide','\x23support'],legacy='topbar'),
'mpc':dict(name='RHYTHMER OS',platform='FOR MPC SAMPLE',root='https://jazzyrhythmer.github.io/mpc-sample/',logo=None,sections=['\x23home','\x23engines','\x23workflow','\x23release','manual/','\x23studio'],legacy='')}
LABELS=['OVERVIEW','ENGINES','FEATURES','GET STARTED','MANUAL','STUDIO'];IDS=['overview','engines','features','start','manual','studio']

def header(site):
 s=SITES[site];root=s['root'];icon=f'<img src="{root+s["logo"]}" width="27" height="27" alt="">' if s['logo'] else '<span class="jr-mark" aria-hidden="true">▥</span>'
 def link(key,url,label):return f'<a href="{url}" aria-label="{label}"'+(' aria-current="page"' if key==site else '')+'>'+('JAZZY' if key=='jazzy' else 'RHYTHMER')+'</a>'
 platform='<div class="jr-platform-switcher" role="navigation" aria-label="Platforms and instruments"><div class="jr-platform-group" role="group" aria-label="Firmware for FM-1"><span class="jr-platform-label">FOR FM-1</span><div class="jr-platform-links">'+link('jazzy',SITES['jazzy']['root'],'JAZZY for FM-1')+link('rhythmer',SITES['rhythmer']['root']+'#home','RHYTHMER for FM-1')+'</div></div><div class="jr-platform-group" role="group" aria-label="Firmware for MPC Sample"><span class="jr-platform-label">FOR MPC SAMPLE</span><div class="jr-platform-links">'+link('mpc',SITES['mpc']['root']+'#home','RHYTHMER OS for MPC Sample')+'</div></div></div>'
 platform=platform[:-6]+'<div class="jr-platform-group" role="group" aria-label="Instruments for Mac"><span class="jr-platform-label">FOR MAC</span><div class="jr-platform-links"><a target="_top" href="https://jazzyrhythmer.github.io/mac/" aria-label="Rhythmer Engines for Mac">RHYTHMER</a></div></div>'+'</div>'
 nav='<nav class="jr-section-nav" aria-label="Site sections">'+''.join(f'<a data-section="{id}" href="{root+path}">{label}</a>' for label,id,path in zip(LABELS,IDS,s['sections']))+'</nav>'
 return f'<header class="jr-site-header {s["legacy"]}"><a class="jr-brand" href="{root+s["sections"][0]}">{icon}<span>{s["name"]}</span><small>{s["platform"].replace("FOR ","for ")}</small></a>'+nav+platform+'</header>'

def apply(root,site,subpages=True):
 root=Path(root);assets=Path(__file__).resolve().parent
 for name in ('platform-navigation.css','platform-navigation.js'):shutil.copy2(assets/name,root/name)
 import runpy
 runpy.run_path(str(assets/'support.py'))['apply_support'](root,site)
 targets=[root/'index.html',root/'engine.html']
 if subpages:targets += [root/'manual/index.html',root/'manual/quickstart.html',root/'installer/index.html']
 for path in targets:
  if not path.is_file():continue
  data=path.read_text();prefix='../' if path.parent!=root else ''
  data=re.sub(r'<div class="jr-manual-utility">.*?</div>','',data,flags=re.S)
  match=re.search(r'<header\b([^>]*)>',data)
  class Attrs(HTMLParser):
   def handle_starttag(self,tag,attrs):self.attrs=dict(attrs)
  attrs=Attrs();attrs.feed(match.group() if match else '<header>');old=attrs.attrs
  replacement=header(site)
  if old.get('class'):
   cls=re.search(r'class="([^"]+)"',replacement).group(1)
   replacement=replacement.replace('class="'+cls+'"','class="'+' '.join(dict.fromkeys((cls+' '+old['class']).split()))+'"',1)
  for key,value in old.items():
   if key.startswith('data-'):replacement=replacement.replace('<header ','<header '+key+('="'+value+'"' if value else '')+' ',1)
  replacement=replacement.replace('<a ','<a target="_top" ')

  if not re.search(r'<header\b',data):continue
  utility=''
  if site=='mpc' and 'manual' in path.parts:utility='<div class="jr-manual-utility"><a href="'+SITES[site]['root']+'manual/quickstart.html">FIRST PATTERN</a><a href="'+SITES[site]['root']+'manual/">MANUAL</a><button class="print" type="button">PRINT</button></div>'
  data=re.sub(r'<header\b.*?</header>',replacement+utility,data,count=1,flags=re.S)
  data=re.sub(r'<link[^>]+href="[^\"]*platform-navigation\.css[^\"]*"[^>]*>','',data)
  data=re.sub(r'<script[^>]+src="[^\"]*platform-navigation\.js[^\"]*"[^>]*></script>','',data)
  data=data.replace('</head>',f'<link rel="stylesheet" href="{prefix}platform-navigation.css?v=navigation-20261116.2"><script src="{prefix}platform-navigation.js?v=navigation-20261116.2" defer></script></head>')
  path.write_text(data);print('Updated navigation:',path.relative_to(root))
if __name__=='__main__':apply(sys.argv[1],sys.argv[2])
