"""Кортежи"""
from ctypes.wintypes import tagPOINT

"""Кортеж – упорядоченный список неизменяемых объектов"""
#
# from string import ascii_lowercase, ascii_uppercase, digits,
# print(ascii_lowercase)
#
# t = 22
# tp = (22, 33, 44)
# print(id(tp[0]), id(t)) #что за магия
# print(tp)
# print(tp[2]) #получение значения по индексу
# print(tp[:-1]) #все элементы, кроме последнего
# print(tp[::-1]) # обратный срез кортежа
# print(list(tp))
# str = 'qwerty'
# list = list(str)
# print(list)
# print(''.join(list))
# tps = tuple(str)
# print(tps)
# print(''.join(tps))
# n = 7
# print(type(n))
# print(n)
#
#
# print(ord('A')) #латиница
# print(ord('А')) #кириллица
#
# print(chr(1049))
#
# n, m, z = 7, 5, 8 #== n, m, z = (7, 5, 8)
# print(type(n))
# print(n)
#
# PI = 3.1415926,
# print(type(PI))
#
# name, *marks = 'Ivan', 4, 5, 6, 7 #упаковать в коллекцию
# print(name)
# print(*marks)

# tp = ('login', 'pwd', 'uname')
# print(tp)
# print(id(tp))
# buff = list(tp)
# print(buff)
# buff[-1] = 'qwerty'
# tp = tuple(buff)
# print(id(tp))
# print(tp)

tp = 22, 33, 44, 22
print(type(tp))
print(len(tp))
print(tp.count(22))
print(tp[0] == tp[-1])
print(tp[0] is tp[-1]) #один и тот же объект
print(id(tp[0]), id(tp[-1]))








