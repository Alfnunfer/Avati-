# Avatiñ@

## Descripción del proyecto:

Este proyecto se enfoca en ofrecer una solución para aquellos niños y niñas que no pueden asistir durante un período prolongado a clases presenciales por diversas razones, como pueden ser  hospitalizaciones o tratamientos domiciliarios de larga duración, ubicación geográfica, entre otras. 
El objetivo principal es mejorar aspectos socioemocionales relacionados con la ausencia del niño/a de su grupo de pares en el aula, como son:
- mejorar la percepción del niño/a ausente de minimizar su ausencia y participar en actividades del aula.
- promover la motivación del niño/a ausente en aspectos relacionados con su actividad escolar. 
- mejorar la percepción del grupo de compañeros/as de aula de la presencia real de su compañero/a ausente en su experiencia de aula.

La solución propuesta consiste en diseñar y desarrollar un avatar robótico social que les permita interactuar con sus compañeros y profesores de manera virtual y en tiempo real.


## Uso:

Actualmente solo están implementadas las funciones básicas (motores, leds). Ejecutando el archivo Main.py con el comando "python Main.py" se ejecutará una pequeña demostración. En un futuro se deberá implementar una aplicación móvil con la capacidad de conectarse, enviar y recibir información del robot.

Actualmente el código Main y Servidor2 se ejecuta automáticamente nada más encender el robot, si esto se quisiese cambiar solo haría falta ir al archivo en el directorio "/etc/rc.local" y modificar la linea "python /home/username/Desktop/Main.py &" y "python /home/username/Desktop/CodigoExtra/Servidor2.py &"

Para editar el codigo se puede usar el comando "sudo nano rc.local"


## Conexión eléctrica:

A continuación se muestra el esquema de conexión de los elementos.

No encontré el mismo modelo de la matriz led real, el modelo en el esquema tiene un pin extra que no habrá en el real.

En el esquema solo se muestra una matriz led debido a que las dos tienen las mismas conexiones.

![image](https://github.com/Alfnunfer/Avati-/assets/61046182/6d983c73-6066-48da-944a-8fb766632074)


## Estructura del proyecto:

El proyecto se divide en dos carpetas principales, la primera es la carpeta de Códigos, y la segunda es la carpeta con los modelos 3d, las diferentes versiones y los archivos stl de cada pieza por separado.
El código Main es el principal y es el que se encarga de llamar a las clases de los otros códigos.


## Mejoras Futuras:

Añadir la aplicación móvil que se conecte con el robot.

Modificar los modelos 3d para añadir huecos para cámara, altavoz, micrófono y led de estado.


## Créditos:

Programación, Modelado 3d, Montaje - Alfonso Núñez Ferreiro

Diseño, Asistente estético - Manuel Anxo Núñez Ferreiro

Proyecto propuesto por el departemento de e-learning del CESGA

Proyecto basado en el proyecto ABILITI:
https://abiliti.eu/resources/
