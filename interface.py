import tkinter as tk
import zipfile
import rarfile
from io import BytesIO
from PIL import Image, ImageTk
from biblioteca import (
    carregar_hqs,
    pegar_capa,
    contar_paginas,
    carregar_hqs_marvel,
    carregar_hqs_dc,
    organizar_biblioteca,
    listar_personagens,
    listar_hqs,
    listar_edicoes,
    listar_subpastas,
    listar_hqs_subpasta
)
from config import caminho_hqs_marvel, caminho_hqs_dc
from Launcher import abrir_hq
import customtkinter as ctk


COR_DO_FUNDO = "#101014"
COR_DO_PAINEL = "#18181f"
COR_TEXTO = "#FFFFFF"
COR_TEXTO_SECUNDARIO = "#A0A0AA"
COR_DESTAQUE = "#E63946"

# Cores adicionais para a nova aparência
COR_CARD = "#202027"
COR_CARD_HOVER = "#292931"
COR_BORDA = "#30303A"
COR_VERDE = "#55D187"
COR_AZUL = "#5B8DEF"


# Função de carregar hq dentro da interface,
# recebe uma lista de Hqs e mostra elas na biblioteca
def carregar_hq_interface(lista_hqs, hqs):

    # Foi criado para não duplicar as Hqs ao clicar no botão mais de uma vez
    lista_hqs.delete(0, tk.END)

    # Foi criado para inserir cada hq do inicio ao fim da lista recebida
    for hq in hqs:
        lista_hqs.insert(tk.END, hq.name)


# Foi criado para Selecionar as hqs na interface
def selecionar_hq(
    lista_hqs,
    hqs,
    texto_selecao,
    capa_hq,
    pag_hq,
    formato_hq,
    editora_hq,
    personagem_hq
):

    selecao = lista_hqs.curselection()

    if selecao:

        hq = hqs[selecao[0]]

        print(f"Hq Selecionada foi: {hq}\n")

        # Atualiza o texto do painel de informações
        texto_selecao.config(
            text=hq.name
        )

        # Conta a quantidade de páginas da HQ
        paginas = contar_paginas(hq)

        pag_hq.config(
            text=f"📄  {paginas} páginas"
        )

        # Mostra o formato do arquivo
        formato = hq.suffix.upper()

        formato_hq.config(
            text=f"📦  {formato}"
        )

        dados_capa = pegar_capa(hq)

        if dados_capa:

            # Converte os dados da capa em uma imagem
            imagem = Image.open(BytesIO(dados_capa))

            # Redimensiona a capa para caber no painel
            imagem.thumbnail((220, 300))

            # Converte a imagem para o formato usado pelo Tkinter
            capa_tk = ImageTk.PhotoImage(imagem)

            # Mostra a capa no Label
            capa_hq.config(image=capa_tk)

            # Mantém a imagem na memória
            capa_hq.image = capa_tk

            print("Capa carregada com sucesso!\n")

        else:

            print("Capa não encontrada!")

            capa_hq.config(
                image=""
            )

            capa_hq.image = None


# Foi Criado para abrir a hq selecionada na interface
def abrir_hq_interface(lista_hqs, hqs):

    hq_selecionada = lista_hqs.curselection()

    if not hq_selecionada:

        print("Nenhuma HQ Selecionada.")

        return

    hq = hqs[hq_selecionada[0]]

    print(f"HQ Selecionada: {hq}")

    abrir_hq(hq)


# Função para iniciar interface
def iniciar_interface():

    # Abrir Janela
    janela = tk.Tk()

    # Título da interface
    janela.title("HQ Launcher")

    # Tamanho Da Janela
    janela.geometry("1440x900")

    # Cor de Fundo da Janela
    janela.configure(bg=COR_DO_FUNDO)

    janela.resizable(True, True)

    # Área responsável pelo cabeçalho da interface
    cabeçalho = tk.Frame(
        janela,
        bg=COR_DO_FUNDO
    )

    # Posiciona o cabeçalho na parte superior
    cabeçalho.pack(
        fill="x",
        padx=30,
        pady=(25, 15)
    )

    # Título principal do programa
    titulo = tk.Label(
        cabeçalho,
        text="HQ LAUNCHER",
        fg=COR_TEXTO,
        bg=COR_DO_FUNDO,
        font=("Segoe UI", 28, "bold")
    )

    # Alinha o título à esquerda
    titulo.pack(anchor="w")

    # Subtítulo do programa
    subtitulo = tk.Label(
        cabeçalho,
        text="Minha Biblioteca de HQs",
        fg=COR_TEXTO_SECUNDARIO,
        bg=COR_DO_FUNDO,
        font=("Segoe UI", 12)
    )

    # Posiciona o subtítulo abaixo do título
    subtitulo.pack(
        anchor="w",
        pady=(2, 12)
    )

    # Área onde ficarão as informações resumidas da biblioteca
    painel_estatisticas = tk.Frame(
        cabeçalho,
        bg=COR_DO_FUNDO
    )

    painel_estatisticas.pack(
        fill="x"
    )

    # Card responsável pelo total de edições
    card_edicoes = tk.Frame(
        painel_estatisticas,
        bg=COR_CARD,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        width=155,
        height=42
    )

    card_edicoes.pack(
        side="left",
        padx=(0, 8)
    )

    card_edicoes.pack_propagate(False)

    label_total_edicoes = tk.Label(
        card_edicoes,
        text="0",
        fg=COR_TEXTO,
        bg=COR_CARD,
        font=("Segoe UI", 16, "bold")
    )

    label_total_edicoes.pack(
        side="left",
        padx=(12, 5)
    )

    label_edicoes_texto = tk.Label(
        card_edicoes,
        text="EDIÇÕES",
        fg=COR_TEXTO_SECUNDARIO,
        bg=COR_CARD,
        font=("Segoe UI", 9, "bold")
    )

    label_edicoes_texto.pack(
        side="left",
        padx=(0, 12)
    )

    # Card responsável pelo total de personagens/equipes
    card_personagens = tk.Frame(
        painel_estatisticas,
        bg=COR_CARD,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        width=155,
        height=42
    )

    card_personagens.pack(
        side="left",
        padx=8
    )

    card_personagens.pack_propagate(False)

    label_total_personagens = tk.Label(
        card_personagens,
        text="0",
        fg=COR_TEXTO,
        bg=COR_CARD,
        font=("Segoe UI", 16, "bold")
    )

    label_total_personagens.pack(
        side="left",
        padx=(12, 5)
    )

    label_personagens_texto = tk.Label(
        card_personagens,
        text="PERSONAGENS",
        fg=COR_TEXTO_SECUNDARIO,
        bg=COR_CARD,
        font=("Segoe UI", 9, "bold")
    )

    label_personagens_texto.pack(
        side="left",
        padx=(0, 12)
    )

    # Card responsável pela editora atual
    card_editora = tk.Frame(
        painel_estatisticas,
        bg=COR_CARD,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        width=155,
        height=42
    )

    card_editora.pack(
        side="left",
        padx=8
    )

    card_editora.pack_propagate(False)

    label_editora = tk.Label(
        card_editora,
        text="TODAS",
        fg=COR_TEXTO,
        bg=COR_CARD,
        font=("Segoe UI", 10, "bold")
    )

    label_editora.pack(
        expand=True
    )

    # Área onde ficarão os principais elementos do Launcher
    area_principal = tk.Frame(
        janela,
        bg=COR_DO_FUNDO
    )

    # Faz a área ocupar o espaço disponível
    area_principal.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )

    # Painel onde ficará a lista de HQs
    painel_biblioteca = tk.Frame(
        area_principal,
        bg=COR_DO_PAINEL
    )

    # Posiciona o painel no lado esquerdo
    painel_biblioteca.pack(
        side="left",
        fill="both",
        expand=True
    )

    # painel onde ficará as informações da HQ selecionada
    painel_info = tk.Frame(
        area_principal,
        bg=COR_DO_PAINEL,
        width=350
    )

    painel_info.pack(
        side="right",
        fill="both",
        expand=True,
        padx=(10, 10)
    )

    painel_info.pack_propagate(False)

    # Título do painel de informações
    titulo_informacoes = tk.Label(
        painel_info,
        text="📖  INFORMAÇÕES",
        fg=COR_TEXTO,
        bg=COR_DO_PAINEL,
        font=("Segoe UI", 13, "bold")
    )

    # Posiciona o título dentro do painel
    titulo_informacoes.pack(
        anchor="w",
        padx=20,
        pady=(15, 5)
    )

    # Área onde será mostrado o nome da HQ selecionada
    texto_selecao = tk.Label(
        painel_info,
        text="Nenhuma HQ selecionada",
        fg=COR_TEXTO,
        bg=COR_DO_PAINEL,
        font=("Segoe UI", 15, "bold"),
        justify="left",
        wraplength=310
    )

    # Posiciona o texto dentro do painel
    texto_selecao.pack(
        anchor="w",
        padx=20,
        pady=(5, 8)
    )

    # Informação da editora da HQ
    editora_hq = tk.Label(
        painel_info,
        text="",
        fg=COR_TEXTO_SECUNDARIO,
        bg=COR_DO_PAINEL,
        font=("Segoe UI", 10, "bold")
    )

    editora_hq.pack(
        anchor="w",
        padx=20,
        pady=(0, 5)
    )

    # Informação do personagem da HQ
    personagem_hq = tk.Label(
        painel_info,
        text="",
        fg=COR_TEXTO_SECUNDARIO,
        bg=COR_DO_PAINEL,
        font=("Segoe UI", 10, "bold")
    )

    personagem_hq.pack(
        anchor="w",
        padx=20,
        pady=(0, 8)
    )

    # Área onde será mostrada a capa da HQ selecionada
    capa_hq = tk.Label(
        painel_info,
        bg=COR_DO_PAINEL
    )

    # Posiciona a capa dentro do painel
    capa_hq.pack(
        pady=10
    )

    # Área para mostrar informações técnicas da HQ
    painel_detalhes = tk.Frame(
        painel_info,
        bg=COR_CARD,
        highlightbackground=COR_BORDA,
        highlightthickness=1
    )

    painel_detalhes.pack(
        fill="x",
        padx=20,
        pady=(5, 15)
    )

    # Informação das páginas da HQ
    pag_hq = tk.Label(
        painel_detalhes,
        text="📄  -- páginas",
        fg=COR_TEXTO,
        bg=COR_CARD,
        font=("Segoe UI", 11, "bold")
    )

    pag_hq.pack(
        side="left",
        padx=12,
        pady=10
    )

    # Informação do formato da HQ
    formato_hq = tk.Label(
        painel_detalhes,
        text="📦  --",
        fg=COR_TEXTO_SECUNDARIO,
        bg=COR_CARD,
        font=("Segoe UI", 10, "bold")
    )

    formato_hq.pack(
        side="right",
        padx=12,
        pady=10
    )

    # Título da biblioteca de HQs
    titulo_biblioteca = tk.Label(
        painel_biblioteca,
        text="📚 Biblioteca",
        fg=COR_TEXTO,
        bg=COR_DO_PAINEL,
        font=("Segoe UI", 15, "bold")
    )

    # Posiciona o título dentro do painel
    titulo_biblioteca.pack(
        anchor="w",
        padx=20,
        pady=(20, 10)
    )

    # Barra de pesquisa da biblioteca
    barra_pesquisa = ctk.CTkEntry(
        painel_biblioteca,
        placeholder_text="🔎  Pesquisar...",
        fg_color=COR_DO_FUNDO,
        border_color=COR_BORDA,
        text_color=COR_TEXTO,
        placeholder_text_color=COR_TEXTO_SECUNDARIO,
        corner_radius=10,
        height=38,
        font=("Segoe UI", 11)
    )

    # Posiciona a barra de pesquisa acima da lista
    barra_pesquisa.pack(
        fill="x",
        padx=20,
        pady=(0, 10)
    )

    # Componente para Lista de HQs na interface
    lista_hqs = tk.Listbox(
        painel_biblioteca,
        bg=COR_DO_FUNDO,
        fg=COR_TEXTO,
        selectbackground=COR_DESTAQUE,
        selectforeground=COR_TEXTO,
        font=("Segoe UI", 11),
        relief="flat",
        highlightthickness=0,
        activestyle="none",
        bd=0
    )

    # Posiciona a lista de hqs dentro do painel
    lista_hqs.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 15)
    )

    # Área responsável por organizar os botões
    painel_botoes = tk.Frame(
        painel_biblioteca,
        bg=COR_DO_PAINEL
    )

    # Posiciona o painel dos botões
    painel_botoes.pack(
        fill="x",
        padx=20,
        pady=(0, 20)
    )

    painel_filtros = tk.Frame(
        painel_botoes,
        bg=COR_DO_PAINEL
    )

    painel_filtros.pack(
        side="left",
        expand=True,
        fill="x"
    )

    painel_acao = tk.Frame(
        painel_botoes,
        bg=COR_DO_PAINEL
    )

    painel_acao.pack(
        side="right",
        padx=(10, 0)
    )

    # Carrega as HQs usando a função carregar_hqs
    hqs = carregar_hqs()

    # Carrega somente as HQs da Marvel
    hqs_marvel = carregar_hqs_marvel()

    # Carrega somente as HQs da DC
    hqs_dc = carregar_hqs_dc()

    # Organiza a biblioteca da Marvel
    biblioteca_marvel = organizar_biblioteca(
        caminho_hqs_marvel
    )

    # Organiza a biblioteca da DC
    biblioteca_dc = organizar_biblioteca(
        caminho_hqs_dc
    )

    # Guarda a lista de Hqs que está sendo mostrada atualmente
    hqs_atual = hqs

    # Guarda o nível atual da biblioteca:
    nivel_atual = "hqs"

    # Guarda qual biblioteca organizada está ativa (marvel ou dc)
    biblioteca_atual = None

    # Guarda a lista de nomes de personagens mostrada atualmente,
    # na mesma ordem em que aparecem na lista_hqs
    personagens_atual = []

    # Guarda o nome do personagem selecionado, usado quando
    personagem_atual = None

    # Guarda a lista de nomes das pastas de HQ do personagem atual
    # na mesma ordem em que aparecem na lista_hqs
    hqs_personagem_atual = []

    # Guarda a lista de subpastas da HQ atual
    subpastas_atual = []

    # Guarda a HQ atualmente selecionada para navegação
    hq_atual_navegacao = None

    # Pilha de navegação: guarda, em ordem, as telas por onde o usuário
    # passou, para que o botão "VOLTAR" saiba reconstruir a tela anterior.
    # Cada item é uma tupla começando com o tipo de tela:
    pilha_navegacao = []

    # Guarda os itens que estão atualmente visíveis na pesquisa
    itens_pesquisa_atual = []

    # Atualiza as informações do cabeçalho
    def atualizar_estatisticas(biblioteca, nome_editora):

        if biblioteca is None:

            total_edicoes = len(hqs)

            personagens = set()

            for personagem in biblioteca_marvel:
                personagens.add(personagem)

            for personagem in biblioteca_dc:
                personagens.add(personagem)

            total_personagens = len(personagens)

        else:

            total_edicoes = 0

            for personagem in biblioteca:

                for nome_hq in biblioteca[personagem]:

                    total_edicoes += len(
                        biblioteca[personagem][nome_hq]["edicoes"]
                    )

                    subpastas = biblioteca[personagem][nome_hq]["subpastas"]

                    for arquivos in subpastas.values():
                        total_edicoes += len(arquivos)

            total_personagens = len(biblioteca)

        label_total_edicoes.config(
            text=str(total_edicoes)
        )

        label_total_personagens.config(
            text=str(total_personagens)
        )

        label_editora.config(
            text=nome_editora
        )

    # Função para carregar todas as HQs
    def carregar_todas():

        nonlocal hqs_atual
        nonlocal nivel_atual

        nivel_atual = "hqs"

        hqs_atual = hqs

        # é feito para zerar o histórico de navegação
        pilha_navegacao.clear()

        atualizar_estatisticas(
            None,
            "TODAS"
        )

        # Limpa as informações anteriores
        texto_selecao.config(
            text="Nenhuma HQ selecionada"
        )

        editora_hq.config(
            text=""
        )

        personagem_hq.config(
            text=""
        )

        pag_hq.config(
            text="📄  -- páginas"
        )

        formato_hq.config(
            text="📦  --"
        )

        capa_hq.config(
            image=""
        )

        capa_hq.image = None

        barra_pesquisa.delete(
            0,
            tk.END
        )

        carregar_hq_interface(
            lista_hqs,
            hqs_atual
        )

    # Função para mostrar os personagens e equipes
    def mostrar_personagens(biblioteca):

        nonlocal nivel_atual
        nonlocal biblioteca_atual
        nonlocal personagens_atual

        nivel_atual = "personagens"

        biblioteca_atual = biblioteca

        personagens_atual = listar_personagens(
            biblioteca
        )

        lista_hqs.delete(
            0,
            tk.END
        )

        # Atualiza o painel de informações
        texto_selecao.config(
            text="Selecione um personagem"
        )

        editora_hq.config(
            text="🦸  Personagens e equipes"
        )

        personagem_hq.config(
            text=f"📚  {len(personagens_atual)} encontrados"
        )

        pag_hq.config(
            text=""
        )

        formato_hq.config(
            text=""
        )

        capa_hq.config(
            image=""
        )

        capa_hq.image = None

        for personagem in personagens_atual:

            lista_hqs.insert(
                tk.END,
                f"  {personagem}"
            )

    # Função para carregar somente as HQs da Marvel
    def carregar_marvel():

        # Guarda a tela atual (o que estava sendo mostrado antes)
        # para o botão VOLTAR poder reconstruí-la depois
        pilha_navegacao.append(
            ("hqs", hqs_atual)
        )

        atualizar_estatisticas(
            biblioteca_marvel,
            "MARVEL"
        )

        barra_pesquisa.delete(
            0,
            tk.END
        )

        mostrar_personagens(
            biblioteca_marvel
        )

    # Função para carregar somente as HQs da DC
    def carregar_dc():

        pilha_navegacao.append(
            ("hqs", hqs_atual)
        )

        atualizar_estatisticas(
            biblioteca_dc,
            "DC"
        )

        barra_pesquisa.delete(
            0,
            tk.END
        )

        mostrar_personagens(
            biblioteca_dc
        )

    # Função para mostrar as pastas de HQ de um personagem específico
    # (ex: "Justiceiro 2011", "Justiceiro Especial")
    def mostrar_hqs_personagem(biblioteca, personagem):

        nonlocal nivel_atual
        nonlocal personagem_atual
        nonlocal hqs_personagem_atual

        nivel_atual = "hqs_personagem"

        personagem_atual = personagem

        hqs_personagem_atual = listar_hqs(
            biblioteca,
            personagem
        )

        lista_hqs.delete(
            0,
            tk.END
        )

        # Atualiza o painel de informações
        texto_selecao.config(
            text=personagem
        )

        editora_hq.config(
            text="🦸  Personagem / Equipe"
        )

        personagem_hq.config(
            text=f"📚  {len(hqs_personagem_atual)} séries encontradas"
        )

        pag_hq.config(
            text=""
        )

        formato_hq.config(
            text=""
        )

        capa_hq.config(
            image=""
        )

        capa_hq.image = None

        for nome_hq in hqs_personagem_atual:

            lista_hqs.insert(
                tk.END,
                f"  {nome_hq}"
            )

    # Função para mostrar as edições e subpastas de uma pasta de HQ específica
    def mostrar_edicoes_hq(biblioteca, personagem, nome_hq):

        nonlocal hqs_atual
        nonlocal nivel_atual
        nonlocal subpastas_atual
        nonlocal hq_atual_navegacao

        edicoes = listar_edicoes(
            biblioteca,
            personagem,
            nome_hq
        )

        subpastas = listar_subpastas(
            biblioteca,
            personagem,
            nome_hq
        )

        hq_atual_navegacao = nome_hq

        # Atualiza o painel de informações
        texto_selecao.config(
            text=nome_hq
        )

        editora_hq.config(
            text=f"📚  {label_editora.cget('text')}"
        )

        personagem_hq.config(
            text=f"🦸  {personagem}"
        )

        pag_hq.config(
            text=f"📖  {len(edicoes)} edições"
        )

        formato_hq.config(
            text=f"📁  {len(subpastas)} pastas"
        )

        capa_hq.config(
            image=""
        )

        capa_hq.image = None

        # Se existem subpastas, mostra elas separadamente
        # das edições principais
        if subpastas:

            nivel_atual = "subpastas"

            subpastas_atual = list(subpastas.keys())

            lista_hqs.delete(
                0,
                tk.END
            )

            # Mostra primeiro as edições principais
            for edicao in edicoes:

                lista_hqs.insert(
                    tk.END,
                    f"  {edicao.name}"
                )

            # Depois mostra as subpastas
            for nome_subpasta in subpastas_atual:

                lista_hqs.insert(
                    tk.END,
                    f"  📁 {nome_subpasta}"
                )

            # Guarda as edições principais
            hqs_atual = edicoes

        else:

            # Não existem subpastas
            nivel_atual = "hqs"

            hqs_atual = edicoes

            carregar_hq_interface(
                lista_hqs,
                hqs_atual
            )

    # Função para mostrar as edições de uma subpasta
    def mostrar_edicoes_subpasta(
        biblioteca,
        personagem,
        nome_hq,
        nome_subpasta
    ):

        nonlocal nivel_atual
        nonlocal hqs_atual

        hqs_subpasta = listar_hqs_subpasta(
            biblioteca,
            personagem,
            nome_hq,
            nome_subpasta
        )

        hqs_atual = hqs_subpasta

        nivel_atual = "hqs"

        # Atualiza o painel de informações
        texto_selecao.config(
            text=nome_subpasta
        )

        editora_hq.config(
            text=f"📁  {nome_hq}"
        )

        personagem_hq.config(
            text=f"🦸  {personagem}"
        )

        pag_hq.config(
            text=f"📖  {len(hqs_subpasta)} edições"
        )

        formato_hq.config(
            text="📦  Subpasta"
        )

        capa_hq.config(
            image=""
        )

        capa_hq.image = None

        carregar_hq_interface(
            lista_hqs,
            hqs_atual
        )

    # Função chamada pelo botão VOLTAR: desempilha a última tela
    # guardada em pilha_navegacao e reconstrói ela na lista_hqs
    def voltar():

        nonlocal hqs_atual
        nonlocal nivel_atual

        # Se não há histórico, não há para onde voltar
        if not pilha_navegacao:

            print("Não há tela anterior para voltar.")

            return

        tela_anterior = pilha_navegacao.pop()

        tipo = tela_anterior[0]

        barra_pesquisa.delete(
            0,
            tk.END
        )

        if tipo == "hqs":

            # tela_anterior é ("hqs", lista_de_arquivos)
            nivel_atual = "hqs"

            hqs_atual = tela_anterior[1]

            carregar_hq_interface(
                lista_hqs,
                hqs_atual
            )

        elif tipo == "personagens":

            # tela_anterior é ("personagens", biblioteca)
            # Chama mostrar_personagens diretamente (sem empilhar de novo)
            mostrar_personagens(
                tela_anterior[1]
            )

        elif tipo == "hqs_personagem":

            # tela_anterior é ("hqs_personagem", biblioteca, personagem)
            # Chama mostrar_hqs_personagem diretamente (sem empilhar de novo)
            mostrar_hqs_personagem(
                tela_anterior[1],
                tela_anterior[2]
            )

        elif tipo == "subpastas":

            mostrar_edicoes_hq(
                tela_anterior[1],
                tela_anterior[2],
                tela_anterior[3]
            )

    # Função responsável por pesquisar dentro da tela atual
    def pesquisar(evento=None):

        nonlocal itens_pesquisa_atual

        termo = barra_pesquisa.get().strip().lower()

        lista_hqs.delete(
            0,
            tk.END
        )

        itens_pesquisa_atual = []

        if nivel_atual == "hqs":

            itens_pesquisa_atual = [
                hq
                for hq in hqs_atual
                if termo in hq.name.lower()
            ]

            for hq in itens_pesquisa_atual:

                lista_hqs.insert(
                    tk.END,
                    hq.name
                )

        elif nivel_atual == "personagens":

            itens_pesquisa_atual = [
                personagem
                for personagem in personagens_atual
                if termo in personagem.lower()
            ]

            for personagem in itens_pesquisa_atual:

                lista_hqs.insert(
                    tk.END,
                    f"  {personagem}"
                )

        elif nivel_atual == "hqs_personagem":

            itens_pesquisa_atual = [
                nome_hq
                for nome_hq in hqs_personagem_atual
                if termo in nome_hq.lower()
            ]

            for nome_hq in itens_pesquisa_atual:

                lista_hqs.insert(
                    tk.END,
                    f"  {nome_hq}"
                )

        elif nivel_atual == "subpastas":

            edicoes = listar_edicoes(
                biblioteca_atual,
                personagem_atual,
                hq_atual_navegacao
            )

            subpastas = listar_subpastas(
                biblioteca_atual,
                personagem_atual,
                hq_atual_navegacao
            )

            # Guarda os itens da tela na mesma ordem em que aparecem
            itens_pesquisa_atual = []

            for edicao in edicoes:

                if termo in edicao.name.lower():

                    itens_pesquisa_atual.append(
                        ("edicao", edicao)
                    )

                    lista_hqs.insert(
                        tk.END,
                        f"  {edicao.name}"
                    )

            for nome_subpasta in subpastas_atual:

                if termo in nome_subpasta.lower():

                    itens_pesquisa_atual.append(
                        ("subpasta", nome_subpasta)
                    )

                    lista_hqs.insert(
                        tk.END,
                        f"  📁 {nome_subpasta}"
                    )

    # Evento responsável por atualizar a pesquisa enquanto o usuário digita
    barra_pesquisa.bind(
        "<KeyRelease>",
        pesquisar
    )

    # Botão para Carregar HQ,
    # command=lambda: dar um comando para chamar a função carregar_hq_interface
    # e mostrar as hqs com lista_hqs
    button = ctk.CTkButton(
        painel_filtros,
        text="TODAS HQS",
        command=carregar_todas,
        fg_color="#2A2A32",
        hover_color="#3A3A45",
        text_color="#FFFFFF",
        corner_radius=10,
        font=("Segoe UI", 10, "bold"),
        cursor="hand2"
    )

    # Posiciona o Botão de carregar Hqs dentro do Frame
    button.pack(
        side="left",
        expand=True,
        fill="x",
        padx=(0, 5),
        ipady=8
    )

    # Botão para Abrir HQ,
    # command=lambda: dar um comando para chamar a função abrir_hq_interface
    button_open_hq = ctk.CTkButton(
        painel_acao,
        text="ABRIR HQ",
        command=lambda: abrir_hq_interface(
            lista_hqs,
            hqs_atual
        ),
        fg_color="#FFFFFF",
        hover_color="#D9D9D9",
        text_color="#101014",
        corner_radius=10,
        font=("Segoe UI", 11, "bold"),
        height=40,
        cursor="hand2"
    )

    # Posiciona o Botão de Abrir Hqs dentro do Frame
    button_open_hq.pack(
        side="left",
        expand=True,
        fill="x",
        padx=(10, 0),
        ipady=8
    )

    # Botão para Voltar um nível na navegação,
    # command=voltar: chama a função que desempilha a tela anterior
    button_voltar = ctk.CTkButton(
        painel_acao,
        text="VOLTAR",
        command=voltar,
        fg_color="#2A2A32",
        hover_color="#3A3A45",
        text_color="#FFFFFF",
        corner_radius=10,
        height=40,
        font=("Segoe UI", 11, "bold"),
        cursor="hand2"
    )

    # Posiciona o Botão de Voltar dentro do Frame
    button_voltar.pack(
        side="left",
        expand=True,
        fill="x",
        padx=(10, 0),
        ipady=8
    )

    # Botão para carregar somente as HQs da Marvel
    button_marvel = ctk.CTkButton(
        painel_filtros,
        text="MARVEL",
        command=carregar_marvel,
        fg_color="#E62429",
        hover_color="#EB7C7C",
        text_color="#FFFFFF",
        corner_radius=8,
        font=("Segoe UI", 11, "bold"),
        cursor="hand2"
    )

    # Posiciona o botão da Marvel
    button_marvel.pack(
        side="left",
        expand=True,
        fill="x",
        padx=(5, 5),
        ipady=8
    )

    # Botão para carregar somente as HQs da DC
    button_dc = ctk.CTkButton(
        painel_filtros,
        text="DC",
        command=carregar_dc,
        fg_color="#0B1F3A",
        hover_color="#163A63",
        text_color="#FFD700",
        corner_radius=8,
        font=("Segoe UI", 11, "bold"),
        cursor="hand2"
    )

    # Posiciona o botão da DC
    button_dc.pack(
        side="left",
        expand=True,
        fill="x",
        padx=(5, 15),
        ipady=8
    )

    # Função central que decide o que fazer quando um item da lista
    # é selecionado, de acordo com o nível de navegação atual
    def ao_selecionar_item(evento):

        nonlocal hqs_atual

        if nivel_atual == "hqs":

            selecao = lista_hqs.curselection()

            if not selecao:
                return

            indice = selecao[0]

            # Quando existe pesquisa, usa a lista filtrada
            lista_selecao = (
                itens_pesquisa_atual
                if barra_pesquisa.get().strip()
                else hqs_atual
            )

            if indice >= len(lista_selecao):
                return

            selecionar_hq(
                lista_hqs,
                lista_selecao,
                texto_selecao,
                capa_hq,
                pag_hq,
                formato_hq,
                editora_hq,
                personagem_hq
            )

            # Atualiza o contexto da HQ selecionada
            if biblioteca_atual is not None:

                editora_hq.config(
                    text=f"🏢  {label_editora.cget('text')}"
                )

                if personagem_atual:

                    personagem_hq.config(
                        text=f"🦸  {personagem_atual}"
                    )

                else:

                    personagem_hq.config(
                        text=""
                    )

        elif nivel_atual == "personagens":

            selecao = lista_hqs.curselection()

            if selecao:

                indice = selecao[0]

                lista_selecao = (
                    itens_pesquisa_atual
                    if barra_pesquisa.get().strip()
                    else personagens_atual
                )

                if indice >= len(lista_selecao):
                    return

                personagem = lista_selecao[indice]

                # Guarda a tela de personagens atual antes de avançar,
                # para o botão VOLTAR poder reconstruí-la depois
                pilha_navegacao.append(
                    ("personagens", biblioteca_atual)
                )

                mostrar_hqs_personagem(
                    biblioteca_atual,
                    personagem
                )

        elif nivel_atual == "hqs_personagem":

            selecao = lista_hqs.curselection()

            if selecao:

                indice = selecao[0]

                lista_selecao = (
                    itens_pesquisa_atual
                    if barra_pesquisa.get().strip()
                    else hqs_personagem_atual
                )

                if indice >= len(lista_selecao):
                    return

                nome_hq = lista_selecao[indice]

                # Guarda a tela de pastas de HQ atual antes de avançar,
                # para o botão VOLTAR poder reconstruí-la depois
                pilha_navegacao.append(
                    (
                        "hqs_personagem",
                        biblioteca_atual,
                        personagem_atual
                    )
                )

                mostrar_edicoes_hq(
                    biblioteca_atual,
                    personagem_atual,
                    nome_hq
                )

        elif nivel_atual == "subpastas":

            selecao = lista_hqs.curselection()

            if not selecao:
                return

            indice = selecao[0]

            # Quando existe pesquisa, usa os itens filtrados
            if barra_pesquisa.get().strip():

                if indice >= len(itens_pesquisa_atual):
                    return

                tipo_item, item = itens_pesquisa_atual[indice]

                if tipo_item == "edicao":

                    edicoes = listar_edicoes(
                        biblioteca_atual,
                        personagem_atual,
                        hq_atual_navegacao
                    )

                    indice_edicao = edicoes.index(item)

                    selecionar_hq(
                        lista_hqs,
                        edicoes,
                        texto_selecao,
                        capa_hq,
                        pag_hq,
                        formato_hq,
                        editora_hq,
                        personagem_hq
                    )

                    # Seleciona temporariamente a edição correta
                    lista_hqs.selection_clear(
                        0,
                        tk.END
                    )

                    lista_hqs.selection_set(
                        indice
                    )

                    editora_hq.config(
                        text=f"🏢  {label_editora.cget('text')}"
                    )

                    personagem_hq.config(
                        text=f"🦸  {personagem_atual}"
                    )

                else:

                    nome_subpasta = item

                    pilha_navegacao.append(
                        (
                            "subpastas",
                            biblioteca_atual,
                            personagem_atual,
                            hq_atual_navegacao
                        )
                    )

                    mostrar_edicoes_subpasta(
                        biblioteca_atual,
                        personagem_atual,
                        hq_atual_navegacao,
                        nome_subpasta
                    )

                return

            edicoes = listar_edicoes(
                biblioteca_atual,
                personagem_atual,
                hq_atual_navegacao
            )

            subpastas = listar_subpastas(
                biblioteca_atual,
                personagem_atual,
                hq_atual_navegacao
            )

            # As primeiras posições pertencem às edições principais
            if indice < len(edicoes):

                selecionar_hq(
                    lista_hqs,
                    edicoes,
                    texto_selecao,
                    capa_hq,
                    pag_hq,
                    formato_hq,
                    editora_hq,
                    personagem_hq
                )

                editora_hq.config(
                    text=f"🏢  {label_editora.cget('text')}"
                )

                personagem_hq.config(
                    text=f"🦸  {personagem_atual}"
                )

            else:

                indice_subpasta = indice - len(edicoes)

                nome_subpasta = subpastas_atual[
                    indice_subpasta
                ]

                pilha_navegacao.append(
                    (
                        "subpastas",
                        biblioteca_atual,
                        personagem_atual,
                        hq_atual_navegacao
                    )
                )

                mostrar_edicoes_subpasta(
                    biblioteca_atual,
                    personagem_atual,
                    hq_atual_navegacao,
                    nome_subpasta
                )

    # Evento responsável por detectar quando um item é selecionado
    # (seja uma HQ ou um personagem, dependendo do nível atual)
    lista_hqs.bind(
        "<<ListboxSelect>>",
        ao_selecionar_item
    )

    # Inicializa as informações da biblioteca
    atualizar_estatisticas(
        None,
        "TODAS"
    )

    # Loop da interface, ao fechar será cancelado o loop
    janela.mainloop()