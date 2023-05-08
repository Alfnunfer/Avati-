#Importamos librerias
import RPi.GPIO as GPIO
import time

# Configuración del modo de pines
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Led:
	
	def __init__(self):
		
		#Color actual del led
		self.LedC = [0,0,0]
		
		#Diccionario con todos los colores
		self.Clolores = {'K':[0,0,0],
						'W':[1,1,1],
						'R':[1,0,0],
						'Y':[1,1,0],
						'G':[0,1,0],
						'C':[0,1,1],
						'B':[0,0,1],
						'M':[1,0,1]}
    
	# Encender el LED
	def EncenderLed(self, pin):
		#print("Encendiendo el LED...")
		GPIO.output(pin, GPIO.HIGH)

	# Apagar el LED
	def ApagarLed(self, pin):
		#print("Apagando el LED...")
		GPIO.output(pin, GPIO.LOW)
    
    #Cambio el color actual
	def color_actual(self, color):
		self.LedC = self.Clolores[color]
		
	#Actualizo el led
	def Actualizar_Led(self):
		
		if self.LedC[0]==1:
			self.EncenderLed(13)
		else:
			self.ApagarLed(13)
		if self.LedC[1]==1:
			self.EncenderLed(19)
		else:
			self.ApagarLed(19)
		if self.LedC[2]==1:
			self.EncenderLed(26)
		else:
			self.ApagarLed(26)
