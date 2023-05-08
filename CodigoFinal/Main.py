#Importamos librerias
import RPi.GPIO as GPIO
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
import random
import threading



#Importamos los codigos
from Leds import Led
from Control import Servo
from LedOjos import Ojos

# Configuración del modo de pines
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configuración de la conexión SPI (matriz led)
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)
Emocion = 'Normal' #Estado de los Ojos

# Configuración del pin del LED
led_pin = [13,19,26]
for i in led_pin:
    GPIO.setup(i, GPIO.OUT)

# Configuración del pin del servo
servo_pin1 = 23
servo_pin2 = 24
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)

#Variables motores
servo_ang1 = 90
servo_ang2 = 90

Direccion = [0,0] #Dirección de giro de la cabeza

#Defino las variables
led = Led()
led.Actualizar_Led()
motor1 = Servo(servo_ang1, servo_pin1)
motor2 = Servo(servo_ang2, servo_pin2)
ojos = Ojos()

#Funcion que calcula y modifica el angulo de los motores
def control_motor():
    print(1)
    while True:
        motor1.calc_angulos(Direccion[0])
        motor1.set_angle()
        motor2.calc_angulos(Direccion[1])
        motor2.set_angle()
        time.sleep(0.1)

#Función que modifica los Ojos y los hace parpadear. Modificar para cambiar el comportamiento de los Ojos.
def control_ojo():
    print(2)
    while True:
        #Dependiendo de hacia donde havanza la cabeza del robot los ojos miran en una dirección o en otra
        try: 
            if Direccion[0]<-1:
                ojos.Mostrar(device, Emocion+'Izquierda')
            elif Direccion[0]>1:
                ojos.Mostrar(device, Emocion+'Derecha')
            else:
                ojos.Mostrar(device, Emocion)
        except:
            ojos.Mostrar(device, Emocion)
        
        time.sleep(random.random()*2+3) #Esperar entre 3-5 segundos
        
        #Función de parpadeo
        if Direccion[0]<-1:
            ojos.Mostrar(device, 'CerradoIzquierda')
        elif Direccion[0]>1:
            ojos.Mostrar(device, 'CerradoDerecha')
        else:
            ojos.Mostrar(device,'Cerrado')
        time.sleep(0.5)


#Creo dos hilos para que se encargen de los motores y los ojos
Hilo_Motor = threading.Thread(target=control_motor, name='Hilo_Motor')
Hilo_Ojo = threading.Thread(target=control_ojo, name='Hilo_Ojo')
Hilo_Motor.start()
Hilo_Ojo.start()


#Demo----------------------

led.color_actual('W')
led.Actualizar_Led()
Direccion = [0,0.4]
time.sleep(5)

Direccion = [0,-0.4]
time.sleep(5)

Direccion = [0,0]
time.sleep(1)
led.color_actual('B')
led.Actualizar_Led()
Emocion = 'MedioCerrado'
time.sleep(4)

Direccion = [1,0]
time.sleep(5)

Direccion = [-1,0]
time.sleep(5)

Direccion = [0,0]
time.sleep(1)

'''
led.color_actual('R')
led.Actualizar_Led()

i=0
while i<20:
    Emocion = 'AmongUs1'
    time.sleep(0.5)
    Emocion = 'AmongUs2'
    time.sleep(0.5)
    i+=1'''

#Demo----------------------

#Prueba Leds---------------
'''
led.color_actual('W')
led.Actualizar_Led()
time.sleep(1)
led.color_actual('R')
led.Actualizar_Led()
time.sleep(1)
led.color_actual('Y')
led.Actualizar_Led()
time.sleep(1)
led.color_actual('G')
led.Actualizar_Led()
time.sleep(1)
led.color_actual('C')
led.Actualizar_Led()
time.sleep(1)
led.color_actual('B')
led.Actualizar_Led()
time.sleep(1)
led.color_actual('M')
led.Actualizar_Led()
time.sleep(1)
'''
#Prueba Leds---------------


#Prueba Motor--------------
'''
i=0
while i<20:
    motor1.calc_angulos(Direccion[0])
    motor1.set_angle()
    motor2.calc_angulos(Direccion[0])
    motor2.set_angle()
    time.sleep(1)
    i+=1
'''
#Prueba Motor--------------


#Prueba Ojos---------------
'''
ojos.Mostrar(device,'Normal')
time.sleep(3)
ojos.Mostrar(device,'NormalIzquierda')
time.sleep(1)
ojos.Mostrar(device,'NormalDerecha')
time.sleep(1)
ojos.Mostrar(device,'Normal')
time.sleep(0.5)
ojos.Mostrar(device,'Cerrado')
time.sleep(0.5)
ojos.Mostrar(device,'Normal')
time.sleep(0.5)

ojos.Mostrar(device,'MedioCerrado')
time.sleep(3)
ojos.Mostrar(device,'MedioCerradoIzquierda')
time.sleep(1)
ojos.Mostrar(device,'MedioCerradoDerecha')
time.sleep(1)
ojos.Mostrar(device,'MedioCerrado')
time.sleep(0.5)
i=0
while i<5:
    ojos.Mostrar(device,'Corazon1')
    time.sleep(0.5)
    ojos.Mostrar(device,'Corazon2')
    time.sleep(0.5)
    i+=1
i=0
while i<20:
    ojos.Mostrar(device,'AmongUs1')
    time.sleep(0.5)
    ojos.Mostrar(device,'AmongUs2')
    time.sleep(0.5)
    i+=1
'''
#Prueba Ojos---------------


# Limpiar los pines y salir
GPIO.cleanup()
device.cleanup()
print("Fin del programa.")
