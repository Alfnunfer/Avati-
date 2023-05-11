import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.video import Video
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import pyaudio
import socket
import struct
import pickle
import cv2
import cProfile
import numpy as np
from io import BytesIO
import wave
import pygame



kivy.require('1.11.1') # Versión mínima de Kivy requerida

# Configuración del servidor
HOST = '10.212.5.49' # Dirección IP del servidor (en este caso, se usa la dirección local)
PORT = 5000 # Puerto en el que el servidor escuchará las conexiones entrantes

# Configuración de la captura de audio
CHUNK = 1024*4 # Tamaño del buffer de audio
FORMAT = pyaudio.paInt16 # Formato de audio
CHANNELS = 1 # Número de canales (mono)
RATE = 44100 # Tasa de muestreo
audio = pyaudio.PyAudio() # Inicializamos la clase PyAudio
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
stream2 = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)


def send_audio(conn, data):
    # Serializamos los datos utilizando la biblioteca "pickle"
    data_serialized = pickle.dumps(data)
    # Enviamos los datos al cliente
    conn.sendall(struct.pack("H", len(data_serialized)) + data_serialized)
    #conn.sendall(data_serialized)


# Clase que representa la pantalla de la aplicación
class VideoScreen(Widget):
    def __init__(self, **kwargs):
        

        super(VideoScreen, self).__init__(**kwargs)
        # Iniciamos la conexión con el servidorbuffer = cv2.flip(frame, 0).tobytes()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        
        print(f"Conectado al servidor {HOST}:{PORT}")
        # Iniciamos la reproducción de audio
        #self.sound = SoundLoader#.load(None)


        # Creamos un widget de imagen para mostrar la imagen recibida
        self.image = Image()
        self.add_widget(self.image)

    def update(self, dt):
        # Recibimos los datos de video del servidor
        
        
        # Recibimos el tamaño de los datos
        #data_size = struct.unpack("B", self.sock.recv(struct.calcsize("B")))[0]
        data_size = struct.unpack("I", self.sock.recv(4))[0]

        print('data_size',data_size)
        data_size=921765
        # Recibimos los datos en sí y los deserializamos
        frame_data = b''
        while len(frame_data) < data_size:
            
            packet = self.sock.recv(data_size - len(frame_data))
            if not packet:
                break
            frame_data += packet

        

        if frame_data:
        # Deserializamos los datos de video

            frame = pickle.loads(frame_data)
            #print(len(frame))
            
            frame = cv2.flip(frame, 0)
            
            window_size = Window.size
            max_size = max(window_size)
            scale = max_size / max(frame.shape[:2])
            frame = cv2.resize(frame, None, fx=scale, fy=scale)         

            # Decodificamos los datos de la imagen y la mostramos en el widget de imagen
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(frame.tobytes(), colorfmt='bgr')#, bufferfmt='ubyte'
            self.image.size = (Window.width, Window.height)
            self.image.texture = texture

            # Solicitamos la actualización de la pantalla
            self.image.canvas.ask_update()
    
        
        # Recibimos los datos de audio del servidor
        
        # Recibimos el tamaño de los datos
        audio_size = struct.unpack("H", self.sock.recv(struct.calcsize("H")))[0]
        print('audio_size',audio_size)
        
        # Recibimos los datos en sí y los deserializamos
        audio_data = b''
        while len(audio_data) < audio_size:
            packet = self.sock.recv(audio_size - len(audio_data))
            if not packet:
                break
            audio_data += packet
        #audio_data = self.sock.recv(CHUNK)
        audio_data = pickle.loads(audio_data)
        #print(audio_data)
        if audio_data:
            # Reproducimos los datos de audio recibidos
            stream.stop_stream()
            if not stream.is_active():
                stream.start_stream()
            stream.write(audio_data)


        
        # Capturamos un buffer de audio y lo enviamos al cliente
        #stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        audio_data = stream2.read(CHUNK)
        #send_data(conn, audio_data)
        send_audio(self.sock, audio_data)
        #print(len(audio_data))

# Clase que representa la aplicación
class VideoApp(App):
    def build(self):
        # Creamos la pantalla de la aplicación
        screen = VideoScreen()
        # Actualizamos la pantalla a una tasa de 30 FPS
        Clock.schedule_interval(screen.update, 1.0/30.0)
        return screen
VideoApp=VideoApp()
# Iniciamos la aplicación
if __name__ == '__main__':
    VideoApp.run()

