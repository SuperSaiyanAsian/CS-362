def leap(year):
    if year % 4 != 0 :
        print(year, 'is not a leap year.')
    elif year % 100 == 0:
        if year % 400 == 0:
            print(year, 'is a leap year.')
        else:
            print(year, 'is not a leap year.')
    else:
        print(year, 'is a leap year.')

# To run this program, uncomment the following line, replace the '?' with desired year, and run 'py .\LeapYear.py' in terminal.
#leap(?)