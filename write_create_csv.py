import csv
file_name = input('Enter file name: ')
name = input('Enter your fullname')
age = int(input('Enter your age'))
gender = input('enter male or female')

with open(file_name, 'w') as file:
    text = writerow()