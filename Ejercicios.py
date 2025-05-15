#🟢 Nivel Básico
# *****Saludo personalizado*****
# Crea una función que reciba un nombre y muestre un saludo personalizado.
# def name_person():
#     while True:
#         name = input("Enter your name: ").capitalize().strip()
#         name = str(name)
#         if len(name) == 0 or not name.replace(" ", "").isalpha() :
#             print("ERRO: Enter a name")
#             continue
#         print(f"Hello {name} is a pleasure to meet you")
#         return
# name_person()

# def person_name(name):
#     name = str(name).capitalize()
#     if len(name) == 0 or not name.replace(" ", "").isalpha():
#         print("ERROR")
#         exit()
#     print(f"Hello {name} is a pleasure to meet you")
# person_name("cristian")



#🟢 Nivel Básico
# *****Suma de dos números*****
# Escribe una función que reciba dos números y devuelva su suma.
# def sum_number(num1, num2):
#     return num1 + num2

# def validadate_number(str):
#     try: return int(str)
#     except ValueError: return -1

# flag_1 = False
# flag_2 = False

# while True:
#     if not flag_1:
#         num_1 = validadate_number(input("Enter a first number: "))
#         if num_1 < 0:
#             print("Enter a valid number")
#             continue
#         flag_1 = True

#     if not flag_2:
#         num_2 = validadate_number(input("Enter a second number: "))
#         if num_2 < 0:
#             print("Enter a valid number")
#             continue
#         flag_2 = True
#     print(f"The suma of number1 {num_1} + number2 {num_2} = {sum_number(num_1, num_2)}")
#     break

# def sum_num(num_1, num_2):
#     return num_1 + num_2
# total = sum_num(1, 3)
# print(total)



#🟢 Nivel Básico
# *****Número par o impar*****
# Crea una función que determine si un número es par o impar.
# def valid_int(str):
#     try:return int(str)
#     except ValueError: return -1

# is_pair = lambda num: num %2 == 0

# while True:
#     num = valid_int(input("Enter a number: "))
#     if num < 0:
#         print("ERROR")
#         continue
#     if is_pair(num):
#         print(f"Is pair {num}")
#     else:
#         print(f"Not is pair {num} ")


#🟢 Nivel Básico
# **Mayoría de edad**
# Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.
# def validadate_number(str):
#     try: return int(str)
#     except ValueError: return -1

# def adult():
#     while True:
#         age = input("Enter your age: ")
#         age = validadate_number(age)
#         if age == 0:
#             print("You are a newborn")
#             break
#         elif age > 0 and age < 12:
#             print("You are a child")
#             break
#         elif age >= 13 and age < 18:
#             print("You are a teenager")
#             break
#         elif age >= 18:
#             print("You are of legal age")
#             break
#         else:
#             print("Enter a valid number")
#             continue
# adult()


#🟢 Nivel Básico
# *****Conversor de temperatura*****
# Crea una función que convierta grados Celsius a Fahrenheit.
# def validate_float(num):
#     try: return float(num)
#     except ValueError: return -1

# def c_to_f():
#     celsius = validate_float(input("Enter the value in celsius grades: "))
#     if celsius <= 0:
#         print("ERROR")
#         return   
#     cels = (celsius * 9) / 5 + 32
#     print(f"The conversion from degrees Celsius ({celsius}) to Fahrenheit is = {cels}F°")
# c_to_f()



# *****Área de un triángulo*****
# Escribe una función que devuelva el área de un triángulo dado su base y altura.
# def validate_float(num):
#     try: return float(num)
#     except ValueError: return -1

# def base_x_height():
#     while True:
#         base = validate_float(input("Enter the base of the triangle: "))
#         if base <= 0:
#             print("ERROR")
#             continue
#         height = validate_float(input("Enter the height of the triangle: "))
#         if height <= 0:
#             print("ERROR")
#             continue
#         area = (base * height) / 2
#         print(f"The area of the triangle is = {area}")
# base_x_height()


#🟢 Nivel Básico
#*****Mayor de una lista*****
#Crea una función que reciba una lista de números y devuelva el mayor.
# def list_num(list_number):
#     number = list_number[0]
#     for i in list_number:
#         if i > number:
#             number = i
#     return number
# num_list = [9,7,4,8,1,11,15,6,20]
# print(list_num(num_list))


#🟢 Nivel Básico
# *****Contar letras*****
# Escribe una función que cuente cuántas veces aparece una letra en una palabra.
# def count_word(word, letter):
#     word = word.lower()
#     letter = letter.lower()
#     count = 0
#     for i in word:
#         if i == letter:
#             count += 1
#     return count
# result = count_word("Palabra", "a")
# print(f"Palabra tiene {result} (a)")





#🟡 Nivel Intermedio
# *****Filtrar pares*****
# Crea una función que reciba una lista de números y devuelva solo los pares.
# def pair_num(list_number):
#     number = []
#     for i in list_number:
#         if i %2 == 0:
#             number.append(i)
#     return number
# num_list = [1,2,3,4,5,6,7,8,9,10,12,13,14,11]
# result = pair_num(num_list)
# print(f"The numbers pairs {result}")


#🟡 Nivel Intermedio
#*****Palíndromo*****
# Escribe una función que determine si un texto es un palíndromo.
# def palindormo():
#     string = input("Enter a palindromo: ").lower()
#     if string == string[::-1]:
#         print(f"Is a palindromo {string}")
#     else:
#         print(f"not is a palindromo {string} = {string[::-1]}")
# palindormo()


#🟡 Nivel Intermedio
# *****Factorial*****
# Crea una función que calcule el factorial de un número entero positivo.
# def validate_int(str):
#     try: return int(str)
#     except ValueError: return -1

# def factorial():
#     while True:
#         num = validate_int(input("Enter a number: "))
#         if num < 0:
#             print("ERROR")
#             continue
#         factorial_number = 1
#         for i in range(1, num + 1):
#             factorial_number *= i
#         print(f"The number factorial of {num} = {factorial_number}")
# factorial() 


#🟡 Nivel Intermedio
# *****Eliminar duplicados*****
# Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.
# def list_ls():
#     while True:
#         list1 = input("Enter a comma-separated list: ").capitalize().strip().split(",")
#         if len(list1) == 0:
#             print("ERROR")
#             continue
#         new_list = []
#         for i in list1:
#             if i not in new_list:
#                 new_list.append(i)
#         print(f"The list without repeated numbers = {new_list}")
#         return
# list_ls()


#🟡 Nivel Intermedio
# *****FizzBuzz*****
# Crea una función que reciba un número y devuelva "Fizz"3, "Buzz"3 o "FizzBuzz"3-5 según las reglas del juego.
# def valid_num(str):
#     try: return int(str)
#     except ValueError: return -1
    
# def num_F_B_FB():
#     while True:
#         num = valid_num(input("Enter a number: "))
#         if num <= 0:
#             print("ERROR")
#             continue
#         if num %3 == 0 and num %5 == 0:
#             print(f"FizzBuzz: the number {num} is divisible by 3-5")
#             return
#         elif num %5 == 0:
#             print(f"Buzz: the number {num} is divisible by 5")
#             return
#         elif num %3 == 0:
#             print(f"Fizz: the number {num} is divisible by 3")
#             return
#         else:
#             print("is not divisible by 3-5")
#             continue            
# num_F_B_FB()
    

#🟡 Nivel Intermedio
# *****Contar vocales*****
# Escribe una función que reciba una cadena y devuelva la cantidad de vocales.
# def text_string():
#     while True:
#         string = input("Enter a word with its respective vowels: ").capitalize().strip()
#         letter = "a","e","i","o","u"
#         if len(string) == 0:
#             print("ERROR")
#             continue
#         count = 0
#         for i in string:
#             if i in letter:
#                 count += 1
#         print(f"hay {count} vowels")
#         return count   
# text_string()


#🟡 Nivel Intermedio
# Invertir texto
# Crea una función que invierta una cadena de texto.
# def string_text():
#     while True:
#         string = input("Enter a text: ").strip()
#         if len(string) == 0:
#             print("ERROR")
#             continue
#         print(f"The word {string} inverted is {string[::-1]}")
#         break
# string_text()


# 🔴 Nivel Avanzado
# Validar contraseña segura
# Escribe una función que valide si una contraseña cumple con requisitos de seguridad (mayúsculas, minúsculas, números y símbolos).
# def input_user():
#     return input("Enter a password: ")

# def valid_password(password):
#     characters = ",.-{}+()*[]¨´!#$\¡?!%&/" 
#     mayus = False
#     min = False
#     num = False
#     sim = False
#     for carac in password:
#         if carac.isupper():
#             mayus = True       
#         if carac.islower():
#             min = True
#         if carac.isdigit():
#             num = True
#         if carac in characters:
#             sim = True
#         if mayus and min and num and sim:
#             break
#     if mayus == True:
#         print("Has capital letters")
#     else:
#         print("Has no capital letters")
#     if min == True:
#         print("Has lowercase")
#     else:
#         print("Has no lowercase letters")    
#     if num == True:
#         print("It has numbers")
#     else:
#         print("It doesn't have numbers") 
#     if sim == True:
#         print("Has symbols")
#     else:
#         print("Has no symbols") 
#     return mayus and min and num and sim  
# result = valid_password(input_user())


# 🔴 Nivel Avanzado
# Simular dado
# Crea una función que simule el lanzamiento de un dado de 6 caras.
# import random

# def dado():
#     dice = random.randint(1, 6, 4)
#     return dice
# print(dado())