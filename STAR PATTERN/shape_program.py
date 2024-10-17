my_name = input("Enter your name: ")
print("Welcome ",my_name.upper)

print("choose a shape from the list below")
list_shape = """
    1. Hourglass
    2. Pyramid
    3. Right angle triangle
    4. left angle triangle
    5. Inverted pyramid
    6. Double pyramid
    7. Double inverted pyramid
    8. Diamond
    """
print(list_shape)

# ------------------------- Shapes ----------------------------------------
def hourglass(n):

    for i in range(1, n):
        for j in range(1, i):
            print(' ', end='')
        for k in range(i, n):
            print("* ", end='')
        print()
    for i in range(n - 2, 0, -1):
        for j in range(1, i):
            print(' ', end='')
        for k in range(i, n):
            print("* ", end='')
        print()
def pyramid(n):
    
    for i in range(n - 1, 0, -1):
        for j in range(1, i):
            print(' ', end='')
        for k in range(i, n):
            print("* ", end='')
        print()
def right_aligned_triangle(n):
    for i in range(1, n +1):
        # print space
        for j in range(n - i): 
            print("",end="")
        # print asterisks
        for k in range(i):
            print("* ", end="")
        print()
def left_aligned_triangle(n):
    for i in range(1, n +1):
        # print space
        for j in range(n - i): 
            print("  ",end="")
        # print asterisks
        for k in range(i):
            print("* ", end="")
        print()
def inverted_pyramid(n):
    
    for i in range(1,n):
        for j in range(1, i):
            print(' ', end='')
        for k in range(i, n):
            print("* ", end='')
        print()
def double_pyramid(n):
    
    for i in range(1,n+1):
        print(' '*(n-1), end="")
        for j in range(1, i+1):
            print('  *',end="")
        print("  "*((n-i)*2),end="")
        for k in range(1,i+1):
            print("* 5 ",end=" ")
        print()
def double_inverted_pyramid(n):
    
    for i in range(1,n+1):
        print(' '*(n-1), end="")
        for j in range(1, i+1):
            print('  *',end="")
        print("  "*((n-i)*2),end="")
        for k in range(1,i+1):
            print("* 5 ",end=" ")
        print()
def diamond(n):
    
    for i in range(n - 1, 0, -1):
        for j in range(1, i):
            print(' ', end='')
        for k in range(i, n):
            print("* ", end='')
        print()
    for i in range(2,n):
        for j in range(1, i):
            print(' ', end='')
        for k in range(i, n):
            print("* ", end='')
        print()
shape_input = (input("enter a shape name or number: ")).lower()
 
# convert in to 
if shape_input.isnumeric():
    shape = int(shape_input)
else:
    shape = shape_input
print(shape)

if shape == "hourglass" or shape == 1:
    num_row = int(input('enter the numbers of rows: '))
    hourglass(num_row)
    
elif shape == 'pyramid' or shape == 2:
        my_num = int(input('Enter the number of rows: '))
        pyramid(my_num)

elif shape == 'right angle triangle' or shape == 3:
            my_num = int(input('Enter the number of rows: '))
            right_aligned_triangle(my_num)
            
elif shape == 'left angle triangle' or shape == 4:
            my_num = int(input('Enter the number of rows: '))
            left_aligned_triangle(my_num)

elif shape == 'inverted pyramid' or shape == 5:
            my_num = int(input('Enter the number of rows: '))
            inverted_pyramid(my_num)

elif shape == 'double pyramid' or shape == 6:
            my_num = int(input('Enter the number of rows: '))
            double_pyramid(my_num)

elif shape == 'double inverted pyramid' or shape == 7:
            my_num = int(input('Enter the number of rows: '))
            double_inverted_pyramid(my_num)

elif shape == 'diamond' or shape == 8:
            my_num = int(input('Enter the number of rows: '))
            diamond(my_num)
else: 
    print('sorry invalid entry')