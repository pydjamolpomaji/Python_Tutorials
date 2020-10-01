# Program 1 :-
# Display the Month of the Year.
import calendar

year = int(input('Enter the Year :'))
month = int(input('Enter the Month :'))

cal = calendar.month(year, month)
print(cal)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 2 :-
# Python Program to Check Leap Year
year = int(input('Enter the Year :'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('{} is leap Year'.format(year))
        else:
            print('{} is not a leap Year'.format(year))
    else:
        print('{} is leap Year'.format(year))
else:
    print('{} is not a leap Year'.format(year))
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
