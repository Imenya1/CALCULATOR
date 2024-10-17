# n = 8
# for i in range(n - 1, 0, -1):
#     for j in range(1, i):
#         print(' ', end='')
#     for k in range(i, n):
#         print("* ", end='')
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(1, i):
#         print(' ', end='')
#     for k in range(i, n):
#         print("* ", end='')
#     print()

def double_pyramid(n):
    
    for i in range(1,n+1):
        print(' '*(n-1), end="")
        for j in range(1, i+1):
            print('  *',end="")
        print("  "*((n-i)*2),end="")
        for k in range(1,i+1):
            print("* 5 ",end=" ")
        print()
            
my_num = int(input('Enter the number of rows: '))
double_pyramid(my_num)
    