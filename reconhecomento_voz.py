import speech_recognition as sr


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


# Teste da função
texto = ouvir()

print(f"Você disse: {texto}")