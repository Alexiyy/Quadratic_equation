def input_valid():
    while True:
        x = int(input("Введите переменную x = "))
        if x > 0:
            collatz(x)
            break
        print("Неверное число, попробуйте другое")
    return x

def x2():
    pass

def x3_1(x):
    x = x * 3 + 1
    sp.append(int(x))
    return collatz(x)

def collatz():
    pass

def x3_1():
    pass

def collatz():
    pass

input_valid()