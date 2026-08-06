
from pathlib import Path
import subprocess
from config import caminho_YacReader



def abrir_hq(hq: Path):
    subprocess.Popen([caminho_YacReader, str(hq)])