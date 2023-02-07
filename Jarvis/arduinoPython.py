import serial
import threading
import time

conected = False
port = 'COM5'
baudRate = 115200

messagesReceived = 1
turnOffArduinoThread = False

try:
    SerialArduino = serial.Serial(port, baudRate, timeout = 0.2)
except:
    print("Verificar porta serial ou religar Arduino")

def handle_data(data):
    time.sleep(5)
    global messagesReceived
    print("Recebi " + str(messagesReceived) + ": " + data)
    messagesReceived += 1

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
time.sleep(2)
print("Arduino Pronto")

while (True):
    try:
        print("Enviando")
        SerialArduino.write('ligar luzes\n'.encode())
        time.sleep(5)

    except KeyboardInterrupt:
        print("Apertou CTRL+C")
        turnOffArduinoThread = True
        SerialArduino.close()
        readSerialThread.join()
        break
