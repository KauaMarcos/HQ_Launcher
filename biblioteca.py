from pathlib import Path
from config import caminho_hqs
import zipfile
import rarfile
import subprocess
import tempfile
rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\WinRAR.exe"

# Função para carregar as Hq's, pega o caminho_hqs de config.py,
# e faz uma lista das Hq's, adicionando extensões .cbr e .cbz
def carregar_hqs():

    biblioteca = Path(caminho_hqs)

    hqs = []

    if not biblioteca.exists():
        return hqs

    for arquivo in biblioteca.rglob("*"):

        if arquivo.suffix.lower() in (".cbr", ".cbz"):
            hqs.append(arquivo)

    return hqs


# Função responsável por encontrar a capa da HQ
def pegar_capa(hq):


    # Verifica se a HQ é CBZ
    if hq.suffix.lower() == ".cbz":

        with zipfile.ZipFile(hq, "r") as arquivo:

            imagens = [
                nome for nome in arquivo.namelist()
                if nome.lower().endswith(
                    (".jpg", ".jpeg", ".png", ".webp")
                )
            ]

            if imagens:
                return arquivo.read(imagens[0])


    # Verifica se a HQ é CBR
    elif hq.suffix.lower() == ".cbr":

        # Caminho do WinRAR
        winrar = r"C:\Program Files\WinRAR\WinRAR.exe"

        # Cria uma pasta temporária
        pasta_temp = Path(
            tempfile.mkdtemp()
        )

        # Comando que será executado pelo WinRAR
        comando = [
            winrar,
            "x",
            "-ibck",
            "-y",
            str(hq),
            str(pasta_temp)
        ]

        # Executa o WinRAR
        subprocess.run(
            comando,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        # Procura as imagens extraídas
        imagens = []

        for arquivo in pasta_temp.rglob("*"):

            if arquivo.suffix.lower() in (
                ".jpg",
                ".jpeg",
                ".png",
                ".webp"
            ):

                imagens.append(arquivo)

        # Se encontrou alguma imagem
        if imagens:

            return imagens[0].read_bytes()


    return None