"""Функция – генератор"""

def gen(n):
    i=0
    while i < n:
        i+=1
        yield i


res = gen(5)
print(res)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# не занимает память как список,
# то есть генератор экономит память

"""Выражение - генератор"""

result = (i for i in gen(5))
print(result)
