def left_aligned_triangle(n):
    for i in range(1, n +1):
        # print space
        for j in range(n - i): 
            print("  ",end="")
        # print asterisks
        for k in range(i):
            print("* ", end="")
        print()
my_num = int(input('Enter the number of rows: '))
left_aligned_triangle(my_num)