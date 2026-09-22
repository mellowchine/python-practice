# i = 0
# for _ in 2, 2, 2, 2, 2, 2, 2, 2, 1, 1:
#     i += 1
#     print(i)
# for i in range(10): #start 0, stop не выводится, step = 1
#     print(i)
# for i in range(2, 10, 2):
#     print(i ** 2)
for i in range(1,10):
    for j in range(1,10):
        print(f'{i*j:2}',end=' ')
    print()
