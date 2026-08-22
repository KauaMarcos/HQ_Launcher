from pathlib import Path
import subprocess
from config import caminho_YacReader


# Função para abrir Hq com subprocess.Popen,
# Path sendo para pegar um caminho de arquivo,
# str pra deixar o tipo de hq em string
def abrir_hq(hq: Path):

    # Abre a HQ no YacReader
    subprocess.Popen([caminho_YacReader, str(hq)])