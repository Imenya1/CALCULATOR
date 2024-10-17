import calendar

year = int(input("Enter calendar year: "))
month_input = (input("Enter month: "))
if month_input.isdigit():
    month = int(month_input) 
if month < 1 or month > 12:
    print("Invalid entry: \"restart the program\"")
else:
    print(calendar.month(year,month))