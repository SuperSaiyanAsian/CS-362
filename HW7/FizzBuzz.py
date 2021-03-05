def fizzbuzz():
    OneHundred = ""

    for i in range(1, 101):
        if(i % 3 == 0):
            OneHundred = OneHundred + "Fizz "

        else:
            if(i == 100):
                OneHundred = OneHundred + str(i)
            else:
                OneHundred = OneHundred + str(i) + " "

    return OneHundred
