n = 5
for i in range(n - 1, 0, -1):
    for j in range(1, i):
        print(' ', end='')
    for k in range(i, n):
        print("* ", end='')
    print()
# for i in range(2,n):
#     for j in range(1, i):
#         print(' ', end='')
#     for k in range(i, n):
#         print("* ", end='')
#     print()