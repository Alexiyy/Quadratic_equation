def input_valid():
    while True:
        x = int(input("Введите переменную x = "))
        if x > 0:
            collatz(x)
            break
        print("Неверное число, попробуйте другое")
    return x

def x2(x):
    x = x / 2
    sp.append(int(x))
    return collatz(x)

def x3_1(x):
    x = x * 3 + 1
    sp.append(int(x))
    return collatz(x)

def collatz(x):
   
sp = []
input_valid()
print ('Список имеет вид: '+str(x))
