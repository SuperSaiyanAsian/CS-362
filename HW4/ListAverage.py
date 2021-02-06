def findAverage(list):
    sum = 0
    
    for element in list:
        try:
            floatNum = float(element)
            sum += floatNum

        except ValueError:
            raise TypeError("Invalid Element")
            
    try:
        average = round(sum/len(list))

    except:
        raise ZeroDivisionError("Empty List Given")
    
    return average
            