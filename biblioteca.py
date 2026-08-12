from pathlib import Path
from config import caminho_hqs

# Função para carregar as Hq's, pega o caminho_hqs de config.py,
#  e faz uma lista das Hq's, adicionando extensões .cbr e .cbz
def carregar_hqs():

    biblioteca = Path(caminho_hqs)

    hqs = []

    if not biblioteca.exists():
        return hqs
    for arquivo in biblioteca.rglob("*"):     
        if arquivo.suffix.lower() in (".cbr", ".cbz"):
            hqs.append(arquivo)
    
    return hqs