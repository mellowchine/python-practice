"""Алгоритмы"""
from unittest import result
from xml.dom.minidom import ProcessingInstruction

# age=int(input('Введите возраст: '))
#
# if age>=18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# tot=int(input('Введите остаток на счету: '))
# sm=int(input('Введите сумму для снятия: '))
# result=tot-sm
# if sm<=tot:
#     print('Заберите деньги.', 'Остаток на стече:', result)
# else:
#     print('Недостаточно денег на счете. Введите сумму меньше.')
# """Калькулятор"""
#
# n=int(input('Введите первое число:'))
# n1=int(input('Введите второе число:'))
# sign=input('Введите операцию:')
# result = 0
# if sign == '+':
#     result = n + n1
# elif sign == '-':
#     result = n - n1
# elif sign == '*':
#     result = n * n1
# elif sign == '/':
#     if n1==0:
#         result='Низя!'
#     else:
#         result = n / n1
# print(result)

"""Проверка логина и пароля"""
# login='admin'
# password='password'
# your_login=input('Введите логин: ')
# your_password=input('Введите пароль: ')
# if login==your_login and password==your_password:
#     print('Успех!')
# else:
#     print('Не повезло, не фортануло')

# login='admin'
# password='password'
# while True:
#     your_login=input('Введите логин: ')
#     your_password=input('Введите пароль: ')
#     if login==your_login and password==your_password:
#         print('Успех!')
#         break
#     else:
#         print('Не повезло, не фортануло')

"""Это очень рабочий отввет дипсик"""
# login = 'admin'
# password = 'password'
#
# for user in range(1, 11):  # обрабатываем 10 пользователей
#     print(f"\n--- Пользователь {user} ---")
#     your_login = input('Введите логин: ').lower()
#
#     attempts = 0
#     while attempts < 3:
#         your_password = input('Введите пароль: ').lower()
#         if your_login == login and your_password == password:
#             print('Успех! Доступ разрешён.')
#             break  # выходим из цикла попыток
#         else:
#             attempts += 1
#             print(f'Не повезло, не фортануло. Осталось попыток: {3 - attempts}')
#
#     # Если после трёх попыток пароль так и не был введён верно
#     if attempts == 3:
#         print('Учётная запись заблокирована. Переход к следующему пользователю.')
#
# print("\nВсе пользователи обработаны.")



# login = 'admin'
# password = 'password'
#
# for i in range(1, 11):
#     print(f'User{i}')
#
#     your_login = input("Логин: ").lower()
#     if your_login == login:
#
#         attempts = 0
#         while attempts < 3:
#             your_password = input('Пароль: ').lower()
#             if your_login == login and your_password == password:
#                 print('Проходи, чувствуй себя как дома! (Но не забывай, что ты в гостях)')
#                 break
#             else:
#                 print('Неверный пароль! Повнимательнее!')
#                 attempts += 1
#         i+=1
#     else:
#         print('Промахнулся в буквах?')
