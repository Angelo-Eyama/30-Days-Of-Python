#Dia 2:30 de Aprender Python - Variables
'''
    En python, el estandar para nombrar variables es el snake_case,
    es decir, separar las palabras usando guiones bajos y debe estar en minúsculas.

    No es obligatorio nombrarlo así, pero es mejor para adaptarse a otros códigos
'''

### Ejercicios Nivel 1 ###
first_name = "Angelo"
last_name = "Eyama"
full_name = "Angelo Eyama"
country = "Equatorial Guinea"
city = "Malabo"
age = 22
year = 2024
is_married = False
is_true = True
is_light_on = False

'''
Las variables de una linea es una declaración e inicalización de varias variables 
en una sola linea de código
Las variables que se crean pueden ser de distintos tipos
'''
uno, dos, tres, cuatro = 1, 2, 3, "cuatro"
#En este caso se asignan en orden: uno = 1, dos = 2, tres = 3, cuatro = "cuatro"

# DUDA: ¿En python se pueden crear variables sin darles un valor inicial?
# Respuesta: No, en python no se pueden crear variables sin asignarles un valor inicial


### Ejercicios Nivel 2 ###
'''
    type() es una función que devuelve el tipo de dato del objeto que recibe como argumento.
    Lo devuelve pero NO LO IMPRIME, es necesario ponerlo en un print para que se vea
'''
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

'''
    La función len() devuelve la longitud de una cadena, un array o una lista
'''
print()#Esto es un salto de linea (también podemos usar \n)
print( "Length first name:",len(first_name) )
print( "Length last name:",len(last_name))
print()

num_one = 5
num_two = 4
total = num_one + num_two               # 5 + 4
diff = num_one - num_two                # 5 - 4
product = num_one * num_two             # 5 * 4
division = num_one / num_two            # 5 / 4
remainder = num_two % num_one           # 4 mod 5
exp = num_one ** num_two                # 5 ^ 4
floor_division = num_one // num_two     # 5 / 4 (devuelve solo la parte entera)

print(num_one, "+", num_two, "=", total)
print(num_one, "-", num_two, "=", diff)
print(num_one, "*", num_two, "=", product)
print(num_one, "/", num_two, "=", division)
print(num_two, "mod", num_one, "=", remainder)
print(num_one, "^", num_two, "=", exp)
print(num_one, "//", num_two, "=", floor_division)
print()

radius = 30
pi = 3.141592

#La fórmula del área de un círculo es A = pi * (radio^2)
area_of_circle = pi * radius**2

#La formula para la circunferencia (o perímetro) de un círculo es P = pi * 2r
circum_of_circle = pi * (2 * radius)
print("Area de un circulo de", radius, "metros =", area_of_circle)
print("Perimetro de un circulo de", radius, "metros =", circum_of_circle)

'''
    Ahora, hacemos lo mismo pero con los datos que introduce el usuario
    La salida normal de input() es un string, lo convertimos a numérico con float
    para poder operar con ese dato despues
'''
radius = float(input("Introduzca el valor del radio: "))
#Recalculamos los valores del circulo con el nuevo radio
area_of_circle = pi * radius**2
circum_of_circle = pi * (2 * radius)
print("Area de un circulo de", radius, "metros =", area_of_circle)
print("Perimetro de un circulo de", radius, "metros =", circum_of_circle)

## Final del ejercicio ##
#   Solicitar por teclado los nombres y la edad
first_name = input("Introduzca su primer nombre: ")
last_name = input("Introduzca el segundo nombre: ")
age = int(input("Introduzca la edad: "))
