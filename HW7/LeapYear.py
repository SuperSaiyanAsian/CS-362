def leap(year):
    if(year % 4 == 0 and year % 100 != 0):
        return("Year " + str(year) + " is a leap year.")
    
    elif(year % 400 == 0):
        return("Year " + str(year) + " is a leap year.")

    else:
        return("Year " + str(year) + " is not a leap year.")
