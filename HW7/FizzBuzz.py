def fizzbuzz():
    OneHundred = ""

    for i in range(1, 101):
        if(i % 3 == 0 and i % 5 != 0):
            OneHundred = OneHundred + "Fizz "
        
        elif(i % 3 != 0 and i % 5 == 0):
            if(i == 100):
                OneHundred = OneHundred + "Buzz"
            else:
                OneHundred = OneHundred + "Buzz "
            
        elif(i % 15 == 0):
            OneHundred = OneHundred + "FizzBuzz "

        else:
            OneHundred = OneHundred + str(i) + " "

    return OneHundred
