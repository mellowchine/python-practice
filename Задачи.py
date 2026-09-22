"""Играем в программистов
Семинар"""
import random
from datetime import *

from itertools import count
from unittest import result
from zoneinfo import available_timezones
import tkinter as tk

from tkinter import *
from tkinter import messagebox
from tkinter import END

# from строки import res

# Задача 1
# a= 'I like python, it is very useful for data analysis'
# b= 'python is the best tool for dealing with big data'
# выписать вторую строку без слов в первой строке

# a = 'I like python, it is very useful for data analysis'
# b = 'python is the best tool for dealing with big data'
#
#
# a=a.replace(',','')
# a = a.split() # разбить по пробелам
# b = b.split()
#
# c = []
# for word in b:
#     if word not in a:
#         c.append(word)
# # res = [word for word in b if word not in a]
#
# print(' '.join(c))
# print(' '.join([word for word in b if word not in a]))

# разбираем list comprehension
# res = random.sample(range(1000000), k=1000000)
# res.insert(0,0)
# for n, i in enumerate(res, 1):
#     print(n, i)
#     if i == 0:
#         break



# # Задача 2
# mytuple1 = (1, 1, 2)
# mytuple2 = (2, 4)
# tpl_tuple = (mytuple1, mytuple2)
# mylist2 = modify_lastelement (tpL_tuple, 5)
# ( (1,1,5), (2, 5))

# Задача 3
# Ввести оценки каждого студента за семестр по одной дисциплине в формате
# name 4 3 4 5 4 3 4 .
# В консоль вывести ведомость имя ср. балл отсортированную по имени и вторую отсортированную по среднему баллу.

# n = int(input('Number of students: '))
# data = []
# for i in range(n):
#     name, *marks = input('Form: name 3 4 5 2: ').split()
#     print(marks)
#     marks = [int(mark) for mark in marks]
#     print(marks)
#     mean = sum(marks) / len(marks)
#     data.append((name, mean))
#     print(data)
# Более удобный вариант
# n = int(input('Number of students: '))
# data = {}
# for i in range(n):
#     name, *marks = input('Form: name 3 4 5 2: ').split()
#     print(marks)
#     marks = [int(mark) for mark in marks]
#     print(marks)
#     mean = sum(marks) / len(marks)
#     data[name] = round(mean, 2)
# print(data)

# Задача 4
# Дана строка: "Иванов Исан Иванович, email: ivanov_ii@example.com, тел:
# +7(912)345-67-89, абрес: ул. Ленина, дом 15, кв. 200"

# Получить фамилию и инициалы.
# Из строки с электронной почтой выделить имя пользователя и домен.
# Извлечь телефон и адрес.
# • Вывести информацию в виде:
# Пользователь: Фамилия инициалы
# Email: домен: имя:
# Tel:
# Адрес проживания:

# st = ('Иванов Петр Иванович, email: ivanov_ii@example.com, тел: +7(912)345-67-89, адрес: ул. Ленина, дом 15, кв. 200')
# fio = st.split(', ')[0]
# surname = fio.split(' ')[0]
# name = fio.split(' ')[1][0]
# patronymic = fio.split(' ')[2][0]
#
# mail= st.split(', ')[1]
# domen = mail.split('@')[1].strip()
# email = mail.split('@')[0]
# username = email.split(' ')[1]
#
# phone = st.split(', ')[2]
# tel = phone.split(' ')[1]
#
# adress = st.split('адрес')[1]
#
# print(st.split(', '))
# print('Пользователь: ', surname, name, patronymic)
# print('Email:', 'Домен: ', domen, 'Имя: ', username)
# print('Tel:', tel)
# print('Адрес проживания:', adress)
#
# print(f'Пользователь: {surname} {name} {patronymic} \nEmail: Домен: {domen} Имя: {username} \nTel: {tel}) \nАдрес проживания: {adress}')
#
# Задача 5
# Дан список: numbers = [12, 7, 18, 5, 9, 14, 21, 8, 30, 11, 4, 15]
# 1. Выведите каждый второй элемент списка (начиная с первого).
# 2. Выведите список в обратном порядке без использования метода reverse ()
# (используйте срезы).
# 3. Удалите из списка все элементы, которые делятся на 3 без остатка.

# num = [12, 7, 18, 5, 9, 14, 21, 8, 30, 11, 4, 15]
#
# print(num[::2])
# print(num[::-1])
#
# result = []
# for x in num:
#     if x % 3 == 0:
#         result.append(x)
# print(result)

# Задача 5: Написать команды
# list = [100, 212, 3, 4, 5]
# # Исходный список:
# # print(list)
# # Количество элементов:
# print(len(list))
# # Четные числа:
# odd_numbers = [x for x in list if x % 2 == 0]
# print(odd_numbers)
# # Нечетные числа:
# not_odd_numbers = [x for x in list if x % 2 != 0]
# print(not_odd_numbers)
# # Максимальное значение:
# print(max(list))
# # Минимальное значение:
# print(min(list))
# # Среднее значение:
# print(round(sum(list)/len(list),2))
# # Отсортированный список:
# # list.sort() # метод привязан к структуре (для строки нет такого метода)
# print(list) # тот же отсортированный список
# print(sorted(list)) # функция, создает новый список
# # Список наоборот:
# print(list[::-1])

# Задача 6: поиск и модификация кортежа
# fruits = ('apple', 'banana', 'orange', 'pear', 'banana','mango', 'banana')
# print(fruits.index('banana'))
# print(fruits.count('banana'))
# print(fruits[::2])

# new_fruits = ()
# for i in fruits:
#     new_fruits = new_fruits + (i,)
#     print(new_fruits)

# новый кортеж, в котором все элементы дублируются
# new_fruits = ()
# for i in fruits:
#     new_fruits += (i, i)
# print(new_fruits)

# # Задача 7: операция со множествами
# # Даны два множества:
# set1 = {2, 4, 6, 8, 10, 12}
# set2 = {6, 8, 10, 14, 16, 18}
# # 1. Найдите пересечение множеств.
# set3 = set1 & set2
# print(set3)
# # 2. Найдите объединение множеств.
# set3 = set1 | set2
# print(set3)
# # 3. Удалите из set1 все элементы, которые есть в set2
# set3=set1.difference(set2)
# print(set3)
# # 4. Проверьте, является ли set1 ПОдМНОЖеСТВОм set2.
# print(set1.issubset(set2))

# # Задача 8:
# # Дан словарь:
# d = {'Иван': [5, 4, 5], 'Петр': [3, 4, 4], 'Мария': [5, 5, 4], 'Ольга': [4, 5, 5]}
# # 1. Добавьте в словарь нового студента "Анна" с оценками 5, 5, 5
# d['Анна'] = [5, 5, 5]
# print(d)
# # 2. Удалите студента "Петр".
# print(d.pop('Петр')) # del d['Петр']
# print(d)
# # 3. Выведите средний балл для каждого студента (используйте цикл по ключам и значениям).
# for k, v in d.items():
#     v = round(sum(v)/len(v), 2)
#     print(k, v)

# # Задача 9: Угадай число с подсказками
# # Напишите программу, которая:
# # 1. Загадывает случайное число от 1 до 100 (используйте random. randint).
# x = random.randint(1, 100)
# print(x)
# cnt = 0
# # 2. Просит пользователя угадать число.
# while True:
#     s = int(input('Введи число: '))
#     cnt+=1
#     if s > x:
#         print('Слишком много')
#     # 3. Если пользователь ввёл число меньше загаданного, выведите "Больше! "
#     elif s < x:
#         print('Бери больше')
#     else:
#         print('Угадал! Число: ', x, 'Попыток: ', cnt)
#         break
# 4. Если больше — "Меньше!"
# 5. Если угадал — "Поздравляю!"

# Задача 10: Анализ строки
# Напишите программу, которая принимает строку от пользователя и выводит:
#vowels = 'а, е, и...'
#vowels = [i.strip() for i in vowels,split(',')]
# vowels = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э','Ю', 'Я']
# consonants = ['Б', 'В', 'Г', 'Д', 'Ж', 'З','Й', 'К', 'Л','М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
# signs = ['.', "'", ',' , ';', ':', '…', '?','!', '—', '(', ')', '«', '»']
# vowel_count = 0
# consonant_count = 0
# digit_count = 0
# str = input('Введите текст: ').upper()
# print(str.split())
# for i in str:
#     if i != ' ' and i not in signs:
#         if i in consonants:
#             consonant_count += 1
#         elif i in vowels:
#             vowel_count += 1
#         else: #elif i.isdigit:
#             digit_count += 1
# print('Количество гласных: ', vowel_count)
# print('Количество согласных: ', consonant_count)
# print('Количество цифр: ', digit_count)
# print({symbol for symbol in str if symbol in vowels})
# # 1. Количество гласных букв (а, е, ё, и, о, у, ы, э, ю, я). +
# # 2. Количество согласных букв. +
# # 3. Количество цифр. +
# # 4. Самый часто встречающийся символ (исключая пробелы).
# max_count = 0
# max_ch = ''
# count = 0
#
# for i in str:
#     if i != ' ' and i not in signs:
#         count = str.count(i)
#         if count > max_count:
#             max_count = count
#             max_ch = i
# print(f'Самый часто встречающийся символ: ', max_ch) # Выдает первую самую часто встречающуюся, если одинаковое количество раз встречается несколько букв, то выдаст только одну

# Задача 11.  Функция для работы со списком
# Напишите функцию process-list(2st) которая:
# 1. Принимает список чисел.
# 2. Возвращает новый список, где все чётные числа заменены на их квадраты, а нечётные - на и
# 3. Обработайте случай, если на вход подан не список (выведите "Ошибка: аргумент не является
# 4. Переписать через списковое включение
# 5. Переписать через lambda функцию.
#
# def process_list(numbers):
#     """Чётные — в квадрат, нечётные — как есть."""
#     result = []
#     for x in numbers:
#         if x % 2 == 0:
#             result.append(x ** 2)
#         else:
#             result.append(x)
#     return result
#
#
# while True:
#     s = input('Введите числа через пробел: ')
#     try:
#         nums = [int(x) for x in s.split()]
#     except ValueError:
#         print('Ошибка: вводите только числа, разделённые пробелами.')
#         continue
#
#     if len(nums) < 2:
#         print('Нужно ввести хотя бы два числа.')
#         continue
#
#     break
#
# print(process_list(nums))
#
#
#
# def process_list(numbers):
#     """Чётные — в квадрат, нечётные — как есть."""
#     return [x**2 if x % 2 == 0 else x for x in numbers]
#
#
# while True:
#     s = input('Введите числа через пробел: ')
#     try:
#         nums = [int(x) for x in s.split()]
#     except ValueError:
#         print('Ошибка: вводите только числа, разделённые пробелами.')
#         continue
#
#     if len(nums) < 2:
#         print('Нужно ввести хотя бы два числа.')
#         continue
#
#     break
#
# print(process_list(nums))


# c лямбдой:
# s = input('Введите числа через пробел: ')
# nums = [int(x) for x in s.split()]                    # шаг 1: строка → список чисел
# evensq = [x**2 if x % 2 == 0 else x for x in nums]    # шаг 2: обработка
# print(evensq)

# вариант 2 с лямбдой:
# def proccess_list(lst):
#     if isinstance(lst, list):
#
#         new_lst = []
#         for i in lst:
#             if i%2 == 0:
#                 new_lst.append(i**2)
#             else:
#                 new_lst.append(i)
#         return new_lst
#     else:
#         print("Ошибка: введен не список")
#
# print(proccess_list([1, 2, 3, 4]))

# Задача 12: «Камень, ножницы, бумага»
# Напишите программу, которая.
# 1.Запрашивает у пользователя выбор (камень, ножницы, бумага).
# 2. Случайным образом выбирает вариант для компьютера.
# 3. Определяет победителя (или ничью) и выводит результат.
# 4. Повторяет игру, пока пользователь не введёт "выход".

# мое решение
# def rocks_paper_scissors():
#     you = 0
#     robot = 0
#     while True:
#         x = int(input('Я хочу сыграть с тобой в игру. \nВыбирай: 1 - камень, 2 - ножницы, 3 - бумага \n(можешь выйти в любой момент, если напишешь 4 – выход): '))
#
#         if x == 4:
#             print('До встречи!')
#             break
#
#         if x not in (1, 2, 3):
#             print('Неверный ввод, попробуй ещё раз.')
#             continue
#
#         y = random.randint(1, 3)
#
#         if x==y:
#             print('Не подглядывай! Ничья')
#         elif (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
#             print('А ты хорош! Еще?')
#             you += 1
#
#         else:
#             print('Моя взяла! Хочешь отыграться?')
#             robot +=1
#         print(f'Счет: ты {you} - я {robot}')
#
# rocks_paper_scissors()

# препод
# while True:
#     options = ['rock', 'paper', 'scissors']
#     your_choice = input('Rock, paper, or scissors, mate? \nTo quit type "loser": ')
#
#     if your_choice == 'loser':
#         print('Your loss!')
#         break
#     if your_choice not in options:
#         print('Wrong option!')
#         continue
#     computer_choice = random.choice(options)
#     print(computer_choice)
#
#     if your_choice == computer_choice:
#         print('Draw!')
#     elif ((your_choice == 'rock' and computer_choice == 'paper') or
#           (your_choice == 'paper' and computer_choice == 'scissors') or
#           (your_choice == 'scissors' and computer_choice == 'rock')):
#         print('You lose! Once more?')
#     else:
#         print('You win! Again?')
#         continue

# Задача 13: Работа с датами
# Напишите программу, которая:
# 1. Запрашивает у пользователя дату рождения в формате DD. MM. YYYY.
# 2. Вычисляет возраст пользователя на текущую дату О.
# 3. Выводит результат в формате: "Вам (возраст) лет (или год/года) ".
# 4. Обработайте случай, если пользователь ввёл некорректную дату (наприме
# 31.02.2000).

# birth_date = input('Введите дату вашего рождения в формате дд.мм.гггг: ')
# try:
#     birth_date = datetime.strptime(birth_date, '%d.%m.%Y')
# except ValueError:
#     print('Ошибка: некорректная дата.')
#     exit()
#
# today = datetime.today()
# age = today.year - birth_date.year
#
# if birth_date.month > today.month or birth_date.month == today.month and birth_date.day > today.day:
#     age -= 1
#     word = ''
#     if age % 10 == 1:
#         word = 'год'
#     elif age in [2, 3, 4]:
#         word = 'года'
#     else:
#         word = 'лет'
#
#     print('Вам: ', age, word)
# else:
#     if age % 10 == 1:
#         word = 'год'
#     elif age in [2, 3, 4]:
#         word = 'года'
#     else:
#         word = 'лет'
#     print(f'Вам {age} {word}')


# # Задача 14: Работа со словарем
# user = {
# "name": "Anna",
# "age": 20,
# "city": "Moscow"
# }
#
# # 1. получить имя и возраст:
# print(user["name"], user["age"])
#
# # 2. изменить город:
# user["city"] = "New York"
# print(user["city"])
#
# # 3. добавить профессию, удалить возраст:
# user["job"] = "self-employed"
# user.pop('age')
# print(user)
# # 4. проверить наличие ключа "emai":
# print(user.get('email'))
# if 'email' in user:
#     print('found a key')
# else:
#     print('no key')
# # вывести все ключи и значения:
# print(user.keys())
# print(user.values())
# print(user.items())

# # Задача 15: Дана строка. Создать словарь подсчета слов.
#
# text = "Осень в Москве, Зима в Москве, Весна в Москве, Лето в Москве. Времена года!"
# # Создать словарь подсчета слов:
# words=text.replace (',', '').replace ('.', '').replace ('!', '').lower().split()
# counts = {}
# print(words)
# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
# print(counts)

# Задача 16: Разделить студентов по группам
# students = [
#     ('Anna', 'A'),
#     ('Ivan', 'B'),
#     ('Maria', 'A'),
#     ('Petr', 'B'),
#     ('Olga', 'C')
# ]
#
# groups = {}
# for name, group in students:
#     if group not in groups:
#         groups[group] = []
#
#     groups[group].append(name)
#
# print(groups)

# Задача 17:
# warehouse = {
#      "laptop": {"price": 80000, "quantity": 5},
#      "mouse": {"price": 1500, "quantity": 20},
#      "keyboard": {"price": 4000, "quantity": 10}
#  }
#
# # Программа должна уметь:
# # 1 - Показать товары
# # 2 - Добавить товар
# # 3 - Продать товар
# # 4 - Пополнить остаток
# # 5 - Изменить цену
# # 6 — Общая стоимость склада
# # 7 - Самый дорогой товар
# # 8 - Товары с остатком меньше 3
# # 0 - Выход
#
# while True:
#     print('1 - Show items')
#     print('2 - Add item')
#     print('3 - Sell item')
#     print('4 - Restock item')
#     print('5 - Change the price')
#     print('6 - Total warehouse value')
#     print('7 - The most expensive item')
#     print('8 - Items with quantity under 3')
#     print('0 - Exit')
#
#     choice = input('Select an option: ')
#     if choice == '0':
#         print('See you next time!')
#         break
#
#     elif choice == '1':
#         for name, info in warehouse.items():
#             print(f"{name} — {info['price']}")
#
#     elif choice == '2':
#         name = input('Enter the name of item: ')
#
#         if name in warehouse:
#             print(f'The item "{name}" already exists!')
#         else:
#             price = int(input('Enter the price of item: '))
#             quantity = int(input('Enter the quantity of item: '))
#             warehouse[name] = {'price': price, 'quantity': quantity}
#             print(f'Added: {name}')
#
#     elif choice == '3':
#         name = input('Enter the name of the item to sell: ')
#
#         if name not in warehouse:
#             print(f'The item "{name}" was not found')
#         else:
#             sold = int(input('How many to sell: '))
#
#             if sold > warehouse[name]['quantity']:
#                 print(f'Not enough items. The quantity: {warehouse[name]["quantity"]}.')
#             else:
#                 warehouse[name]['quantity'] -= sold
#                 print(f'Sold {sold} of {name}. The quantity: {warehouse[name]["quantity"]}')
#
#     elif choice == '4':
#         name = input('Enter the name of the item to restock: ')
#
#         if name not in warehouse:
#             print(f'The item "{name}" was not found')
#         else:
#             quantity = int(input('How many to restock: '))
#             warehouse[name]['quantity'] += quantity
#             print(warehouse[name]['quantity'])
#
#     elif choice == '5':
#         name = input('Enter the name of the item: ')
#         if name not in warehouse:
#             print(f'The item "{name}" was not found')
#         else:
#             price = int(input('Enter the new price: '))
#             warehouse[name]['price'] = price
#             print(warehouse[name]['price'])
#
#     elif choice == '6':
#         warehouse_price = 0
#         for name, info in warehouse.items():
#             warehouse_price += info['price'] * info['quantity']
#         print('Total warehouse value: ', warehouse_price)
#
#     elif choice == '7':
#         name, info = max(warehouse.items(), key=lambda x: x[1]['price'])
#         print(f'{name}: {info["price"]}')

#     классические алгоритм перебора
#     elif choice == '7':
        # max_price = 0
        # max_product = ""
        # for name, product in warehouse.items():
        #     if product['price'] > max_price:
        #         max_price = product['price']
        #         max_product = name
        # print(f"Самый дорогой товар {max_product} цена:{max_price}")
#
#     elif choice == '8':
#         new_items = []
#         for name, info in warehouse.items():
#             if info['quantity'] < 3:
#                 new_items.append(name)
#         print(new_items)
# # через списковое включение (list comprehension)
# #     elif choice == '8':
# #         new_items = [name for name, info in warehouse.items() if info['quantity'] < 3]
# #         print(new_items)

# Задача 18: Бронирование мест в кинотеатре
#решение 1 с циклом while
# Зал размером 10×15 мест
# rows = 10      # рядов
# cols = 15      # мест в ряду
#
# hall = [[0] * cols for _ in range(rows)]
# occupied_count = 25
#
# # Все возможные координаты (ряд, место)
# all_seats = [(r, c) for r in range(rows) for c in range(cols)]
#
# # Перемешиваем и занимаем 25 случайных мест
# random.shuffle(all_seats)
# for r, c in all_seats[:occupied_count]:
#     hall[r][c] = 1
#
# # Основной цикл бронирования
# while True:
#     ticket = int(input('Выберите ряд (или 0 для выхода): '))
#
#     if ticket == 0:
#         print('Всего доброго!')
#         break
#
#     if ticket < 1 or ticket > rows:
#         print('Такого ряда нет!')
#         continue
#
#     row_index = ticket - 1
#     available_seats = []
#     for c in range(cols):
#         if hall[row_index][c] == 0:
#             available_seats.append(c + 1)
#
#     if not available_seats:
#         print(f'В ряду {ticket} нет свободных мест. Выберите другой ряд.')
#         continue
#
#     print(f'Свободные места в ряду {ticket}: {available_seats}')
#
#     seat = int(input('Выберите место: '))
#
#     if seat not in available_seats:
#         print('Место недоступно.')
#         continue
#
#     hall[row_index][seat - 1] = 1
#     available_seats.remove(seat)
#
#     print('Успех! Место забронировано.')
#     print(f'Осталось свободных мест в ряду: {len(available_seats)}')

# # решение 2 без цикла while
# # Есть зал размером 10Х15 мест.
# rows = 10      # рядов
# cols = 15      # мест в ряду
#
# hall = [[0] * cols for _ in range(rows)]
# occupied_count = 25
#
# # # занимаем места, Дамы и Господа
# # # способ 1
# # for _ in range(occupied_count):
# #     r = random.randint(0, rows - 1)   # случайный ряд
# #     c = random.randint(0, cols - 1)   # случайное место
# #     hall[r][c] = 1 # Проблема: одно и то же место может попасться дважды →
# #     # реально занятых мест будет меньше 25. Если это не критично — способ простой.
# # # способ 2
#
# # # Все возможные координаты (ряд, место)
# all_seats = [(r, c) for r in range(rows) for c in range(cols)]
#
# # # Перемешиваем и берём нужное количество
# random.shuffle(all_seats)
# for r, c in all_seats[:occupied_count]:
#     hall[r][c] = 1
#
# # Плюсы:
# # Ровно 25 мест, без повторов.
# # random.shuffle() перемешивает список на месте
#
# # Для каждого ряда:
# # Проверить каждое место.
# ticket=int(input('Выберите ряд: '))
# available_seats = []
# if ticket < 1 or ticket > rows:
#     print('Такого ряда нет!')
# else:
#     available_seats = []
#     row_index = ticket - 1  # потому что в hall индексы с 0
#     for c in range(cols):
#         if hall[row_index][c] == 0:  # 0 = свободно
#             available_seats.append(c + 1)  # номер места с 1
#
# if available_seats:
#     print(f'Свободные места в ряду {ticket}: {available_seats}')
#     seat = int(input('Выберете место: '))
#     if seat in available_seats:
#         hall[row_index][seat - 1] = 1
#         print('Успех!')
#         print('Осталось свободных мест: ', len(available_seats) - 1)
#     else:
#         print('Место недоступно')
#
#
# else:
#     print(f'В ряду {ticket} нет свободных мест')
#     ticket = int(input('Выберите другой ряд: '))
#
#
# # Если место свободно:
# # спросить, хочет ли пользователь его купить.
# # Если пользователь согласен:
# # забронировать место.
# # После завершения вывести количество свободных мест.

# Решение препода
# hall = [[0 for place in range (15)] for row in range (10)]
# for row in range (10):
#     print (f'row {row + 1}')
#
#     for place in range (15):
#         print(f'place {place + 1}')
#         if hall[row][place] == 0:
#             answer = input('Хотите забронировать (да / нет)? ')
#             if answer == 'да':
#                 hall[row][place] = 1
#
# count = 0
# for row in hall:
#     count +=row.count(0)
#
# print(f'Количество свободных мест: {count}')
# for row in hall:
#     print(row)
#
# # Задача 19: Два поля ввода
#
# # Сделать форму: имя: ввод, возраст: ввод
# # При нажатии кнопки выводится: Привет, Имя! Тебе созраст лет!
#
# def greeting():
#     name = entry_name.get()
#     age = entry_age.get()
#     label_greeting.config(text='Привет')
#     return label_greeting.config(text=f'Привет, {name}! Тебе {age} лет.')
#
#
# win=tk.Tk()
# win.geometry('300x300')
# win.title('Greeting')
#
# label_name=tk.Label(win, text = 'Введите имя:')
# label_name.pack()
#
# entry_name = tk.Entry(win, width=15)
# entry_name.pack(pady = 10)
#
# label_age=tk.Label(win, text='Введите возраст: ')
# label_age.pack()
#
# entry_age = tk.Entry(win, width=15)
# entry_age.pack(pady = 10)
#
# button=tk.Button(win, text = 'Показать', command=greeting)
# button.pack(pady = 10)
#
# label_greeting=tk.Label(win, text='')
# label_greeting.pack()
#
# tk.mainloop()

# Задача 20: Графическое решение для «Камень, ножницы, бумага»

# options = ['rock', 'paper', 'scissors']
# win=tk.Tk()
# win.geometry('400x300')
# win.title('Rock Paper Scissors')
#
# def play(your_choice):
#     computer_choice = random.choice(options)
#     print(computer_choice)
#
#     if your_choice == computer_choice:
#         result = 'Draw!'
#     elif ((your_choice == 'rock' and computer_choice == 'paper') or
#           (your_choice == 'paper' and computer_choice == 'scissors') or
#           (your_choice == 'scissors' and computer_choice == 'rock')):
#         result = 'You lose! Once more?'
#     else:
#         result = 'You win! Again?'
#
#     result_label.config(
#         text = f'You go {your_choice}\n I go {computer_choice} \n{result}'
#
#     )
#
#
#
# def play_rock():
#     play('rock')
#
# def play_paper():
#     play('paper')
#
# def play_scissors():
#     play('scissors')
#
#
#
# label_name=tk.Label(win, text = 'Chose your weapon:')
# label_name.pack()
#
# button_rock=tk.Button(win, text = 'Rock', command = play_rock)
# button_rock.pack(pady = 10)
#
# button_paper=tk.Button(win, text = 'Paper', command = play_paper)
# button_paper.pack(pady = 10)
#
# button_scissors=tk.Button(win, text = 'Scissors', command = play_scissors)
# button_scissors.pack(pady = 10)
#
# result_label=tk.Label(win, text = '')
# result_label.pack()
#
# tk.mainloop()

# Задача 21: Написать бот с использованием datetime, который будет определять,
# сколько времени прошло или осталось до дня рождения
# # С дипсиком:
# dt = datetime.now()
# b_day = input('Введите дату (формат: ДД.ММ.ГГГГ): ')
#
# try:
#     date_ = datetime.strptime(b_day, '%d.%m.%Y')
# except ValueError:
#     print('Ошибка: некорректная дата')
#     exit()
#
# this_year_bday = date_.replace(year=dt.year)
#
# if this_year_bday < dt:
#     days = (dt - this_year_bday).days
#     print(f'Прошло: {days} дней')
# elif this_year_bday > dt:
#     days = (this_year_bday - dt).days
#     print(f'Осталось: {days} дней')
# else:
#     print('С днём рождения!')

# Препод решает:
# birthday = input('Your birthday(dd.mm.yyyy): ')
# birthday = datetime.strptime(birthday, '%d.%m.%Y').date()
# date_today = date.today()
# year_ = date_today.year
# birth_day = birthday
# birthday = birthday.replace(year=year_)
# age_days  = (date.today() - birth_day).days
# if birthday < date.today():
#     birthday = birthday.replace(year=year_+1)
#     age_days = ((date_today + timedelta(days=365)) - birth_day).days
# elif birthday == date.today:
#     print('HB')
#     exit(0)
#
# days_ = (birthday - date_today).days
#
# # age = round(age_days / 365)
# age = age_days / 365
# print(birthday-date_today)
# print(f'Количество дней до дня рождения – {days_}, Вам исполнится {age:.0f} лет')
# # Как рааньше писалась ф-строка:
# # print('Количество дней до дня рождения – {}, Вам исполнится {} лет'.format(days_, age))
# # print('Количество дней до дня рождения – %d, Вам исполнится %d лет'%(days_, age))
#
# Задача 22: Создаем анкету
#
# def close():
#     window.destroy()
#
# def clear():
#     name_entry.delete(0, END)
#     surname_entry.delete(0, END)
#     petname_entry.delete(0, END)
#     age_entry.delete(0, END)
#     txt.delete('1.0', END)
#     result_l.config(text='')
#
#
#
# def info():
#     name = name_entry.get()
#     surname = surname_entry.get()
#     petname = petname_entry.get()
#     age = age_entry.get()
#     about = txt.get('1.0', END)
#     # if name == '' or surname == '' or petname == '' or age == '':
#         # result_l.config(text='Error: Required fields are not filled')
#     if not name or not surname or not petname or not age:
#         messagebox.showwarning('Warning', 'Required fields are not filled')
#         return
#     if not age.isdigit():
#         messagebox.showwarning('Warning', 'Age must be number')
#         return
#
#     result_l.config(text=(f'Now I know everything about you, {name} {surname}. \nYou are {age} years old! As you say, {about}\nAnd I am coming for {petname}'))
#     # messagebox.showinfo('I know everything about you!',
#     #                     f'Name: {name}\nSurname: {surname}\nPetname: {petname}\nAge: {age}')
#
#
# window=Tk()
# window.geometry('600x500')
# window.title('Секретная анкета')
#
# header_frame = Frame(window)
# header_frame.pack()
#
# form_frame = Frame(window)
# form_frame.pack()
#
# text_frame = Frame(window)
# text_frame.pack()
#
# button_frame = Frame(window)
# button_frame.pack()
#
# l=Label(header_frame, text='Tell me about you')
# l.pack()
#
# name_l=Label(form_frame, text='Name')
# name_l.grid(row=0, column=0)
#
# name_entry=Entry(form_frame)
# name_entry.grid(row=0, column=1)
#
# surname_l=Label(form_frame, text='Surname')
# surname_l.grid(row=1, column=0)
#
# surname_entry=Entry(form_frame)
# surname_entry.grid(row=1, column=1)
#
# petname_l=Label(form_frame, text='Petname')
# petname_l.grid(row=2, column=0)
#
# petname_entry=Entry(form_frame)
# petname_entry.grid(row=2, column=1)
#
# age_l=Label(form_frame, text='Age')
# age_l.grid(row=3, column=0)
#
# age_entry=Entry(form_frame)
# age_entry.grid(row=3, column=1)
#
# gender = StringVar()
#
# R1 = Radiobutton(form_frame, variable=gender, value="male", text="Male")
# R1.grid(row = 4,column = 0)
#
# R2 = Radiobutton(form_frame, variable=gender, value="female", text="Female")
# R2.grid(row = 4,column = 1)
#
# about_l = Label(text_frame, text='About me')
# about_l.pack()
#
# txt = Text(text_frame, width=40, height=8)
# txt.pack(side=LEFT)
#
# scrollbar = Scrollbar(text_frame, command=txt.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
# txt.config(yscrollcommand=scrollbar.set)
#
# btn_info = Button(button_frame, text="Show info", command=info)
# btn_info.pack(pady=3)
#
# btn_close = Button(button_frame, text='Close', command=close)
# btn_close.pack(pady=3)
#
# btn_clear = Button(button_frame, text='Clear', command=clear)
# btn_clear.pack(pady=3)
#
# result_l=Label(button_frame, text='')
# result_l.pack()

# Задача: 22
# def play():
#     computer = random.choice(["red", "yellow", "green"])
#     your_choice = light.get()
#     if your_choice == computer:
#         result_l.config(text='You win!')
#     else:
#         result_l.config(text=(f'You lose! I chose {computer}\n Once more?'))
#
# window=Tk()
# window.geometry('300x200')
# window.title('Traffic light')
#
# # red = "red"
# # green = "green"
# # yellow = "yellow"
#
# light = StringVar(value="red")
# # drink = StringVar(value=coffee)
# l=Label(window, text='Choose color')
# l.pack()
#
# R1 = Radiobutton(window, text="red", value="red", variable=light)
# R1.pack()
#
# R2 = Radiobutton(window, text="yellow", value="yellow", variable=light)
# R2.pack()
#
# R3 = Radiobutton(window, text="green", value="green", variable=light)
# R3.pack()
#
# btn_choose = Button(window, text='Choose', command=play)
# btn_choose.pack(pady=3)
#
# result_l=Label(window, text='')
# result_l.pack()
# window.mainloop()

# Задача 23: Менеджер заметок

# from tkinter import filedialog as fd
#
#
# def add_note():
#
#     try:
#         file = fd.askopenfilename(
#             filetypes = [("Text", "*txt"),("All Files", "*.*")]) # настраиваем, какие типы файлов можно обработать/открыть
#
#         if not file:
#             return
#         # with open(r'/Users/kseniaperesada/Desktop/untitled/todo.txt', 'r', encoding='utf-8') as file:
#         with open(file, 'r', encoding='utf-8') as file:
#             note = file.read()
#         # note = "Remember to brush your teeth"
#             txt.insert(END, note)
#     except Exception as error:
#         messagebox.showerror("Error", error)
#
#
# def clear_note():
#     answer = messagebox.askokcancel('Q','Delete all notes?')
#     if answer:
#         txt.delete(1.0, END)
#
#
# def save():
#     try:
#         file = fd.asksaveasfilename(
#             filetypes = [("Text", "*txt")]) # настраиваем, какие типы файлов можно обработать/открыть
#
#         if not file:
#             return
#
#         with open(file, 'w', encoding='utf-8') as file:
#             note = txt.get(1.0, END)
#             file.write(note)
#             messagebox.showinfo('Info', 'File is saved')
#     except Exception as error:
#         messagebox.showerror("Error", error)
#
# def info():
#     messagebox.showinfo('Info', 'This is a notebook')
#
#
# window=Tk()
# window.geometry('500x600')
# window.title('Notes')
#
# mainmenu = Menu(window)
# window.config(menu=mainmenu)
# filemenu = Menu(mainmenu, tearoff=0)
# filemenu.add_command(label="Add", command=add_note)
# filemenu.add_command(label="Save", command=save)
# filemenu.add_command(label="Clear", command=clear_note)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=window.quit)
# infomenu=Menu(mainmenu, tearoff=0)
# infomenu.add_command(label="About", command=info)
# mainmenu.add_cascade(label="File", menu=filemenu)
# mainmenu.add_cascade(label="Info", menu=infomenu)
#
# form_frame = Frame(window)
# form_frame.pack(side=LEFT)
#
# txt = Text(form_frame, width=40, height=20, bg='lightyellow', fg='black',  wrap=WORD)
# txt.pack(side=LEFT)
#
# scrollbar = Scrollbar(form_frame, command=txt.yview)
# scrollbar.pack(side=LEFT, fill=Y)
# txt.config(yscrollcommand=scrollbar.set)
#
# btn = Button(window, text="Add", command=add_note)
# btn.pack(side=LEFT)
#
# btn_clear = Button(window, text="Clear", command=clear_note)
# btn_clear.pack(side=LEFT)
#
# btn_save = Button(window, text="Save", command=save)
# btn_save.pack(side=LEFT)
#
# window.mainloop()

# Задача 24:
