"""Семинар по строкам"""

# s='"Python – современный язык программирования! Многие начинают изучать Python! Мы уже пишем код на Python!"'
# print(s.replace('Python','Java').replace('!','.').upper()) #Задание 1: заменить Питон на Джава + Задание 2: Убрать! + Задание 3: Написать заглавными
# print(len(s)) #Количество символов с пробелами
# print(len(s.replace(" ",""))) #Количество символов без пробелов
# print(len(s.replace('Python','Java').replace('!','.').upper()))
# print(len(s.replace('Python','Java').replace('!','.').upper().replace(" ","")))
# print(len(s.split()))
# print(len(s.replace('–', '').split())) # количество слов
# print(len(ls))


your_password = input('Введите пароль: ')

if len(your_password)>=8:
    has_upper = False
    has_digit = False

    for i in your_password:
        if i.isupper():
            has_upper = True
        if i.isdigit():
            has_digit = True
    if has_upper and has_digit:
        print('Хорошая защита')
    else:
        if not has_digit:
                print('Должен содержать хотя бы одну цифру')
        if not has_upper:
            print('Должен содержать заглавную букву')

else:
    print('Пароль должен быть длиннее 8 символов')