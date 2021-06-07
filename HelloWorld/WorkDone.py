# name = 'John Smith'
# age = 20
# is_new = True
#
# if(age == 20 & is_new):
#     print(name + 'is '+ age + ' years old')
# else:print('Is old')

#weight = float(input('what\'s your weight in pounds: '))
# pounds_to_kilograms = weight * 0.453592
# print(pounds_to_kilograms)

#
# temperature = 2
# name = "Kgomotso" * 7
#
# if len(name) <3:
#     print('Name must be at least 3 characters')
# elif len(name) < 50:
#     print('Name Looks good')
# else:
#     print('Name is too long')
#     print(name + f'= {len(name)}')

#=================First task=================
# input_weight = int(input('Weight: '))
# weight_type = input('(L)bs or (K)g: ')
#
# if weight_type.upper() == "K":
#     weight_lbs = input_weight * 2.205
#     print(f'You are {weight_lbs} pounds')
# elif weight_type.upper() == "L":
#     weight_kg = float(input_weight) * 0.454
#     print(f'You are {weight_kg} kg')
# else:
#     print('You chose the wrong weight type')
#print(input_weight)


# #==============Corrections==================
# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f'You are {converted} pounds')


#LOOOP

# i = 1;
# while i<=5:
#     print('*' * i)
#     i = i + 1
# print("Done")

# #===========GUESSING GAME=============

# secret_number = 4
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won')
#         break
# else:
#     print('Sorry, you failed')


## ===========Car APP==========
# help = input('>')
# count = 0
# if help.upper() == 'HELP':
#     print('start - to start the car')
#     print('stop - to stop the car')
#     print('quit - to exit')
#     while True:
#         input_opt = input('>')
#         if input_opt.upper() == "START":
#             print('The car started... Ready to go')
#             break
#         elif input_opt.upper() == "STOP":
#             print('The car is stopping')
#             break
#         elif input_opt.upper() == "QUIT":
#             print('Exit')
#             break
#         else:
#             print('I don\'t understand')
# else:
#     print('I don\'t understand')

# =========CORRECTIONS==============

# started = False
#
# while True:
#     command = input('> ').lower()
#     if command == 'start':
#         if started:
#             print('Started already')
#         else:
#             print('get started... Ready to go')
#             started = True
#     elif command == 'stop':
#         if started:
#             print('car stopped')
#             started = False
#         else:
#             print('car already stopped')
#     elif command == 'help':
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#             ''')
#     elif command == quit:
#         print('Exiting')
#         break
#     else:
#         print("I don't understand")
#
#

## ===============F shape===========

# iteration = []
# for shape in range(2):
#     print('XXXXX')
#     iteration.append(shape)
#     for line in iteration:
#         print('XX')


# =================for loop ===============
# for item in ['Kgomotso', 'Masondo', 'Lomachenko']:
#     print(item)
#
# for item in range(5,10):
#     print(item)
#
# for item in range(2, 15, 3):
#     print(item)
#
#
# for x in range(3):
#     for y in range(3):
#         print(f"({x}, {y})")

# numbers = [5, 2, 5, 2, 2]

# for number in numbers:
#     print(number * "*")
#
# for number in numbers:
#     output = ''
#     for count in range(number):
#         output += '*'
#     print(output)


# # ==============GET MAXIMUM NUMBER ============

# numbers = [2, 13, 18, 4, 12, 15, 10]
# max = 0
#
# for number1 in numbers:
#     if number1 > max:
#         max = number1
# print(max)

# # ========Lists===========
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [5, 2, 1, 5, 7, 4]
# numbers.append(15)
# print(numbers)
# numbers.copy()
# print(numbers)

# numbers.sort()
# numbers.reverse  ()
# print(numbers)
# print(numbers.count(5))
# print(numbers)
# numbers.remove(2)
# print(numbers)
# print(5 in numbers)
# print(numbers.index(5))
# print(numbers.clear())
# print(numbers )


#  Write program that removes duplicates
#
# numbers = [1 , 2, 2, 3, 3, 4, 5, 8, 8, 9, 1, 2, 3, 2, 10, 8]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# # tuples they are immutable

# numbers = (1, 2, 3)
#
#
# x = numbers[0]
# y = numbers[1]
# z = numbers[2]

# OR

# x, y, z = numbers

# print(y)


# # =========Dictionaries=========
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# customer["birthdate"] = "Jan 1 1980"
# # print(customer['s'])
#
# print(customer.get("birthdate"))

# phone = input('Phone: ')
# digits_mapping = {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four"
# }
#
# output = ""
#
# for char in phone:
#     output += digits_mapping.get(char, "!") + " "
# print(output)


# #==========Dictionary Program with Mosh===========NEED PRACTISE=====
# message = input(">")
# words = message.split(' ')
#
# emojis = {
#     ":)": "😁",
#     ":(": "😞"
# }
# output = ""
#
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)


# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')
#
#
# print('Start...')
# greet_user('Kgomotso', 'Masondo')
# print('Finish...')
#


#  # =======Functions keyword argument======
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')
#
#
# print('Start...')
# greet_user(last_name='Masondo', first_name='Kgomotso')
# print('Finish...')

# # ==========Function That Returns a Value======
# def square(number):
#     return number * number
#
#
# number = int(input('Square number: '))
# print(square(number))


# ======Emoji Converter in a function===========

# def emoji_converter(message):
#     words = message.split(' ')
#     dict = {
#         ':)': "😃",
#         ':(': "😞"
#     }
#     output = ""
#     for word in words:
#         output += dict.get(word, word) + ' '
#     return output
#
#
# message = input('> ')
# print(emoji_converter(message))



# ======Exceptions======
# try:
#     age = int(input('Age: '))
#     total = 500/age
#     print(total)
# except ZeroDivisionError:
#     print('Can\'t divide a number by 0')
# except ValueError:
#     print('Invalid value')

#===========Class===========

# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# point1.z = 30
#
# print(f'{point1.x} {point1.y} {point1.z}')
# point1.draw()

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw ")
#
#
# point = Point(10, 20)
# print(point.x)
# point.draw()

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
#
# person = Person("Kgomotso")
#
# print(person.name)
# person.talk()
#
# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Human:
#     def speaking(self):
#         print('I said Hello')
#
#
# class Dog(Mammal):
#     def bark(self):
#         print('Barking..')
#
#
# class Cat(Mammal, Human):
#     def meouw(self):
#         print("Meouw")
#
#
# cat1 = Cat()
# cat1.walk()
# cat1.meouw()
# cat1.speaking()
#
# dog1 = Dog()
# dog1.bark()

##=========================PACKAGES AND IMPORT=====================

# import converters
# from converters import lbs_to_kg
#
# def lbs_to_kg(weight):
#     return weight
#
#
# weight = int(input('enter you weight in KG: '))
# print(converters.kg_to_lbs(69))
# print(lbs_to_kg(156))

#from utils import find_max

# =========FIND MAX VALUE=========
# from utils import find_max
#
# numbers = [2, 13, 18, 4, 12, 15, 10]
# print(find_max(numbers))


#from ecommerce.shipping import *
#import ecommerce.shipping

#ecommerce.shipping.calc_shipping()

#calc_shipping()
#cal_arrived()
#cal_deliver()






