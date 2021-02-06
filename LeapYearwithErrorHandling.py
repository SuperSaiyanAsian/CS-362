def leap(year):
    if year % 4 != 0 :
        print(year, 'is not a leap year.\n')
    elif year % 100 == 0:
        if year % 400 == 0:
            print(year, 'is a leap year.\n')
        else:
            print(year, 'is not a leap year.\n')
    else:
        print(year, 'is a leap year.\n')

# To run this program, run 'py .\LeapYearwithErrorHandling.py' in terminal.
inputYear = input("Enter desired year: ")

try:
    integer = int(inputYear)
    leap(integer)
except ValueError:
    try:
        floatNum = float(inputYear)
        print("Invalid year. Input \"" + str(floatNum) + "\" is a floating point number.")
    except ValueError:
        print("Invalid year. Input \"" + inputYear + "\" is a string.")
