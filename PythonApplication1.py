import math as m


a = int(input ('����� ���������� a:'))
b = int(input ('����� ���������� b:'))
c = int(input ('����� ���������� c:'))

d =b*b - 4*a*c

if(d > 0):
    x1 = (-b + m.sqrt(d))/(2*a)
    x2 = (-b - m.sqrt(d))/(2*a)
    print('����� ��������� ����� ' + str(x1) + ' � ' + str(x2) )
elif(d == 0):
    x = -b/(2*a)
    print('������ ��������� ����� ' + str(x))
else: print('��������� �� ����� ������')