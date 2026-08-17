from pathlib import Path
from config import caminho_hqs, caminho_hqs_marvel, caminho_hqs_dc
import zipfile
import rarfile
import subprocess
import tempfile
import shutil

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

def carregar_hqs_marvel():

    hqs_marvel = []

    if not caminho_hqs_marvel.exists():

        return hqs_marvel

    for arquivo in caminho_hqs_marvel.rglob("*"):

        if arquivo.suffix.lower() in (".cbr", ".cbz"):
            hqs_marvel.append(arquivo)
 
    return hqs_marvel

def carregar_hqs_dc():

    hqs_dc = []

    if not caminho_hqs_dc.exists():

        return hqs_dc

    for arquivo in caminho_hqs_dc.rglob("*"):

        if arquivo.suffix.lower() in (".cbr", ".cbz"):
            hqs_dc.append(arquivo)
    
    return hqs_dc
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

        try:

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

                # Lê a capa antes de apagar a pasta temporária
                capa = imagens[0].read_bytes()

                return capa

            return None

        finally:

            # Apaga a pasta temporária e todos os arquivos extraídos
            shutil.rmtree(
                pasta_temp,
                ignore_errors=True
            )


    return None


# Função responsável por contar as páginas da HQ
def contar_paginas(hq):

    # Verifica se a HQ é CBZ
    if hq.suffix.lower() == ".cbz":

        with zipfile.ZipFile(hq, "r") as arquivo:

            imagens = [
                nome for nome in arquivo.namelist()
                if nome.lower().endswith(
                    (".jpg", ".jpeg", ".png", ".webp")
                )
            ]

            return len(imagens)


    # Verifica se a HQ é CBR
    elif hq.suffix.lower() == ".cbr":

        # Caminho do WinRAR
        winrar = r"C:\Program Files\WinRAR\WinRAR.exe"

        # Cria uma pasta temporária
        pasta_temp = Path(
            tempfile.mkdtemp()
        )

        try:

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

            # Conta a quantidade de páginas
            quantidade_paginas = len(imagens)

            return quantidade_paginas

        finally:

            # Apaga a pasta temporária e todos os arquivos extraídos
            shutil.rmtree(
                pasta_temp,
                ignore_errors=True
            )

    return 0