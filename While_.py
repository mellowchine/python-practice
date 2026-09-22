# """while"""

import math

# i=0
# while i<10:
#     i+=1
#     if i==7:
#         continue #прерывает итерацию
#     print(i, end=' ')

# i=0
# while i<10:
#     i+=1
#     if i== 7:
#         break #прерывает цикл
#     print(i, end=' ')
#
# else: #только с break
#     print('\nGoodbye')


# symbols = input('>').upper()
# while symbols != 'END':
#     print(symbols, end=' ')
#     symbols = input('>').upper()

# n = int(input('>'))
# sm = 0
# cnt = 0
# while n!=-1000:
#     sm += n
#     cnt += 1
#     print(n, end=' ')
#     n = int(input('>>'))
# # print('Средняя температура за период:"', round(sm/cnt, 2),'"',sep='') #печатается 1 ноль после запятой
# print(f'Средняя температура за период:"{sm/cnt:.2f}"') #строка формата - печатается 2 ноля после запятой

# """
# 35 100
# 71 cm
# """
# n=71
# n1=33
# n2=42
# print(35, 100, '\n' + str(n), 'cm')
# print(type(n))
# print(f'{n1} {n2} \n{n} cm')

"""
123
Посчитать количество и сумму цифр в числе 123
"""
"""
n=123

sm=123 % 10 = 3
    //10 = 12 % 10 = 2
                    //10 = 1 % 10 = 1
                             //10 = 0
"""
#считаем цифры и сумму цифр
# n = int(input('> '))
# nn = n
# sm = 0
# cnt = 0
# while n > 0:
#     remince = n % 10 Получаем последнюю цифру числа
#     sm+=remince прибавляем полученную цифру в sm
#     cnt+=1 увеличиваем счетчик на 1
#     n = n // 10
# print(f'В числе {nn} {cnt} ц. суммой {sm}.')

#если есть возможность не менять типы данных, то не нужно их менять!
#с цифрами быстрее, чем со строками
#
# n = int(input('> ')) #123
# res = 0
# while n > 0:
#     remince = n % 10 #3->2->1 #получаем последнюю цифру
#     res = res * 10 + remince #3->30+2->320+1 #
#     n//=10 #12->1->0. #получаем целую часть числа после отделения последней цифры
# print(res)
# += → сложить и присвоить
#
# -= → вычесть и присвоить
#
# *= → умножить и присвоить
#
# /= → разделить (получить float) и присвоить
#
# //= → разделить нацело и присвоить (int)

"""Наибольший общий делитель НОД
36 24 -> 36 - 24 = 12
12 24 -> 24 - 12 = 12
12 12 -> 12 = 12 -> NOD
"""
#
# n1 = int(input('>'))
# n2 = int(input('>>'))
#
# while n1 != n2:
#     if n1 > n2:
#         n1 -= n2
#     else:
#         n2 -= n1
# print(f'NOD={n1}')


# n1 = int(input('>'))
# n2 = int(input('>>'))
# print(f'NOD = {math.gcd(n1,n2)}')
# while n1 != n2:
#     if n1 > n2:
#         n1 -= n2
#     else:
#         n2 -= n1
# print(f'NOD={n1}')


# for n in range(1,100):
# #модуль валидации
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n, end=' ')

# while True:
#     n = input('> ')
#     n1 = input('>> ')
#     if n.isnumeric() and n1.isnumeric(): #numeric – работает и с арабскими символами
#         n = int(n)
#         n1 = int(n1)
#     res = n + n1
#     print(f'{'Слово' if isinstance(res,str) else "Сумма равна"} {res}')
#     if res == 'stop':
#             break
while True:
    time = 'Может быть временем суток' if 0<= (n:= int(input('>')))<=24 else 'Не может быть временем суток'
    print(time)
    if n < 0:
        break