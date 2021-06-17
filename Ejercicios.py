# menores = []
# mayores = []
#
# while True:
#     nombre = input("Nombre: ")
#     if nombre == "":
#         break
#     edad = input("Edad: ")
#     if str(edad) == "":
#         break
#     if int(edad) >= 18:
#         mayores.append(nombre)
#     elif int(edad) <= 17:
#         menores.append(nombre)
#
# print("mayores: " + str(mayores))
# print("menores: " + str(menores))



# lista_rango = [*range(1, 10)]
# lista_desorden = [2, 3, 4, 7, 8, 6, 1, 9]
# lista_negativa = [-1, -3]
#
# # for i in range(1, 10):
# #     if i not in lista_desorden:
# #         print(str(i) + " is missing")
#
#
# def funcion(x):
#     for i in range(min(x), max(x)):
#         if i not in x:
#             print(str(i) + " is missing")
#
# funcion(lista_negativa)
#
#
# # print(min(1, 2, 3, 4, 5, 6, 7))

# 10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.
# Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#
# ****
# *********
# *******

lista_histograma = [18, 37, 66, 48, 87, 55, 27]

def histograma(x):
    for i in x:
        print("*" * i)


# 9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(n, l):
    print(n * l)

# 8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común
# o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

lista1 = [1, 5, 4, 7, 9, 10]
lista2 = [3, 5, 6, 8, 11, 1]

def superposicion(x, y):
    for i in x:
        if i in y:
            print("True")
            return True


# 7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto
# escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(x):
    word = x
    if word == word[::-1]:
        print(word[::-1] + " es palindromo")
    else: print("no es palindromo")

# 6- Definir una función inversa() que calcule la inversión de una cadena.
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(x):
    return x[::-1]

# 5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los
# números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
#

def sum(x):
    resultado = 0
    for i in x:
        resultado += i
    return resultado

def multip(x):
    resultado = 1
    for i in x:
        resultado *= i
    return resultado


# 4- Escribir una función que tome un carácter y devuelva True
# si es una vocal, de lo contrario devuelve False.

def vowel_check(x):
    list_vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if x in list_vowel:
        print("True")
        return True
    else:
        print("False")
        return False

# 3- Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
# tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def len_check(x):
    len = 0
    for i in x:
        len += 1
    print(len)
    return len


# 2- Definir una función max_de_tres(), que tome tres números como
# argumentos y devuelva el mayor de ellos.

def max_de_tres(x, y, z):
    if x > y and x > z:
        print(x)
        return x
    elif y > x and y > z:
        print(y)
        return y
    elif z > x and z > y:
        print(z)
        return z


# 1- Definir una función max() que tome como argumento dos números
# y devuelva el mayor de ellos.


def maxmine(x, y):
    if x > y:
        print(x)
        return x
    elif x < y:
        print(y)
        return y









