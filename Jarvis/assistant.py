import serial
import threading
import time
import speech_recognition as sr
import pyttsx3 

engine = pyttsx3.init()
voices = engine.getProperty('voices')

#count = 0;
#for voice in voices:
#    print(count, voice.name)
#    count += 1

voice = 1
#0 Microsoft Maria Desktop - Portuguese(Brazil)
#1 Microsoft Zira Desktop - English (United States)

engine.setProperty('voice', voices[voice].id)

r = sr.Recognizer()
mic = sr.Microphone()

conected = False
port = 'COM5'
baudRate = 115200

messagesReceived = 1
turnOffArduinoThread = False

speakText = False
textReceived = ""

try:
    SerialArduino = serial.Serial(port, baudRate, timeout = 0.2)
except:
    print("Verificar porta serial ou religar Arduino")

def handle_data(data):
    time.sleep(1)
    global messagesReceived, engine, speakText, textReceived
    #print("Recebi " + str(messagesReceived) + ": " + data)
    #messagesReceived += 1
    textReceived = data
    speakText = True

def read_from_port(ser):
    global conected, turnOffArduinoThread

    while not conected:
        conected = True

        while True:
            reading = ser.readline().decode()
            if reading != " ":
                handle_data(reading)
            if turnOffArduinoThread:
                print("Desligando Arduino")
                break

readSerialThread = threading.Thread(target = read_from_port, args = (SerialArduino,))
readSerialThread.start()

print("Preparando Arduino")
time.sleep(1)
print("Arduino Pronto")

engine.say("Welcome Juliane! Voice detection started")
time.sleep(15)

while (True):

    if speakText:
        engine.say(textReceived)
        engine.runAndWait()

        speakText = False
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Fale alguma coisa: ")
            audio = r.listen(source)
            time.sleep(3)
            print("Enviando para reconhecimento...")
        try: 
            text = r.recognize_google(audio, language = "pt-BR").lower()

            print("Você disse: {}".format(text))

            if text == "ligar" or text == "desligar":
                try: 
                    pass
                except:
                    print("Sem socket")

        
            #print("Enviando")
            SerialArduino.write((text + '\n').encode())
            time.sleep(1)

            print("Dado enviado")
            if(text == "desativar"):
                print("Saindo")

                deactivating = "Assistant deactivating."

                engine.say(deactivating)
                engine.runAndWait()

                engine.stop()
                turnOffArduinoThread = True
                SerialArduino.close()
                readSerialThread.join()
                break
        except:
            print("Não entendi o que você falou\n")

        time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("Apertou CTRL+C")
        engine.stop()
        turnOffArduinoThread = True
        SerialArduino.close()
        readSerialThread.join()
        break


#engine.say("Hello World!")
#engine.runAndWait()
#engine.stop()