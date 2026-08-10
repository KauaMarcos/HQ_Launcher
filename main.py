from biblioteca import carregar_hqs
from Launcher import abrir_hq
from interface import iniciar_interface
hqs = carregar_hqs()


# Abrir Hq pelo index
# if hqs:
# abrir_hq(hqs[8])


if __name__ == "__main__":
    iniciar_interface()



# Mostrar nome das hq's no terminal
# for hq in hqs:
    # print(hq.name)

# Mostrar a quantidades de HQ's 
# print(f"AQUI TEM {len(hqs)} HQ'S")