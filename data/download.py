from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen
import zipfile

URL = "https://ars.els-cdn.com/content/image/1-s2.0-S2352340918315191-mmc2.zip"
DATA_DIR = Path(__file__).resolve().parent

req = Request(URL, headers={"User-Agent": "Mozilla/5.0"})
with urlopen(req) as resp, zipfile.ZipFile(BytesIO(resp.read())) as zf:
    for member in zf.namelist():
        if member.endswith(".csv"):
            (DATA_DIR / Path(member).name).write_bytes(zf.read(member))

print("Downloaded:", [p.name for p in sorted(DATA_DIR.glob("*.csv"))])