"""List
тип данных = списки – упорядоченный набор объектов (в тч списков)
структура = массив
в питоне числа - неизменяемая инфа
список - изменяемая инфа
"""
import random

"""     0   1   2  3    4    5   """
nums = [22, 33, 44, 55, 99]
"""     -6  -5  -4  -3 -2 -1"""
from copy import deepcopy
# print(nums[-3])
# print(nums[3])
# print(nums[-2:0:-1])
# print(nums[2:])
# print(nums[::-1])

#
# nums = [20, 30, [40, 50]] #вложенный список
# s = nums.copy() #поверхностное копирование
# s = deepcopy(s)
# nums[0] = 200
# nums[-1][0] = 300 #вложенный объект также изменяется в копии
# print(nums)
# print(id(nums))
# print(id(s))
# # print(s)

# nums[:3] = 10, 20, 30
# print(nums)
# ls = [10, 'dasha', 5.45, True, [67, 'andre']]
# lst = [['masha', 28], ['dasha', 22]]  # вложенные списки
# # массив
# name = ['masha', 'dasha'] # массив
# age = [28, 22]            # массив
#
# print(name[0],age[0])
# nums.append(100)  # добавить объект в список, временная сложность 0(1) - низкая
# nums.extend(lst)
# nums.extend([1,2]) # к элементам одного списка добавили элементы другого списка
# nums.insert(0, 200) # поместить на 0 индекс объект 200 – линейная сложность, потому что пришлось передвинуть и переприсвоить другие индексы остальным объектам
# print(nums)
# nums += [1,2] # изменение того же объекта
# print(nums)
# # nums = nums + [1,2] #новый объект
# nums = [20, 30, [40, 50]] #вложенный список
# print(nums)
#
# nums.pop()
# n = nums.pop() # без указания индекса удаляет последний элемент, сложность константная 0(1)
# nn = nums.pop(3)
# print(id(nums))
# print('n==', n, 'nn==', nn)
# print(nums)
# print(n)
# print(len(nums))

# nums = [22, 33, 22, 55, 99, 100]
# print(nums)
# print(nums.count(22))
# print(sum(nums))
# print(max(nums))
# print(min(nums))
# nums.pop()
# print(nums)
# nums.remove(33) #удаляет только первый подходящий объект

#
# while 22 in nums:
#     nums.remove(22) #убрать все подходящие объекты в списке
#
# print(nums)
# print(nums.index(22)) #под каким индексом находится 22
# print(nums.index(22, 1))
#
# nums.reverse() #обратный срез, объект тот же самый
# print(nums)
# print(id(nums))
# print(nums[::-1]) #обратный срез с созданием нового объекта
# print(id(nums))
#
# nums.sort(reverse=True)
# print(nums)

# nums = []
# n = float(input('> '))
# while n != -273:
#     nums.append(n)
#     n = float(input('> '))
# print(f'min = {min(nums)}\nmax = {max(nums)}\nmean = {sum(nums)/len(nums):.2f}')

nums = [22, 33, 44, 55, 99]
ls = [2, 3, 4, 5, 9]
print(nums)
#итерация по индексу
for i in range(len(nums)): #в i получаем индексы - 0, 1, 2, 3, 4, длинну задаем по короткой коллекции
    print(i, nums[i], ls[i], end=' ')
print()
cnt=0
for i in nums:
    print(cnt, i, end='   ')  # по значению
    cnt+=1
print()
for i in enumerate(nums):  #формирует кортеж
    print(i, end=' ')
print()

for i in enumerate(nums):  #формирует кортеж
    print(i[0], i[1], end=' ')
print()

for i, j in enumerate(nums):
    print(i, j, end=' ')
print()

names = ['fedor', 'alisa', 'glasha', 'masha']
names.sort()
for n, name in enumerate(names, 1):
    print(f'{n}. {name}')

for i, j in zip(nums, ls): #формирует одноиндексные кортежи из двух списков
    # print(i)
    print(i-j)

# генерация случайных вещественных (не целых) чисел
print(random.random())
print(random.uniform(1, 10))

# генерация целых случайных чисел
print(random.randint(1, 10)) # старт и стоп ВХОДЯТ
print(random.randrange(1, 100, 2)) # с шагом можно генерировать четные / нечетны / кратные какому-то числу

# случайный выбор из коллекции
print(random.choice(nums))
print(random.choice(range(1, 100, 2)))
print(random.choice(names))

# генерация коллекции из случайных объектов
print(random.choices ('абвгдеёж', k = 4))
print(random.choices(names, k = 3))
print(random.sample(names, k = 3)) # с использованием уникальных индексов = k не может быть ддиннее списка
print(random.sample(names, len(names)))

a = 'I like python, it is very useful for data analysis'
b = 'python is the best tool for dealing with big data'
res = [word for word in b if word not in a]