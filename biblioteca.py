from pathlib import Path
from config import caminho_hqs

def carregar_hqs():

    biblioteca = Path(caminho_hqs)

    hqs = []

    if not biblioteca.exists():
        return hqs
    
    for arquivo in biblioteca.rglob("*"):
        
        if arquivo.suffix.lower() in (".cbr", ".cbz"):
            hqs.append(arquivo)

    return hqs