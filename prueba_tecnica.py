'''
Universidad Escuela Colombiana de Ingeniería
Diseño de Datos y Algoritmos (DDYA)
Profesor: Edward Francia
Estudiante: Herrera Puentes Juan Felipe
Lenguaje: Python
'''

#1. Determinar si un número es positivo, negativo o cero.

num = int(input("Ingrese un número entero: "))

def positivo_negativo(num):
    if num > 0:
        return "\nEl número ingresado es positivo"
    if num < 0:
        return "\nEl número ingresado es negativo"
    else:
        return "\nEl número ingresado es cero"


#2. Determinar si un número pertenece a la sucesión de Fibonacci.

def sucesion_fibonacci(num):
    primero = 0
    segundo = 1

    while segundo < num:
        siguiente = primero + segundo
        primero = segundo
        segundo = siguiente

    if num == 0 or num == segundo:
        print("\nEl número ingresado pertenece a la sucesión de Fibonacci")

    else:
        print("\nEl número ingresado NO pertenece a la sucesión de Fibonacci")

#3.Determinar si un número es primo.

def es_primo(num):

    if num <= 1:
        print("\nEl número no es primo")

    else:
        divisor = 2

        while divisor < num:
            if num % divisor == 0:
                print("\nEl número NO es primo")
            divisor = divisor +1
        print("\nEl número ES primo")


#4 y #5.Dos números y sumar los intermedios. Pero, si los dos números son negativos se multiplican los intermedios.

primer_numero = int(input("\nIngrese el primer número entero: "))
segundo_numero = int(input("Ingrese el segundo número entero: "))

def operar_intermedios(primer_numero, segundo_numero):

    if primer_numero < 0 and segundo numero < 0:
        multiplicacion = 1
        numero_actual = primer_numero + 1

        while numero_actual < segundo_numero:
            multiplicacion = multiplicacion * numero_actual
            numero_actual = numero_actual + 1

        print("\nLa multiplicación de los intermedios de",primer_numero, "y", segundo_numero, "es", multiplicacion)

        else:
            suma = 0
    numero_actual = primer_numero + 1

    while numero_actual < segundo_numero:
        suma = suma + numero_actual
        numero_actual = numero_actual + 1
    print("\nLa suma de los intermedios de",primer_numero, "y", segundo_numero, "es", suma)

operar_intermedios(primer_numero, segundo_numero)
        
#6. Si un número es impar se eleva al cuadrado y si es par al cubo.

num = float(input("\nIngrese un número entero: "))

def elevar_numero(num):
    if num % 2 == 0:
        print("\nEl número es par")
        print("Elevado al cubo es:", num ** 3)

    else:
        print("\nEl número es impar")
        print("Elevado al cuadrado es:", num ** 2)


print(positivo_negativo(num))
sucesion_fibonacci(num)
es_primo(num)
operar_intermedios(primer_numero, segundo_numero)
elevar_numero(num)

#7. Realizar el procedimiento con el código del estudiante.

codigo = int(input("\nIngrese el código del estudiante")
print(positivo_negativo(codigo))
sucesion_fibonacci(codigo)
es_primo(codigo)
elevar_numero(codigo)
#punto #4 y 5 no se pueden por que el código del estudiante es un solo número y se necesitan dos.

#Puntos #8, #9 y #10.
#Profesor Edward, no logré desarrollar completamente los puntos 8,9 y 10 porque, aunque intenté comprender la lógica del procedimiento, aún tengo dificultades para aplicar
#algunos conceptos de programación, me siento bloqueado completamente. Revisé el material de clase e intenté resolverlos, pero preferí no entregar una solución incorrecta o
#copiar algo que no entienda. Considero que todavía necesito reforzar estos temas para poderlos desarrollarlos de manera correcta y entender la lógica detrás de cada ejercicio.
#Espero su clase sea un espacio para comprender mejor y así no se me dificulte la materia. Gracias por la comprensión.
             ca
