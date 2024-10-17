def inverted_pyramid(n):
    
    for i in range(1,n):
        for j in range(1, i):
            print(' ', end='')
        for k in range(i, n):
            print("* ", end='')
        print()
        
my_num = int(input('Enter the number of rows: '))
inverted_pyramid(my_num)