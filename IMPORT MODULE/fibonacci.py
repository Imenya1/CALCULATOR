import math

x = int(input('Enter number of n!: '))
print( x,"factorial equal to: ", math.factorial(x))

#  ------------------  assignment 4 method 2 range -------------------------------

n = int(input('enter factorial number'))
fact = 1

for i in range(1,n+1):
    fact = fact * i
print(fact)