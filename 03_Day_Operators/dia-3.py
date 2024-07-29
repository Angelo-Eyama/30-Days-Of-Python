#Dia 3:30 Aprendiendo Python - Operadores

'''
    En python tenemos los siguientes operadores básicos:
    Addition(+): a + b
    Subtraction(-): a - b
    Multiplication(*): a * b
    Division(/): a / b
    Modulus(%): a % b
    Floor division(//): a // b
    Exponentiation(**): a ** b

    También tenemos operaciones con números complejos:
    (1 + 1j)*(1 - 1j)

    Voy a obviar los operadores aritméticos porque están en el documento anterior
'''

#Operadores de comparación (devuelven True o False según la condicion)
print(3 > 2)     # True, porque 3 es mayor que 2
print(3 >= 2)    # True, porque 3 mayor que 2
print(3 < 2)     # False, porque 2 es menor que 3
print(2 < 3)     # True, porque 2 es menor que 3
print(2 <= 3)    # True, porque 2 es menor que 3
print(3 == 2)    # False, porque 3 no es igual a 3
print(3 != 2)    # True, porque es 3 es distinto de 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('huevo') != len('carne'))    # False
print(len('casa') == len('cama'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

'''
    Otros comparadores de python son los siguientes:
        a = [1,2,3,4]
        b = a
        c = [1,2,3,4]

    is -> Devuelve true si ambas variables/valores apuntan al mismo valor/objeto
        print(a is b) -> True, porque apuntan al mismo sitio
        print(a is c) -> False, porque pese a ser iguales en contenido, están guardados en diferentes espacios de la memoria
        
    is not -> Devuelve True si las variables apuntan a objetos o espacios de memoria distintos
        print(a is not b) -> False, porque apuntan al mismo sitio
        print(a is not c) -> True, porque 'a' y 'c' apuntan a lugares distintos

    in -> Devuelve True si el elemento x pertenece a la lista y
        print(3 in a) -> True
        print("Hola" in "Hola mundo") -> True

    not in -> Devuelve True si el elemento x no pertenece a la lista y
        print(3 not in a) -> False
        print("Bye" not in "Hola mundo") -> True
'''

#También están los operadores lógicos (and, or, not)
print(3 > 2 and 4 > 3)     # True
print(3 > 2 and 4 < 3)     # False
print(3 < 2 and 4 < 3)     # False
print(3 > 2 or 4 < 3)      # True
print(not True)            # False
print(not not False)       # False

print()

### EJERCICIOS - DIA 3 ###
age = 22
height = 1.75
complejo = (5 - 3j)

#Solicita base y altura para calcular area de un triangulo (a = 0.5 * b * h)
base = float(input("Introduzca el valor de la base: "))
height = float(input("Introduzca la altura del triangulo: "))
area = 0.5 * base * height
print("El area del triangulo es", area, "\n")

#Solicita lado a, b y c para calcular el perímetro (suma de lados)
a = input("Valor del lado a: ")
b = input("Valor del lado b: ")
c = input("Valor del lado c: ")
perimeter = a + b + c
print("El perimetro del triangulo es", perimeter, "\n")

#Solicita el alto y el ancho de un rectángulo e imprime su area y perimetro
length = float(input("Introduzca la longitud rectangulo: "))
width = float(input("Introduzca el ancho del rectangulo: "))
area = length * width
perimeter = 2 * (length + width)
print("El area es", area, "y el perimetro es", perimeter, "\n")


x = -3
equation = x**2 + 6*x + 9
print(equation) # Imprime 0

print(len("python") is not len("dragon")) #False (negación de un True)
print( ("on" in "Python") and ("on" in "dragon") ) #True

#Convertir un entero a decimal y despues a cadena
entero = len("Python for begginners") #int
entero = float(entero) #float
entero = str(entero) #str
print(type(entero)) #Return str

#Verificar si un numero es par o impar
x = 7
if(x % 2 == 0):
    print(True) #par
else:
    print(False) #impar

#Ya me dio pereza hacer el resto de ejercicios
