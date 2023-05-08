#Importamos librerias
import RPi.GPIO as GPIO
import time

# Configuración del modo de pines
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



class Servo:
    
    def __init__(self, angulo, pin):
        self.angulo = angulo #Angulo actual
        
        self.pwm = GPIO.PWM(pin, 50)# Frecuencia de 50 Hz servo
        self.pwm.start(self.angulo)

    #Mover Servo al angulo actual
    def set_angle(self):
        duty_cycle = self.angulo / 18.0 + 2.5  # Calculo del ciclo de trabajo
        self.pwm.ChangeDutyCycle(duty_cycle)
    
    #Calcular el nuevo angulo actual en vase a la direccion
    def calc_angulos(self, Direccion):
        if self.angulo+Direccion<145 and self.angulo+Direccion>25:# el angulo del motor debe de estar entre 25 y 145.
            self.angulo += Direccion
