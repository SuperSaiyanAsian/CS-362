def generateFullName(first, last):
    for char in first:
        if char.isdigit():
            raise TypeError("Invalid Name(s) Given")

    for char in last:
        if char.isdigit():
            raise TypeError("Invalid Name(s) Given")

    fullName = first + " " + last
    
    return fullName
