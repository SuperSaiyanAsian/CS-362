def leap(year):
    if(year % 4 == 0):
        return("Year " + str(year) + " is a leap year.")
    
    else:
        return("Year " + str(year) + " is not a leap year.")
