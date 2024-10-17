print('FIBONACCI SEQUENCE')

def fibonacci(count):
   fib_s = [0, 1]

   any(map(lambda _:fib_s.append(sum(fib_s[-2:])), range(2,count)))
   
   return fib_s[:count]

nth = int(input('enter n_term of the sequence: '))

print(fibonacci(nth))