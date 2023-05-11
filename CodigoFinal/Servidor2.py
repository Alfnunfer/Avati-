import cv2
import pyaudio
import socket
import struct
import pickle

# Configuración del servidor
HOST = '10.212.5.49' # Dirección IP del servidor (en este caso, se usa la dirección local)
PORT = 5000 # Puerto en el que el servidor escuchará las conexiones entrantes

# Configuración de la captura de video
cap = cv2.VideoCapture(0) # Capturamos el video de la cámara principal

# Configuración de la captura de audio
CHUNK = 1024*4 # Tamaño del buffer de audio
FORMAT = pyaudio.paInt16 # Formato de audio
CHANNELS = 1 # Número de canales (mono)
RATE = 44100 # Tasa de muestreo
audio = pyaudio.PyAudio() # Inicializamos la clase PyAudio
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
stream2 = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

# Función que envía los datos al cliente
def send_data(conn, data):
    # Serializamos los datos utilizando la biblioteca "pickle"
    data_serialized = pickle.dumps(data)
    # Enviamos los datos al cliente
    print('data_serialized',len(data_serialized))
    conn.sendall(struct.pack("I", len(data_serialized)) + data_serialized)
    #conn.sendall(data_serialized)
def send_data2(conn, data):
    # Serializamos los datos utilizando la biblioteca "pickle"
    data_serialized = pickle.dumps(data)
    # Enviamos los datos al cliente
    print('data_serialized',len(data_serialized))
    conn.sendall(data_serialized)
    #conn.sendall(data_serialized)
def send_audio(conn, data):
    # Serializamos los datos utilizando la biblioteca "pickle"
    data_serialized = pickle.dumps(data)
    # Enviamos los datos al cliente
    #print(data)
    print('audio_serialized',len(data_serialized))
    conn.sendall(struct.pack("H", len(data_serialized)) + data_serialized)
    #conn.sendall(data_serialized)

# Función que recibe los datos del cliente
def receive_audio(conn):
    # Recibimos el tamaño de los datos
    audio_size = struct.unpack("H", conn.recv(struct.calcsize("H")))[0]
    # Recibimos los datos en sí y los deserializamos
    audio_data = b''
    while len(audio_data) < audio_size:
        packet = conn.recv(audio_size - len(audio_data))
        if not packet:
            break
        audio_data += packet
    data = pickle.loads(audio_data)
    return data

# Creamos el socket del servidor y lo ponemos a escuchar conexiones entrantes
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor iniciado en {HOST}:{PORT}")
    
    while True:
        
    
        conn, addr = s.accept()
        print(f"Cliente conectado desde {addr[0]}:{addr[1]}")

        # Iniciamos el streaming de video y audio
        #try:
        while True:
            # Capturamos un frame de video y lo enviamos al cliente
            ret, frame = cap.read()
            send_data(conn, frame)
            #print(len(frame))
            
            # Capturamos un buffer de audio y lo enviamos al cliente
            #stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
            audio_data = stream.read(CHUNK)
            #send_data(conn, audio_data)
            send_audio(conn, audio_data)
            #print(len(audio_data))

            
            # Recibimos el audio enviado por el cliente y lo reproducimos
            audio_data2 = receive_audio(conn)
            if audio_data2:
                stream2.stop_stream()
                if not stream2.is_active():
                    stream2.start_stream()
                stream2.write(audio_data2)
        #except:
            #print('Cliente desconectado')
