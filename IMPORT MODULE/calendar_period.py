import calendar
# ------------   -User-input-   ---------------
year = int(input("enter the calender year:  "))
month = [1,2,3,4,5,6,7,8,9,10,11,12]
# int(month) == str(month) = ['january', "february","march","april","may","june","july","august","september","october","november","december"]
# -----------      -Range-      --------------
#if month_input.isdigit():
# month = int(month_input)
# else:
#     month = list(calendar.month_name).index(month_input.capitalize())
#     #print the calendar
#     print(f"the calendar for the month of {calendar.month_name[month]} is: ")
#     print(calendar.month(year,month))
print("Enter the month range of the year: ")
_from = int(input("from: ")) 
_to = int(input('to: '))
month_range = range(_from,_to)

for  i in month_range:
# ---------         Output    ------------------
    print(calendar.month(year,i))