# a mettre dans /var/lib/asterisk/note/
#!/usr/bin/env python3
import sys
import requests
import os
ext = sys.argv[1]
note = "Note indisponible"
try:
    resp = requests.get(f'http://192.168.1.9:5000/note?extension={ext}', timeout=3)
    if resp.status_code == 200:
        note = resp.json().get('note', 'Aucune note')
    else:
        note = f"Erreur API: code {resp.status_code}"
except Exception as e:
    note = f"Erreur de connexion à l’API: {e}"

# Crée le dossier si nécessaire
path = f'/var/lib/asterisk/note'
os.makedirs(path, exist_ok=True)
# Écrit la note dans le fichier
with open(f'{path}/note_{ext}.txt', 'w') as f:
    f.write(note)
