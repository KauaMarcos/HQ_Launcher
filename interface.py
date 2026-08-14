import tkinter as tk
from biblioteca import carregar_hqs
from Launcher import abrir_hq




COR_DO_FUNDO = "#101014"
COR_DO_PAINEL = "#18181f"
COR_TEXTO = "#FFFFFF"
COR_TEXTO_SECUNDARIO = "#A0A0AA"
COR_DESTAQUE = "#E63946"


# Função de carregar hq dentro da interface,
# aí pega a função de carregar_hq de biblioteca
# foi criado uma variável lista_hqs pra colocar dentro da interface
def carregar_hq_interface(lista_hqs, hqs):

    hqs = carregar_hqs()

    # Foi criado para não duplicar as Hqs ao clicar no botão mais de uma vez
    lista_hqs.delete(0, tk.END)

    # Foi criado para inserir cada hq do inicio ao fim da pasta
    for hq in hqs:
        lista_hqs.insert(tk.END, hq)


# Foi criado para Selecionar as hqs na interface
def selecionar_hq(lista_hqs, hqs):

    selecao = lista_hqs.curselection()

    if selecao:
        hq = hqs[selecao[0]]
        print(f"Hq Selecionada foi: {hq} \n")


# Foi Criado para abrir a hq selecionada na interface
def abrir_hq_interface(lista_hqs, hqs):

    hq_selecionada = lista_hqs.curselection()

    if not hq_selecionada:
        print("Nenhuma HQ Selecionada.")
        return

    hq = lista_hqs.get(hq_selecionada[0])

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

    # Botão para Carregar HQ,
    # command=lambda: dar um comando para chamar a função carregar_hq_interface
    # e mostrar as hqs com lista_hqs
    button = tk.Button(
        painel_botoes,
        text="CARREGAR HQS",
        command=lambda: carregar_hq_interface(lista_hqs, hqs),
        bg=COR_DESTAQUE,
        fg=COR_TEXTO,
        activebackground=COR_DESTAQUE,
        activeforeground=COR_TEXTO,
        relief="flat",
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


    # =========================
    # BOTÃO VER SELEÇÃO
    # =========================

    # Botão para Selencionar HQ,
    # command=lambda: dar um comando para chamar a função selecionar_hq
    # e mostrar as hqs com lista_hqs
    button_selecion = tk.Button(
        painel_botoes,
        text="VER SELEÇÃO",
        command=lambda: selecionar_hq(lista_hqs, hqs),
        bg=COR_DO_FUNDO,
        fg=COR_TEXTO,
        activebackground=COR_DESTAQUE,
        activeforeground=COR_TEXTO,
        relief="flat",
        font=("Arial", 10),
        cursor="hand2"
    )

    # Posiciona o Botão de Selecionar Hqs dentro do Frame
    button_selecion.pack(
        side="left",
        expand=True,
        fill="x",
        padx=5,
        ipady=8
    )

    # Botão para Abrir HQ,
    # command=lambda: dar um comando para chamar a função abrir_hq_interface
    button_open_hq = tk.Button(
        painel_botoes,
        text="ABRIR HQ",
        command=lambda: abrir_hq_interface(lista_hqs, hqs),
        bg=COR_DO_FUNDO,
        fg=COR_TEXTO,
        activebackground=COR_DESTAQUE,
        activeforeground=COR_TEXTO,
        relief="flat",
        font=("Arial", 10, "bold"),
        cursor="hand2"
    )

    # Posiciona o Botão de Abrir Hqs dentro do Frame
    button_open_hq.pack(
        side="left",
        expand=True,
        fill="x",
        padx=(5, 0),
        ipady=8
    )


    # Carrega as HQs usando a função carregar_hqs
    hqs = carregar_hqs()


    # Loop da interface, ao fechar será cancelado o loop
    janela.mainloop()