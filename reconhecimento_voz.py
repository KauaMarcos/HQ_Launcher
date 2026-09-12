import speech_recognition as sr
import threading
 
 
# Função responsável por ouvir o microfone 
def ouvir(): 
 
    # Cria o objeto responsável pelo reconhecimento de voz 
    reconhecedor = sr.Recognizer() 
 
    # Acessa o microfone 
    with sr.Microphone() as microfone: 
 
        print("Fale alguma coisa...") 
 
        # Captura o áudio do microfone 
        audio = reconhecedor.listen(microfone) 
 
    # Tenta transformar o áudio em texto 
    try: 
 
        texto = reconhecedor.recognize_google( 
            audio, 
            language="pt-BR" 
        ) 
 
        # Retorna o texto reconhecido 
        return texto 
 
    # Caso o áudio não seja compreendido 
    except sr.UnknownValueError: 
 
        print("Não consegui entender o que foi dito.") 
 
        return None 
 
    # Caso aconteça algum problema no serviço 
    except sr.RequestError as erro: 
 
        print(f"Erro no reconhecimento de voz: {erro}") 
 
        return None 
 
 
# Função responsável por interpretar o comando recebido 
def interpretar_comando(texto): 
 
    # Verifica se algum texto foi reconhecido 
    if texto is None: 
 
        return None 
 
    # Deixa o texto em letras minúsculas 
    texto = texto.lower().strip() 
 
    # Verifica se o usuário pediu para abrir a Marvel 
    if "abrir marvel" in texto: 
 
        return "marvel" 
 
    # Verifica se o usuário pediu para abrir a DC 
    if "abrir dc" in texto: 
 
        return "dc" 
 
    if "lara" in texto: 
 
        return "É GOSTOSONA!" 
 
    # Caso nenhum comando seja reconhecido 
    return None 
 
 
# Função responsável por manter o microfone ouvindo 
def ouvir_continuamente(callback=None): 
 
    # Mantém a escuta funcionando continuamente 
    while True: 
 
        # Ouve uma frase através do microfone 
        texto = ouvir() 
 
        # Interpreta o texto reconhecido 
        comando = interpretar_comando(texto) 
 
        # Mostra o comando identificado no terminal 
        print(f"Comando identificado: {comando}") 
 
        # Envia o comando para quem iniciou a escuta 
        if callback and comando: 
 
            callback(comando) 
 
 
# Função responsável por iniciar a escuta em segundo plano 
def iniciar_escuta(callback=None): 
 
    # Cria uma thread para executar a escuta contínua 
    thread = threading.Thread( 
        target=ouvir_continuamente, 
        args=(callback,), 
        daemon=True 
    ) 
 
    # Inicia a thread 
    thread.start() 
 
 
# Teste da função 
if __name__ == "__main__": 
 
    iniciar_escuta() 
 
    input("Pressione ENTER para encerrar...\n")