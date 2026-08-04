from biblioteca import carregar_hqs

hqs = carregar_hqs()

for hq in hqs:
    print(hq.name)
print(f"Foram encontradas: {len(hqs)} HQS!")
