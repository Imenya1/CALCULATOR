import random
import string

print('PASSWORD GENERATOR')

def password_generator(length, count):
    passwords = []
    for i in range(count):
        password = ''.join(random.choice(string.ascii_letters + string.digits) for p in range(length))
        passwords.append(password)
    return passwords
length = int(input("Enter length of password character: "))  # Length of the PWD
count = int(input("Enter number of password to generate: ")) # count
passwords = password_generator(length,count)
print(count, "Password Generated: ", passwords)