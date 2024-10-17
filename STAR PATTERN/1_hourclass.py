# def hourglass(n):

#     for i in range(1, n):
#         for j in range(1, i):
#             print(' ', end='')
#         for k in range(i, n):
#             print("* ", end='')
#         print()
#     for i in range(n - 2, 0, -1):
#         for j in range(1, i):
#             print(' ', end='')
#         for k in range(i, n):
#             print("* ", end='')
#         print()
# num_row = int(input('enter the numbers of rows: '))
# hourglass(num_row)

from CLASS_EXAMPLE.add2v import add
a = int(input("enter number: "))
b = int(input("enter a number: "))
add(5,5)