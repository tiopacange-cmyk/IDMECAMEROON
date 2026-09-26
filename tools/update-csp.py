#!/usr/bin/env python3
"""Recalcule la politique de sécurité du contenu (CSP) de id-me-platform.html.

La CSP n'autorise que les scripts de la page (identifiés par leur empreinte
SHA-256) et le SDK Firebase. Tout code injecté dans la page est alors bloqué
par le navigateur. À relancer après CHAQUE modification d'un <script> :

    python3 tools/update-csp.py
"""
import base64, hashlib, pathlib, re, sys

path = pathlib.Path(__file__).resolve().parent.parent / 'id-me-platform.html'
html = path.read_text(encoding='utf-8')
scripts = re.findall(r'<script>(.*?)</script>', html, re.S)
hashes = ' '.join("'sha256-%s'" % base64.b64encode(hashlib.sha256(s.encode('utf-8')).digest()).decode()
                  for s in scripts)
csp = ("default-src 'self' https: data: blob:; "
       f"script-src {hashes} https://www.gstatic.com; "
       "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
       "font-src 'self' https://fonts.gstatic.com data:; "
       "img-src 'self' data: blob:; "
       "connect-src 'self' https://*.googleapis.com https://*.firebaseio.com wss://*.firebaseio.com https://*.firebaseapp.com; "
       "frame-src https://*.firebaseapp.com; "
       "object-src 'none'; base-uri 'none'; form-action 'none'")
new, n = re.subn(r'(<meta http-equiv="Content-Security-Policy" content=")[^"]*(">)',
                 lambda m: m.group(1) + csp + m.group(2), html, count=1)
if n != 1:
    sys.exit('Balise CSP introuvable dans id-me-platform.html')
path.write_text(new, encoding='utf-8')
print(f'CSP mise à jour ({len(scripts)} scripts en ligne).')
