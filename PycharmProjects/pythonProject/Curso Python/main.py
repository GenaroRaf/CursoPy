"""""
#Video 1
nombre = "Genaro Rafael"
edad = 21
student = True

print("Hello!")
print(f"My name is: {nombre}")
print(f"I have {edad} years old")

if student:
    print("\nYou are a student")
else:
    print("\nYou aren't a student")


#if student >= 18:
#    print("Yes")
#elif student < 0:
#    print("Maybe")
#else:
#print("No")

#Video 2
#Tipos

nombre = "Genaro"
apellido = ""
edad = 21
estatura = 1.71

print(type(apellido))

edad = float(edad)

print(f"\n\nEdad en decimal: {edad}")
print(f"String booleano: {bool(apellido)}")

estatura = str(estatura)

print(f"Estatura en str: {estatura+"1"}")

#Video 3

name = input("\n\nWhat´s your name?")
age = int(input("How old are you?"))

print(f"\nHello {name}")
print("Happy birthday!!")
print(f"You are {age} years old")

#Exercise 1
widht = float(input("\n\nWidht: "))
lenght = float(input("Lenght: "))

area = widht * lenght

input(f"The area is: {area}")
"""""
import random
import time

#Video 4
"""""
Funciones matematicas
    round() Redondear
    abs() Absoluto de un número
    pow(a,b) Potencias
    max(a,b,c,...z) El máximo de grupo de números
    min(a,b,c,...z) El entero de grupo de números
    
    Imports
    math
    
    Funciones
    math.pi PI
    math.e E (natural)
    math.sqrt Raiz
    math.ceil Redondear hacia arriba 9.1 = 10
    math.floor Redondear hacia abajo 9.999 = 9
"""""
""""
import math

#Exercise 2 Area and circuference

r = float(input("\n\n Digite el radio: "))

circunferecnia = 2 * math.pi * r
area = math.pi * math.pow(r,2)

print(f"\n\nLa circunferencia es: {circunferecnia}")
print(f"El area es: {round(area,2)}cm")

#Exercise 3 Hipotenusa

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

c = math.sqrt((pow(a,2)) + (pow(b,2)))

print(f"Side c: {c}")

"""""

"""""
#Excercise 4
operator = input("Enter an operator (- + * /): ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

if operator == "+":
    result = num1 + num2
    print(f"The result is: {round(result,3)}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is: {round(result,3)}")
elif operator == "*":
    result = num1 * num2
    print(f"The result is: {round(result,3)}")
elif operator == "/":
    result = num1 / num2
    print(f"The result is: {round(result,3)}")
else:
    print(f"{operator} is not a valid operator")
    
"""""


"""""
#Excercise 5

weight = float(input("Enter a weight: "))
unit = input("Kilograms or Pounts? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight,1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight,1)} {unit}")
else:
    print(f"{unit} is not a valid")
    
"""""


"""""
#Exercise 6

unit = input("Is this temperature is Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == ("C"):
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == ("F"):
    temp = round((temp -32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")


#Operación ternaria: x if condicion else y

edad = 18

print("Mayor de edad" if edad >= 18 else "Menor de edad")
result = "Par" if edad % 2 == 0 else "impar"

print(result)
"""""



"""""
#Exercise 7

Cadenas

len(name) Cuenta el numero de letrasd de la cadena
name.find("letra") Te dice la primera posición donde se encontró la coincidencia en la cadena
name.rfind("letra") Te dice la última posición donde se encontró la coincidencia en la cadena
name.capitalize() Convierte en mayuscula la primera letra de la cadena
name.upper() Convierte en mayusculas toda la cadena
name.lower() Convierte en minusculas toda la cadena
name.isdigit() Detecta si la cadena son puros digitos
name.isalpha() Detecta si la cadena son letras
phone_number.count("simbolo") sirve para contar las concidencias de una subcadena, esto incluye simbolos especificos
phone_number.replace("simbolo", "otro_simbolo") Sirve para replazar una subcadena por otro

name = "Genaro Rafael"

print(name.count("fael"))
"""""


"""""
#Exercise 8

#valiadte user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter a username: ")

input(not username.isalpha())

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
"""""


"""""
#Video 16

n = int(input("Digite un # entre 1 - 10: "))

while n < 1 or n > 10:
    print(f"{n} is not valid")
    n = int(input("Digite un # entre 1 - 10: "))

print(f"Your number is {n}")
"""""



"""""
#Video 17
p = 0
r = 0
t = 0


while p <= 0:
    p = float(input("\nDigite su balance: "))
    print(p)
    if p <= 0:
        print("Principle can't be less thanor equal to zero")

while true:
    r = float(input("\nDigite su porcentaje de interes: "))
    if r <= 0:
        print("Interest rate can't be less thanor equal to zero")
    else:
        break

while t <= 0:
    t = float(input("\nDigite el tiempo en años: "))
    if t <= 0:
        print("Time can't be less thanor equal to zero")

total = p * pow((1 + r / 100), t)
print(f"Balance despues {t} años/s: ${t:.2f}")
"""""


"""
#Ciclo for
credit_card = "1234-5678-9012-3456"

#Iteración normal
for i in range(1,11):
    print(i)

print("\nIteracion modificada: ")

#Iteración modificado
for i in range(0,11,2):
    print(i)

print("\nIteracion invertida: ")

#Iteración invertida
for i in reversed(range(1,11)):
    print(i)

print("\nIteracion da partir de una cadena: ")

#Iteración del contenido de una cadena
for i in credit_card:
    print(i)
"""


"""
import time

my_time = int(input("Digite el timepo en segudos: "))

for i in range(my_time,0,-1):
    segundos = i % 60
    minutos = int(i / 60) % 60
    horas = int(i / 3600)

    print(f"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)

print("El tiempo se detuvo")
"""


"""
#Bucles anidados

filas = int(input("Digite las filas: "))
columnas = int(input("Digite las columas: "))
simbolo = input("Digite el simbolo: ")

for i in range(filas):
    for j in range(columnas):
        if j != columnas-1:
            print(simbolo, end=" - ")
        else:
            print(simbolo, end="")
    print()
"""


"""
#   Listas = [] ordenadas y configurables. Puedes duplicar el contenido
#   Set = {} Desordenadas e inconfigurables, pero puedes añadir/eliminar (add/remove). No acepta valores duplicados
#   Tuple = Ordenadas e inconfigurables. Puedes duplicar contenido. Son más rápidas

fruits1 = ["apple", "orange", "banana", "coconut"]
fruits2 = {"apple", "orange", "banana", "coconut"}
fruits3 = ("apple", "orange", "banana", "coconut")

#Funciones globales
print(dir(fruits1)) #Te dice que funciones puedes realizar con esa colección
print(help(fruits2)) #Te describe a detalle las funciones que puedes utilizar en esa collección
print(len(fruits3)) #Te dice cuantos objetos tiene la colleción
print("pineapple" in fruits1) #Te dice si se encontro una coincidencia

#Funciones para tuple
print("Funciones para tuplas: \n")

print(fruits3.count("coconut"))


print("Lista: \n")
print(fruits3)

for fruit in fruits1:
    print(fruit)

#Funciones para set
print("Funciones para sets: \n")

print(fruits2.add("pineapple")) #Función para añadir elementos
print(fruits2.remove("apple")) #Remueve un elemento en especifico
fruits2.pop() #Elimina un elemento de la lista (no se sea aleatorio o es el último elemento)
fruits2.clear() #Elimina el contenido de la lista

print("Set: \n")
print(fruits2)

for fruit in fruits1:
    print(fruit)

#Funciones para list
fruits1[0] = "pineapple" #Igualar un elemento en una posición en especifico
fruits1.append("pineapple") #Agregar elementos a lista
fruits1.remove("orange") #Remueve el elemento dicho
fruits1.insert(0, "grade") #Inserta el elemento en la posición dicha 
fruits1.sort()
fruits1.reverse() #Invierte la lista
print(fruits1.index("grade")) #Te dice en que posición de la lista se encuentra el elemento
print(fruits1.count("orange")) #Realiza un conteo de las coincidencias

print("List: \n")
print(fruits1)

for fruit in fruits1:
    print(fruit)

fruits1.clear() #Elimina el contenido de la lista
"""


"""
foods = []
prices = []
total = 0
cont = 0

while True:
    food = input("Ingrese el alimento a comprar (q to quit): ")

    if food.lower() == "q":
        break
    else:
        cont += 1
        price = float(input(f"Ingrese el valor de {food}: $"))

        foods.append(food)
        prices.append(price)


print("---------Tu carta es----------")
print()
for i in range(0, cont):
    print(f"{foods[i]}:  ${prices[i]}")
    total += prices[i]

print(f"Tu total es: ${total}")
"""

"""
#Listas de listas (matrices :v)
fruits = ["apple", "orange", "banana", "coconut"]
vegetables  = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

for collection in groceries:
    for element in collection:
        print(element, end = " ")
    print

#Tupla de tuplas
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end =" ")
    print()
"""

"""
#Python quiz game
questions = ("¿Cuantos elementos tiene la tabla periodica?: ",
             "¿Cual es el animal que pone los huevos mas grandes?",
             "¿Cual es el gas mas abundante de la atmosfera de la Tierra?",
             "¿Cuantos huesos tiene el cuerpo humano?",
             "¿Cual es el planeta mas caliente del sistema solar?")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Ballena", "B. Cocodrilo", "C. Elefante", "D. Avestruz"),
           ("A. Nitrogeno", "B. Oxigeno" , "C. Dioxido de carbono", "D. Hidrogeno"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercurio", "B. Venus", "C. Tierra", "D. Marte"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
         print(option)


    guess = input("Ingrese (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correcto!")
    else:
        print("Incorrecto!")
        printe(f"la respuesta es: {answers[question_num]}")

    question_num += 1

print("------------------")
print("    Resultados    ")
print("------------------")

print("Respuestas: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()

print("Adivinadas: ", end = "")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(answers) * 100)
print(f"\nTu puntaje es: {score}%")
"""


"""
#Dictionary = una colección de pares {clave:valor} (key:value) ordenados y modificables. Sin duplicados
capitals = {"USA" : "Washington D.C",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Mosow"}

#print(dir(caqpitals)) #Te da todas las funciones que hay para los diccionarios
#print(help(capitals)) #Te describe a detalle cada función
#print(capitals.get("Japan")) # A partir de una llave se realiza una busqueda en el diccionario y se regresa su valor


#if capitals.get("Russia"):
#    print("That capítal exists")
#else:
#    print("That capital does not exist")

#capitals.update({"Germany" : "Berlin"})
#capitals.update({"USA" : "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()
#for key in capitals.keys():
#    print(key)

#values = capitals.values()
#for value in capitals.values():
#    print(value)

#items = capitals.items()
#for key, value in capitals.items():
#    print(f"{key}: {value}")
"""

"""
menu = {"pizza" : 3.00,
        "nachos" : 4.50,
        "palomitas" : 6.00,
        "papas fritas" : 2.50,
        "chips" : 1.00,
        "pretzel" : 3.50,
        "refresco" : 3.00,
        "limonada" : 4.25}

cart = []
total = 0

print("--------- MENU ----------")
for key, value in menu.items():
    print(f"{key:15}: ${value: .2f}")
print("---------------------")

while True:
    food = input("Seleccione un objeto (q para salir): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("\n-------- Tu orden ----------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print()
print(f"El total es: ${total:.2f}")
"""


"""
import random

low = 1
high = 100
options  = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.radiant(low, high)
# number = random.random()
option = random.choice(options)
#random.shuffle(cards)

print(option)
"""


"""
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_runnig = True

while is_runnig:

    guess = input("Ingrese su intento: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1;

        if(guess < lowest_num and guest > highest_num):
            print("Numero fuera de rango")
            print(f"Por favor ingrese un numero entre {lowest_num} y {highest_num}")
        elif guess < answer:
            print("¡Muy bajo! Intente con un numero mayor")
        elif guess > answer:
            print("¡Muy alto! Intente con un numero menor")
        else:
            print(f"Correcto! La respuesta era {answer}")
            print(f"Numero de intentos: {guesses}")
            is_runnig = False
    else:
        print("Numero invalido")
        print(f"Por favor ingrese un numero entre {lowest_num} y {highest_num}")
"""


"""
import random

options = ("piedra", "papel", "tijeras")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Ingrese su opcion (piedra, papel, tijeras): ").lower()

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        print()


        if player == "piedra" and computer == "tijeras":
            print("Player win")
        elif player == "papel" and computer == "piedra":
            print("Player win")
        elif player == "tijeras" and computer == "papel":
            print("Player win")
        elif player == computer:
            print("Empate")
        else:
            print("Computadora win")

        play_again = input("Jugar de nuevo? (s/n): ").lower()
        if not play_again == "s":
            running = False

print("\nGracias por jugar!")
"""

"""
import random
#● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
dice_art =  {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("Ingrese el numero de dados: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end = " ")
    print()
for die in dice:
    total += die
print(f"\ntotal: {total}")
"""


"""
#funciones

def hello(greeting, title, firts, last):
    print(f"{greeting} {title}{firts} {last}")

hello("Hello", "Mr.", "John", "James")
hello("Hello", "Mr.", last="John", firts="James")

#Parametros como listas o arreglos
def fruits(*args):
    for fruit in args:
        print(fruit, end=" ")

fruits("Orange", "apple", "banana")

#Parametros como diccionarios
print("\n")
def direccion(**kwargs):
    for values in kwargs.values():
        print(values)

    print()

    for key in kwargs.keys():
        print(key)

    print()

    for key, value in kwargs.items():
        print(f"{key}: {value}")


direccion(nombre="Selena",
          apartamento="512",
          coche="suru")
"""



"""
# Lista de comprensión: una concisa manera de crear una lista compacta en python y fácil de leer que los bucles tradicionales
# [expression for value in iterable if condition]

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)
"""


"""
#Match-case (switch)

def is_weekend(day):
    day = day.lower()
    
    match day:
        case "sunday" | "saturday":
            return True
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case _:
            return False


print(is_weekend("Sunday"))
"""


"""
#Modulos
import math #importación normal
from math import pi #importar algo especifico
import math as m #cambiar el nombre a mi librería
"""


"""
#Python Banking Program
def show_balance(balance):
    print("************************")
    print(f"Su balance es: {balance:.2f}")
    print("************************")

def deposit():
    print("************************")
    amount = float(input("Ingrese la cantidad a depositar: "))
    print("************************")

    if amount < 0:
        print("Este cantidad no es valida")
        return 0
    else:
        return amount

    return amount

def withdraw(balance):
    print("************************")
    amount  = float(input("Digite la cantidad a retirar: "))
    print("************************")

    if amount > balance:
        print("Este cantidad no es valida")
        return 0
    else:
        return amount




def main():
    balance = 0
    its_running = True

    while its_running:
        print("************************")
        print("   programa bancario    ")
        print("************************")

        print("1.Mostrar saldo")
        print("2.Depositar")
        print("3.Retiro")
        print("4.Salir")

        choice = int(input("Ingrese una opcion: "))

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)
            case 4:
                its_running = False
            case _:
                print("************************")
                print("Esta no es una opcion valida")
                print("************************")

        print("************************")
        print("Que tengas un excelente dia")
        print("************************")

        time.sleep(3)

if __name__ == '__main__':
   main()
"""


"""
# Python casino

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100
    cont =  0

    print("************************")
    print("Bienvenido al casino UwU")
    print("Simbolos: 🍒 🍉 🍋 🔔 ⭐")
    print("************************")

    while balance > 0:
        cont += 1
        print(f"Ronda {cont}")
        print(f"Saldo de cuenta: ${balance}")

        bet = input("Digite su apuesta: ")

        if not bet.isdigit():
            print("Porfavor digite un numero valido")
            continue

        bet =  int(bet)

        if bet > balance:
            print("Saldo insuficiente")
            continue

        if bet <= 0:
            print("La apuesta no puede ser igual o menor a 0")


        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        #payout = int(payout)

        if payout > 0:
            print(f"Tu ganas ${payout}")
        else:
            print("Lo sentimos perdiste la ronda")


        balance += payout

if __name__ == "__main__":
    main()
"""

"""
import random
import string

chars = ' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"Caracteres: {chars}")
print(f"Llave: {key}")

#Encrypt
plain_text = input("Ingrese el mensaje a encriptar: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"mensaje original: {plain_text}")
print(f"mensaje cifrado: {cipher_text}")
"""

# El ahorcado en Python
import random
import palabras

#words = ("manzana", "naranja", "platano", "coco", "piña")
words = palabras.words

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" ° ",
                   "   ",
                   "   "),
               2: (" ° ",
                   " | ",
                   "   "),
               3: (" ° ",
                   "/| ",
                   "   "),
               4: (" ° ",
                   "/|\\",
                   "   "),
               5: (" ° ",
                   "/|\\",
                   "/  "),
               6: (" ° ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(answer)

def main():
     answer = random.choice(words)
     hint = ["_"] * len(answer)
     wrong_guesses = 0
     guessed_letters = set()
     is_running = True

     while is_running:
         display_man(wrong_guesses)
         display_hint(hint)
         #display_answer(answer)
         guess = input("Ingrese una letra: ").lower()

         if len(guess) != 1 or not guess.isalpha():
             print("Entrada invalida")
             continue

         if guess in guessed_letters:
             print("La letra ya fue utilizada")
             continue

         guessed_letters.add(guess)

         if guess in answer:
             for i in range(len(answer)):
                 if(answer[i]) == guess:
                     hint[i] = guess
         else:
             wrong_guesses += 1


         if "_" not in hint:
             display_man(wrong_guesses)
             display_answer(answer)
             print("YOU WIN!")
             is_running = False
         elif wrong_guesses >= len(hangman_art) - 1:
             display_man(wrong_guesses)
             display_answer(answer)
             print("YOU LOSE!")
             is_running = False

if __name__ == "__main__":
    main()