def nthFibonacci(a):
    if a < 0:
        raise ValueError("Invalid Fibonacci Number!")
    elif a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 1
    else:
        return nthFibonacci(a-2) + nthFibonacci(a-1)

def factorial(a):
    if a < 0:
        raise ValueError("Invalid Fibonacci Number!")
    elif a == 1:
        return 1
    else:
        return a * factorial(a-1)