import tkinter as tk

def test():
    print("Botão clicado")

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

    # Botão para abrir HQ, coomand = dar um comando ao clicar no button
    button = tk.Button(frame_hqs, text="ABRIR HQ", command=test)

    # Posiciona o Botão dentro do Frame
    button.pack()

    # Loop da interface, ao fechar será cancelado o loop 
    janela.mainloop()