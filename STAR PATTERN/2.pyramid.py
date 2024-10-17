def pyramid(n):
    
    for i in range(n-1, 0, -1):
        for j in range(1, i):
            print(' ', end='')
        for k in range(i, n):
            print("* ", end='')
        print()
my_num = int(input('Enter the number of rows: '))
pyramid(my_num)

