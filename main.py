from biblioteca import carregar_hqs
from Launcher import abrir_hq

hqs = carregar_hqs()

if hqs:
    abrir_hq(hqs[8])


#for hq in hqs:
    #print(hq.name)

#print(f"AQUI TEM {len(hqs)} HQ'S")