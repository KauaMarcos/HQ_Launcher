import tkinter as tk

def iniciar_interface():

    janela = tk.Tk()

    janela.title("HQ Launcher")

    janela.geometry("900x600")

    frame_hqs = tk.Frame(janela, bg='grey')
    frame_hqs.pack(fill="both", expand=True)

    label = tk.Label(frame_hqs,text="Minhas HQS")
    label.pack()

    janela.mainloop()