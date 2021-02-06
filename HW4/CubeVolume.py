def findVolume(edge):
    try:
        floatNum = float(edge)
        return round(floatNum*floatNum*floatNum)
        
    except ValueError:
        raise TypeError("Invalid Edge")
