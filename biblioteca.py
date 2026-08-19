from pathlib import Path
from config import caminho_hqs, caminho_hqs_marvel, caminho_hqs_dc
import zipfile
import rarfile
import subprocess
import tempfile
import shutil


rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\WinRAR.exe"


# Função para carregar as HQs da biblioteca geral
def carregar_hqs():

    biblioteca = Path(caminho_hqs)

    hqs = []

    if not biblioteca.exists():
        return hqs

    for arquivo in biblioteca.rglob("*"):

        if arquivo.suffix.lower() in (".cbr", ".cbz"):
            hqs.append(arquivo)

    return hqs


# Função para carregar as HQs da Marvel
def carregar_hqs_marvel():

    hqs_marvel = []

    if not caminho_hqs_marvel.exists():
        return hqs_marvel

    for arquivo in caminho_hqs_marvel.rglob("*"):

        if arquivo.suffix.lower() in (".cbr", ".cbz"):
            hqs_marvel.append(arquivo)

    return hqs_marvel


# Função para carregar as HQs da DC
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

        winrar = r"C:\Program Files\WinRAR\WinRAR.exe"

        pasta_temp = Path(
            tempfile.mkdtemp()
        )

        try:

            comando = [
                winrar,
                "x",
                "-ibck",
                "-y",
                str(hq),
                str(pasta_temp)
            ]

            subprocess.run(
                comando,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            imagens = []

            for arquivo in pasta_temp.rglob("*"):

                if arquivo.suffix.lower() in (
                    ".jpg",
                    ".jpeg",
                    ".png",
                    ".webp"
                ):

                    imagens.append(arquivo)

            if imagens:

                capa = imagens[0].read_bytes()

                return capa

            return None

        finally:

            shutil.rmtree(
                pasta_temp,
                ignore_errors=True
            )

    return None


# Função responsável por organizar a biblioteca
def organizar_biblioteca(caminho_hqs):

    biblioteca = Path(caminho_hqs)

    estrutura = {}

    if not biblioteca.exists():
        return estrutura

    for personagem in biblioteca.iterdir():

        if not personagem.is_dir():
            continue

        estrutura[personagem.name] = {}

        for hq in personagem.iterdir():

            if not hq.is_dir():
                continue

            edicoes = []
            subpastas = {}

            for arquivo in hq.iterdir():

                # Edição diretamente dentro da pasta da HQ
                if (
                    arquivo.is_file()
                    and arquivo.suffix.lower() in (".cbr", ".cbz")
                ):

                    edicoes.append(arquivo)

                # Subpasta opcional
                elif arquivo.is_dir():

                    arquivos_subpasta = []

                    for arquivo_subpasta in arquivo.rglob("*"):

                        if (
                            arquivo_subpasta.is_file()
                            and arquivo_subpasta.suffix.lower()
                            in (".cbr", ".cbz")
                        ):

                            arquivos_subpasta.append(
                                arquivo_subpasta
                            )

                    if arquivos_subpasta:

                        subpastas[arquivo.name] = arquivos_subpasta

            estrutura[personagem.name][hq.name] = {
                "edicoes": edicoes,
                "subpastas": subpastas
            }

    return estrutura


# Função responsável por listar personagens/equipes
def listar_personagens(estrutura):

    personagens = []

    for personagem in estrutura:

        personagens.append(personagem)

    return personagens


# Função responsável por listar as HQs de um personagem/equipe
def listar_hqs(estrutura, personagem):

    if personagem not in estrutura:
        return []

    hqs = []

    for hq in estrutura[personagem]:

        hqs.append(hq)

    return hqs

def listar_edicoes(estrutura, personagem, nome_hq):

    if personagem not in estrutura:
        return []

    if nome_hq not in estrutura[personagem]:
        return []

    return estrutura[personagem][nome_hq]["edicoes"]

def listar_subpastas(estrutura, personagem, nome_hq):

    if personagem not in estrutura:
        return {}

    if nome_hq not in estrutura[personagem]:
        return {}

    return estrutura[personagem][nome_hq]["subpastas"]

def listar_hqs_subpasta(estrutura, personagem, nome_hq, nome_subpasta):

    if personagem not in estrutura:
        return []

    if nome_hq not in estrutura[personagem]:
        return []

    subpastas = estrutura[personagem][nome_hq]["subpastas"]

    if nome_subpasta not in subpastas:
        return []

    return subpastas[nome_subpasta]
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

        winrar = r"C:\Program Files\WinRAR\WinRAR.exe"

        pasta_temp = Path(
            tempfile.mkdtemp()
        )

        try:

            comando = [
                winrar,
                "x",
                "-ibck",
                "-y",
                str(hq),
                str(pasta_temp)
            ]

            subprocess.run(
                comando,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            imagens = []

            for arquivo in pasta_temp.rglob("*"):

                if arquivo.suffix.lower() in (
                    ".jpg",
                    ".jpeg",
                    ".png",
                    ".webp"
                ):

                    imagens.append(arquivo)

            quantidade_paginas = len(imagens)

            return quantidade_paginas

        finally:

            shutil.rmtree(
                pasta_temp,
                ignore_errors=True
            )

    return 0

