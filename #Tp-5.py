#Tp-5
#1. Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior (3)
"""def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)"""

#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado.

"""def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)

from redondeo.redondeo import redondear

def suma_decimales(num1, num2):
    resultado = num1 + num2
    return redondear(resultado)"""

#3. Usando el módulo datetime, escribe un programa que muestre la fecha
#y hora actuales del sistema

"""import datetime

# obtener la fecha y hora actual del sistema
fecha_hora_actual = datetime.datetime.now()

# imprimir la fecha y hora actual formateada
print("La fecha y hora actual del sistema son: {}".format(fecha_hora_actual))"""

#4. Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito).

"""import random

while True:
    num = random.randrange(2, 11, 2)
    print(num)"""

#5 Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#para la adivinación o para buscar consejo.
"""import random

def magic_8_ball():
    #posibles respuestas
    respuestas = ["Es seguro que sí",
                  "Las chances son buenas",
                  "Puedes contar con ello",
                  "Pregúntame de nuevo más tarde",
                  "Concéntrate y pregunta de nuevo",
                  "No veo con claridad, intenta de nuevo",
                  "Mi respuesta es no",
                  "Mis fuentes me dicen que no"]
    # Devolver una respuesta al azar
    return random.choice(respuestas)"""

#6. Encuentre el tiempo de ejecución de los programas de los ejercicios
#anteriores (pista: use el módulo time)

"""import time

def EmpezarcontarTiempo():
    InicioDelPrograma=time.time()
    return InicioDelPrograma
def TiempoEmpleado(InicioDelPrograma):
     FinDelPrograma=time.time()
     TiempoEmpleado=FinDelPrograma-InicioDelPrograma
     return TiempoEmpleado"""