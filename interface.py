import tkinter as tk
import zipfile
import rarfile
from io import BytesIO
from PIL import Image, ImageTk
from biblioteca import carregar_hqs, pegar_capa, contar_paginas, carregar_hqs_marvel, carregar_hqs_dc
from Launcher import abrir_hq
import customtkinter as ctk

COR_DO_FUNDO = "#101014"
COR_DO_PAINEL = "#18181f"
COR_TEXTO = "#FFFFFF"
COR_TEXTO_SECUNDARIO = "#A0A0AA"
COR_DESTAQUE = "#E63946"


# Função de carregar hq dentro da interface,
# recebe uma lista de Hqs e mostra elas na biblioteca
def carregar_hq_interface(lista_hqs, hqs):

    # Foi criado para não duplicar as Hqs ao clicar no botão mais de uma vez
    lista_hqs.delete(0, tk.END)

    # Foi criado para inserir cada hq do inicio ao fim da lista recebida
    for hq in hqs:
        lista_hqs.insert(tk.END, hq.name)


# Foi criado para Selecionar as hqs na interface
def selecionar_hq(lista_hqs, hqs, texto_selecao, capa_hq, pag_hq):

    selecao = lista_hqs.curselection()

    if selecao:

        hq = hqs[selecao[0]]

        print(f"Hq Selecionada foi: {hq}\n")

        # Atualiza o texto do painel de informações
        texto_selecao.config(
            text=f"HQ selecionada:\n\n{hq.name}"
        )

        # Conta a quantidade de páginas da HQ
        paginas = contar_paginas(hq)

        pag_hq.config(
            text=f"📄 Página Atual: 0\n📄 Total de Páginas: {paginas}"
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
    janela.geometry("1000x650")

    # Cor de Fundo da Janela
    janela.configure(bg=COR_DO_FUNDO)

    janela.resizable(False, False)

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
        text="HQ Launcher",
        fg=COR_TEXTO,
        bg=COR_DO_FUNDO,
        font=("Arial", 26, "bold")
    )

    # Alinha o título à esquerda
    titulo.pack(anchor="w")

    # Subtítulo do programa
    subtitulo = tk.Label(
        cabeçalho,
        text="Minha Biblioteca de HQs",
        fg=COR_TEXTO_SECUNDARIO,
        bg=COR_DO_FUNDO,
        font=("Arial", 11)
    )

    # Posiciona o subtítulo abaixo do título
    subtitulo.pack(
        anchor="w",
        pady=(3, 0)
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
        bg=COR_DO_PAINEL
    )

    painel_info.pack(
        side="right",
        fill="both",
        expand=True,
        padx=(10, 0)
    )

    # Título do painel de informações
    titulo_informacoes = tk.Label(
        painel_info,
        text="📖 Informações",
        fg=COR_TEXTO,
        bg=COR_DO_PAINEL,
        font=("Arial", 14, "bold")
    )

    # Posiciona o título dentro do painel
    titulo_informacoes.pack(
        anchor="w",
        padx=20,
        pady=(20, 10)
    )

    # Texto que será mostrado quando nenhuma HQ estiver selecionada
    texto_selecao = tk.Label(
        painel_info,
        text="Nenhuma HQ selecionada",
        fg=COR_TEXTO_SECUNDARIO,
        bg=COR_DO_PAINEL,
        font=("Arial", 11)
    )

    # Posiciona o texto dentro do painel
    texto_selecao.pack(
        anchor="w",
        padx=20,
        pady=10
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

    # Informação das páginas da HQ
    pag_hq = tk.Label(
        painel_info,
        text="📄 Página Atual: 0\n",
        fg=COR_TEXTO,
        bg=COR_DO_PAINEL,
        font=("Arial", 11)
    )

    pag_hq.pack(
        anchor="w",
        padx=20,
        pady=10
    )

    # Título da biblioteca de HQs
    titulo_biblioteca = tk.Label(
        painel_biblioteca,
        text="📚 Biblioteca",
        fg=COR_TEXTO,
        bg=COR_DO_PAINEL,
        font=("Arial", 14, "bold")
    )

    # Posiciona o título dentro do painel
    titulo_biblioteca.pack(
        anchor="w",
        padx=20,
        pady=(20, 10)
    )

    # Componente para Lista de HQs na interface
    lista_hqs = tk.Listbox(
        painel_biblioteca,
        bg=COR_DO_FUNDO,
        fg=COR_TEXTO,
        selectbackground=COR_DESTAQUE,
        selectforeground=COR_TEXTO,
        font=("Arial", 11),
        relief="flat",
        highlightthickness=0
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
            padx=(10,0)
    )
    # Carrega as HQs usando a função carregar_hqs
    hqs = carregar_hqs()

    # Carrega somente as HQs da Marvel
    hqs_marvel = carregar_hqs_marvel()

    # Carrega somente as HQs da DC
    hqs_dc = carregar_hqs_dc()

    # Guarda a lista de Hqs que está sendo mostrada atualmente
    hqs_atual = hqs


    # Função para carregar todas as HQs
    def carregar_todas():

        nonlocal hqs_atual

        hqs_atual = hqs

        carregar_hq_interface(
            lista_hqs,
            hqs_atual
        )

    # Função para carregar somente as HQs da Marvel
    def carregar_marvel():

        nonlocal hqs_atual

        hqs_atual = hqs_marvel

        carregar_hq_interface(
            lista_hqs,
            hqs_atual
        )

    # Função para carregar somente as HQs da DC
    def carregar_dc():

        nonlocal hqs_atual

        hqs_atual = hqs_dc

        carregar_hq_interface(
            lista_hqs,
            hqs_atual
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
        font=("Arial", 10, "bold"),
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
        painel_botoes,
        text="ABRIR HQ",
        command=lambda: abrir_hq_interface(
            lista_hqs,
            hqs_atual
    ),
        fg_color="#FFFFFF",
        hover_color="#D9D9D9",
        text_color="#101014",
        corner_radius=10,
        font=("Arial", 11, "bold"),
        height=40,
        cursor="hand2"
    )
    # Posiciona o Botão de Abrir Hqs dentro do Frame
    button_open_hq.pack(
        side='left',
        expand=True,
        fill="x",
        padx=(10,0)
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
         font=("Helvetica", 11, "bold"),
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
           font=("Helvetica", 11, "bold"),
           cursor="hand2"
    )

    # Posiciona o botão da DC
    button_dc.pack(
        side="left",
        expand=True,
        fill="x",
        padx=(5, 5),
        ipady=8
    )

    # Evento responsável por detectar quando uma HQ é selecionada
    lista_hqs.bind(
        "<<ListboxSelect>>",
        lambda evento: selecionar_hq(
            lista_hqs,
            hqs_atual,
            texto_selecao,
            capa_hq,
            pag_hq
        )
    )

    # Loop da interface, ao fechar será cancelado o loop
    janela.mainloop()