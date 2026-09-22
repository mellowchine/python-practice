# """0123456789"""
# s= 'Здравствуйте, гости!'
# s1= 'казак'
# print(s[2])
# for i in range(len(s)):
#     print(i, s[i],end='  ')
# print()
# print(s[::-1])
# print()
# print(len(s))
# print(s[:12])
# print(s[4:])
# print(s[4::-1])
#
#
# if s1 == s1[::-1]:
#     print("Yes")
# else:
#     print("No")
#
# s= 'Здравствуйте, гости!'
# s1= '123456789'
# print(s.isalpha ()) #letters
# print(s.isdigit()) #digits
# print(s.isalnum()) #letters and digits
# print(s.islower())
# print()
# print(s1.isalpha ())
# print(s1.isdigit())
# print(s1.isalnum())
# print(s1.islower())
# print()
# print(s1.islower())
# # for i in s:
# #     print(i,end='  ')
# # print(len(s))
# print(s.lower())
# print(s.rjust(60))
#
# print(s.strip('! З')) #Убирает по краям знаки, если пустой, убирает пробелы
# print(s.rstrip('З ! и'))
# print(s.index('т')) #под каким индексом находится Т
# print(s.index('т',2,10)) #есть ли с 2 по 10 индекса буква Т
# print(s.find('т',2,8))
# print(s.find('т',1,2))# 101 = 1*2**2 + 2**0
# print(s.replace('т','Т',4).replace(',','.'))
# ls = s.split(', ') #изменяет строчку на список слов по разделителю
# print(ls)
#
# print(''.join(ls))
#
# s1 = 'aaa bbb ccc ddd '
# s2 = '111 222 333 444 '
# #получить aaa 111 bbb 222...
# # print(s1 + s2)
# # ls1=s1.split(' ')
# # ls2=s2.split(' ')
# # print(ls1)
# # print(ls2)
# # print(ls1[0]+ls2[0])
# # s3=ls1[0]+ls2[0]
# # print(s3)
#
# # result = s1.join(s2)
# # print(result)

# res=s1[:4]+s2[:4]+s1[4:8]+s2[4:8]+s1[8:12]+s2[8:12]+s1[12:16]+s2[12:16]
# # print(res)
# #если при изменении условия, меняетя решение, решение неверное
# s1 = 'aaa bbb ccc ddd '
# s2 = '111 222 333 444 '
# res =  ''
# for i in range(0,len(s1), 4):
#     res += s1[i:i+4] + s2[i:i+4]
# print(res)
# # s='-3x^2+4x-6=0'
# # a=s.find('x^2')
# # print(a)
#

# s = 'Строка символов'
# # print(s[1::2])
# res = []
# for n, symb in enumerate(s): # пронумеровать все объекты - после S прописать с какого числа пронумеровать
#     if n % 2 != 0:
#         res.append(symb)
# # print(''.join(res))
# print(res)
# # print(''.join([symb for n, symb in enumerate(s) if n % 2 != 0])) # list comprehension

# s = 'hellowclkdmvckmkdaorld'
# # print({symb: s.count(symb) for symb in set(s) }) # быстрый способ
# res = {}
# cnt = 0
# # for symb in set(s):
# for symb in s:
#     res[symb] = s.count(symb)
#     cnt += 1
# print(res)
# print(cnt)
