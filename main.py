# name = input('what is your name?: ')
# age = int(input('How old are you? '))
#
# if age < 12:
#     print('Сенин жашын, кичине')
# elif age > 18:
#     print('Твой возраст подросток')
# else:
#     print('ты крутой')





#
# while True:
#     name = input('Как тебя зовут? (или введи стоп для выхода): ')
#     if name.lower() == 'stop':
#         print('Goodbye!')
#         break
#     print('Hi, ' + name + '!')



# count = 0
# while True:
#     name = input('как тебя зовут? (или веди стоп для выхода): ')
#
#     if name.lower() == 'stop':
#         print('Програма завершена всего приветствий' + str(count))
#         break
#     print('привет, ' + name + '!')
#     count +=1
#


# count = 0
# while True:
#     name = input('как тебя зовут? (стоп): ')
#     if name.lower() == 'stop':
#         print('Молодец ты смог: ' + str(count))
#         break
#     print('привет, ' + name + '!')
#     count += 1
#
#
# input('Кубанычева Лилия')
# print('Ynty')
#
#
# a = int(input(36 // 7))
# print(a)





import math
from turtle import *

def heart_a(k):
    return 15 * math.sin(k) ** 3

def heart_b(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)
speed(1000000)
bgcolor("black")

for i in range(6000):
    goto(heart_a(i) * 20, heart_b(i) * 20)

    for j in range(5):
        color("#f73487")
    goto(0, 0)

done()