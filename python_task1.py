#1
a = int(input())
print(a, a + 1, a + 2, sep='\n')

#2
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#3
x = int(input())
print('Объем равен', x * x * x)
print('Площадь полной поверхности равна', 6 * x * x)

#4
a = int(input())
b = int(input())
print(3 * (a+b) * (a+b) * (a+b) + 275 * b * b - 127 * a - 41)

#5
a = int(input())
print('Предыдущее число:', a - 1)
print('Текущее число:', a)
print('Следующее число:', a + 1)


#6
monitor=9900
systemblock=55600
keyboard=3999
mouse=2990
print('Цена трёх компьютеров:', (monitor + systemblock + keyboard + mouse) * 3)


#7
a1 = int(input())
d = int(input())
n = int(input())
print(a1+d*(n-1))

#8
x=int(input())
print(x,'---', 2*x,'---', 3*x,'---', 4*x,'---', 5*x, sep='', end='')

#9
n=int(input())
k=int(input())
a=k%n
b=k//n
print('Кол-во мандаринов на школьника:', b,'Остаток мандаринов:', a)


#10
t=int(input())
print(t//2 + t%2)


#11
m = int(input())
h = m // 60
s = m % 60
print(m, "мин - это", h, "час", s, "минут.")


#12
num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма чисел =", c + b + a)
print("Произведение чисел =", c * b * a)


#13
number_of_penguins = input()
print('   _~_    ' * int(number_of_penguins))
print('  (o o)   ' * int(number_of_penguins))
print(' /  V  \\  ' * int(number_of_penguins))
print('/(  _  )\\ ' * int(number_of_penguins))
print('  ^^ ^^   ' * int(number_of_penguins))


#14
abc = int(input())
k = 1
n = (abc // 10 ** k) % 10
print(n)


#15
n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)


#16
n = int(input())
print(1 - n)


#17
n = int(input())
print((n//2+1)*2)


#18
v = int(input())
t = int(input())
a = v * t
n = a // 109
print(-(109 * n - a))


#19
h = float(input())
a = float(input())
b = float(input())
print(int(1 + (h - b - 1) / (a - b)))
