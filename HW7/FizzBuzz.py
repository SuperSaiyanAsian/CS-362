def fizzbuzz():
    OneHundred = ""

    for i in range(1, 101):
        if(i == 100):
            OneHundred = OneHundred + str(i)

        else:
            OneHundred = OneHundred + str(i) + " "

    return OneHundred
