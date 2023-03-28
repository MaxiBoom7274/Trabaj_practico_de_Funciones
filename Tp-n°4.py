#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
#ingresado por parámetro.

"""def es_primo(numero):
    
    #Funcion que determina si un numero es primo o no.
    
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos(n):
    
    #Funcion que muestra todos los numeros primos entre 1 y n.
    
    primos = []
    for numero in range(1, n + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

n = 20
print(numeros_primos(n))"""


#2)Escriba una función que le pida al usuario ingresar condimentos para un sandwich, hasta
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
#avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
#programa de acuerdo a estos criterios

"""def hacer_sandwich():
    while True:
        condimento = input("Ingrese un condimento para el sandwich (ingrese 'salir' para terminar): ")
        if condimento == "salir":
            break
        print(condimento + " ha sido agregado al sandwich.")
    print("El sandwich esta listo!")

hacer_sandwich()"""

#3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
#escribiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
#usando argumentos por posicion. Llámela una segunda vez usando argumentos por clave. 

"""def hacer_remera(tamaño, mensaje):
    print(f"Haciendo una remera de tamaño {tamaño} con el mensaje: {mensaje}")"""

#B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
#valores por defecto, y la segunda con valores diferentes.
"""def hacer_remera(mensaje='Me gusta Python', tamaño='L'):
    print("Haciendo una remera de tamaño " + tamaño + " con el mensaje '" + mensaje + "' impreso en ella.")

# Haciendo una remera con valores por defecto
hacer_remera()

# Haciendo otra remera con valores diferentes
hacer_remera(mensaje='Hola mundo', tamaño='M')"""


#4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …). 

"""def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result"""
