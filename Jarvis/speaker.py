import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Fale alguma coisa")
    audio = r.listen(source)
    print("Enviando para reconhecimento")
    try:
        text = r.recognize_google(audio, language = "pt-BR")
        print("Você disse: {}".format(text))
    except:
        print("Não entendi o que você disse")