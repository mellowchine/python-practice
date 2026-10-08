"""Функции – подпрограммы, которые лежат в памяти и ждут, когда их вызовут"""
import numbers
from functools import reduce

# прописываются в начале после импорта
# если функция ничего не возвращает, то она называется процедура
# должно быть прописано return, чтобы возвращала
# def proba ():
#     print('proba')
#     return 'function'
#
# n = proba()
# print(n)


# # всегда выделяется двумя строками
# def summator (x=100, y=50): # summator – имя функции, x, y – параметры функции, можно определить в самой функции
#     return x + y
#
# print(summator(90)) # позиционный аргумент
# print(summator(y=100)) # ключевой аргумент
# res=summator(100,200)
# print(res)
#
#
# def many_args (*args,**kwargs):
#     print(args)
#     print(kwargs)
#     return sum(args)
#
# print(many_args(1, 2, 3,y=20,x=34)) # выводит кортеж
# print(many_args(5, 2, 3))
# print(many_args( 3, 4, c=76)) # выводит словарь по с
#
# # область видимости переменных
# # параметры функции и определенные в ней переменные называются локальными
#
# n = 10
# print(n) # здесь просто чсило n
# print(str(n)) #здесь результат работы функции
# pass

# """Рекурсия
# Факториал:
# 3! = 1 * 2 * 3 = 3 * 2!
# 2! = 1 * 2     = 2 * 1!
# 1! = 1
# n! = n * (n-!)!
# """
#
# def factorial(n):
#     if n == 1:
#         return 1
#     else :
#         return n * factorial(n-1)
#
# print(factorial(5))

# def multiply_numbers(numbers):
#
#     res = 1
#     for i in numbers:
#         res *= i
#     print (res)
#     return res
#
#
# multiply_numbers([1,2,3,4])

# def count_unique_values(numbers):
#     unique = set(numbers)
#     print(len(unique))
#     return (len(unique))
#
# count_unique_values([1,2,3,4,5,5])

# Задача на поичк второго макисимума

# def second(numbers):
#     unique_sorted = sorted(set(numbers), reverse=True)
#     if len(unique_sorted) < 2:
#         return None
#     else:
#         return unique_sorted[1]
#
# n = second([25,25,25])
# print(n)

# Задача на вывод среднего балла студента
#
# def average_score(students, student_name):
#     v = students[student_name]
#     if student_name in students:
#         v = round(sum(v)/len(v), 2)
#         return(v)

# def compress_sequence(s):
#     if not s:  # пустая строка — частный случай
#         return ""
#
#     result = []
#     prev = s[0]
#     count = 1
#
#     for ch in s[1:]:  # начинаем со второго символа
#         if ch == prev:
#             count += 1
#         else:
#             result.append(f"({count}, {prev})")
#             prev = ch
#             count = 1
#
#     result.append(f"({count}, {prev})")  # последняя группа
#     return " ".join(result)
#
# compress_sequence('1222311')
# print(compress_sequence('1222311'))

# def invert_case(s):
#     return s.swapcase()
#
# res = invert_case('ПрИвет')
# print(res)

# def name(nm):
#     cnt = 0
#     def surname(snm):
#         # global cnt # берет переменную из основного кода
#         nonlocal cnt #берет переменную из основной функции
#         cnt += 1 # не работает, потому что cnt не является локальной переменной функции surname
#         print  (cnt, nm, snm)
#     return surname
#
# # name = ('Mary')('Petrov') # так никто не делает
# cnt = 100
# snm = name('Mary') # замыкание
# snm('Petrov')
# snm('Holland')
#
# snm = name('Max') # замыкание
# snm('Petrov')
# snm('Holland')
# snm('Max')

# def power(n):
#     return n**2
#
# n = power(5)
# print(n)


# Если все тело функции можно вложить в return,
# то меняем ее на лямбду
#
# n =(lambda n:n**2) (5) # функция выполнилась в строке
#
# print (n)
#
# l=[22, 33, 44]
"""map – функция высшего порядка, поэтому на первом месте у нее всегда какая-то еще функция, 
здесь: power, может быть str"""
#
# n = list(map(str,l)) # с помощью функции map
# n1 = [str(i)for i in l] # с помощью list comprehension – занимает больше мсте
#
# print(n, n1)
#
#
# def power(n):
#     return n*2
#
# n = list(map(power, l))
# print(n)
#

l = [22, 33, 44]
l1 = [2, 3, 4]

n = list(map(lambda n, m: n > m, l, l1))
print(n)

n = list (filter(lambda x: x % 2 == 0, l))
nn = [i for i in l if i % 2 == 0]
print(n)
print(nn)
"""Если l состоит из миллионан значений, 
то две верхние функции будут выполнять миллион итераций"""
nn = [] # классическая запись
for i in l:
    if i % 2 == 0:
        nn.append(i)


"""Если нет необходимости перебирать весь список, то мы введем break"""
nn = []
for i in l:
    if i == 10:
        nn.append(i)
        break


"""Агрегирующая функция"""
city = ["Y", "o", "r", "k", "-", 4, 5]
# city = map(str, city)
# print(city)
# res = "".join(city)
l = [1, 2, 3, 4, 5]
res = reduce(lambda n, m: str(n) + str(m), city)
print(res)

def concat(n, m):
    print("n = ", n)
    print("m = ", m)
    print (str(n) + str(m))
    return str(n) + str(m)

res = reduce(concat, city)

