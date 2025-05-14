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