import tkinter as tk
from biblioteca import carregar_hqs

# Função de carregar hq dentro da interface,
# aí pega a função de carregar_hq de biblioteca
# foi criado uma variável lista_hqs pra colocar dentro da interface
def carregar_hq_interface(lista_hqs):
    hqs = carregar_hqs()

    print(hqs)
    print(f"AQUI TEM {len(hqs)} HQS \n")

    # Foi criado para não duplicar as Hqs ao clicar no botão mais de uma vez
    lista_hqs.delete(0, tk.END)
    # Foi criado para inserir cada hq do inicio ao fim da pasta
    for hq in hqs:
        lista_hqs.insert(tk.END, hq)

# Função para iniciar interface
def iniciar_interface():

    # Abrir Janela
    janela = tk.Tk()

    # Título da interface  
    janela.title("HQ Launcher")

    # Tamanho Da Janela
    janela.geometry("900x600")

    # Espaço dentro da janela
    frame_hqs = tk.Frame(janela, bg='grey')

    # Posiciona o frame dentro da janela
    frame_hqs.pack(fill="both", expand=True)

    # Componente para Texto na interface
    label = tk.Label(frame_hqs, text="Minhas HQS")

    # Posiciona o label dentro do frame
    label.pack()

    lista_hqs = tk.Listbox(frame_hqs)

    lista_hqs.pack()

    # Botão para abrir HQ,
    # command=lambda: dar um comando para chamar a função carregar_hq_interface
    # e mostrar as hqs com lista_hqs
    button = tk.Button(frame_hqs,
                        text="CARREGAR HQS",
                          command=lambda:carregar_hq_interface(lista_hqs))

    # Posiciona o Botão dentro do Frame
    button.pack()

    # Loop da interface, ao fechar será cancelado o loop
    janela.mainloop()