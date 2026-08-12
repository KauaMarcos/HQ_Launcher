import tkinter as tk
from biblioteca import carregar_hqs
from Launcher import abrir_hq   

### CORES DA INTERFACE ###
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
    cabeçalho = tk.Frame(janela,
                          bg=COR_DO_FUNDO,)
    # Posiciona o cabeçalho na parte superior
    cabeçalho.pack(fill="x",
                   padx=30,
                   pady=(25,15))
    # Título principal do programa
    titulo = tk.Label(cabeçalho,
                      text="HQ Launcher",
                      fg=COR_TEXTO,
                      bg=COR_DO_FUNDO,
                      font=("Arial", 26, "bold"))
    # Alinha o título à esquerda
    titulo.pack(anchor="w")

    # Subtítulo do programa
    subtitulo = tk.Label(cabeçalho,
                         text="Minha Biblioteca de HQs",
                         fg=COR_TEXTO_SECUNDARIO,
                         bg=COR_DO_FUNDO,
                         font=("Arial", 11))

    # Posiciona o subtítulo abaixo do título
    subtitulo.pack(anchor="w", pady=(3, 0))

    # Área onde ficarão os principais elementos do Launcher
    area_principal = tk.Frame(janela,
                              bg=COR_DO_PAINEL)
    # Faz a área ocupar o espaço disponível
    area_principal.pack(fill="both", expand=True, padx=30, pady=10)


    # Painel onde ficará a lista de HQs
    painel_biblioteca = tk.Frame(area_principal,
                                 bg=COR_DO_PAINEL)
    # Posiciona o painel no lado esquerdo
    painel_biblioteca.pack(side="left", fill="both", expand=True)

    # Título da biblioteca de HQs
    titulo_biblioteca = tk.Label(painel_biblioteca, 
                                 text="📚Biblioteca",
                                 fg=COR_TEXTO,
                                 bg=COR_DO_PAINEL,
                                 font=("Arial", 14, "bold"))
    
    # Posiciona o título dentro do painel
    titulo_biblioteca.pack(anchor="w", padx=20, pady=(20, 10))

    # Espaço dentro da janela
    frame_hqs = tk.Frame(janela, bg='grey')

    # Posiciona o frame dentro da janela
    frame_hqs.pack(fill="both", expand=True)

    # Componente para Texto na interface
    label = tk.Label(frame_hqs, text="Minhas HQS")

    # Posiciona o label dentro do frame
    label.pack()

    # Componente para Lista de HQs na interface
    lista_hqs = tk.Listbox(frame_hqs)

    # Posiciona a lista de hqs dentro do frame
    lista_hqs.pack()

    # Carrega as HQs usando a função carregar_hqs
    hqs = carregar_hqs()

    # Botão para Carregar HQ,
    # command=lambda: dar um comando para chamar a função carregar_hq_interface
    # e mostrar as hqs com lista_hqs
    button = tk.Button(frame_hqs,
                        text="CARREGAR HQS",
                          command=lambda:carregar_hq_interface(lista_hqs, hqs))

    # Posiciona o Botão de carregar Hqs dentro do Frame
    button.pack()

    # Botão para Selencionar HQ,
    #  command=lambda: dar um comando para chamar a função selecionar_hq
    # e mostrar as hqs com lista_hqs
    button_selecion = tk.Button(frame_hqs,
                                 text="VER SELEÇÃO",
                                 command=lambda: selecionar_hq(lista_hqs, hqs))

    # Posiciona o Botão de Selecionar Hqs dentro do Frame
    button_selecion.pack()

    # Botão para Abrir HQ,
    #  command=lambda: dar um comando para chamar a função abrir_hq_interface
    button_open_hq = tk.Button(frame_hqs,
                              text="ABRIR HQ",
                              command=lambda: abrir_hq_interface(lista_hqs, hqs))

    # Posiciona o Botão de Abrir Hqs dentro do Frame
    button_open_hq.pack()
    # Loop da interface, ao fechar será cancelado o loop
    janela.mainloop()