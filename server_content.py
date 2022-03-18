import json
import subprocess
from pathlib import Path

DB_FILE = Path("db.json")
DB_URL = "https://raw.githubusercontent.com/jshttp/mime-db/master/db.json"
OUTPUT_DIR = Path("server_content")

if not OUTPUT_DIR.exists():
    OUTPUT_DIR.mkdir()

if DB_FILE.exists():
    DB_FILE.unlink()
    db_download_call = subprocess.run(['wget', '-L', DB_URL], check=True)
else:
    db_download_call = subprocess.run(['wget', '-L', DB_URL], check=True)

with open(DB_FILE) as file:
    mime_db = json.load(file)

result = {}
for k, v in mime_db.items():
    extensions = v.get('extensions')
    if extensions is not None:
        for extension in extensions:
            result.setdefault(extension, {k}).add(k)
            if len(result.get(extension, [])) > 1:
                (OUTPUT_DIR / f"{extension}_file.{extension}").touch()
