import math as m


a = int(input ('Введи коэффицент a:'))
b = int(input ('Введи коэффицент b:'))
c = int(input ('Введи коэффицент c:'))

d =b*b - 4*a*c

if(d > 0):
    x1 = (-b + m.sqrt(d))/(2*a)
    x2 = (-b - m.sqrt(d))/(2*a)
    print('Корни уравнения равны ' + str(x1) + ' и ' + str(x2) )
elif(d == 0):
    x = -b/(2*a)
    print('Корень уравнения равен ' + str(x))
else: print('Уравнение не имеет корней')