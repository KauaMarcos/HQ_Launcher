from biblioteca import carregar_hqs
from interface import iniciar_interface
hqs = carregar_hqs()


# Executa a interface apenas quando o arquivo main.py
#  é chamado diretamente no terminal

if __name__ == "__main__":
    iniciar_interface()
