"""
a=int(input())
b=int(input())
if a>b:
    print(f"Число a= {a} больше")
elif a==b:
    print(f"число a = b")
else:
    print(f"число b = {b} больше")
"""
#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
"""
n=int(input())
m=int(input())
x=((m+n-1)//n)
print(x)
"""
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
"""
a = int(input())
b = int(input())
c = int(input())
a1 = (a + 1) // 2
b1 = (b + 1) // 2
c1 = (c + 1) // 2
s = a1 + b1 + c1
print(s)
"""
#Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. 
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
"""
i=int(input())
j=int(input())
x=i+j-1
print(x)
"""
#Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, или он кратен 400.
"""
year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("Yes")
else:
    print("No") 
"""
#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# a=float(input())
# print(f'{int((a*10)%10)}')



#Домашнее задание

#задача 2. Найти сумму цифр трехзначного числа
# print('Введите число')
# a = int(input())
# x = (a//100)+(a%10)+((a//10)%10)
# print(x)

#задача 4. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# print('Введите общее число журавликов')
# x = int(input())
# print(f'Катя сделала {x*4//6} журавликов, Петя сделал {x//6} журавликов, Сережа сделал {x//6} журавликов')

#Задача 6. Написать программу, которая проверяет счастливость билета (сумма трех первых цифр равна сумме трех последних)

# print('Введите номер билета')
# a = int(input())
# x = ((a//100)%10)+((a//10)%10)+(a%10)
# y = (a//100000)+((a//10000)%10)+((a//1000)%10)
# if y==x:
#     print('Да')
# else: print('Нет')

# Через массивы

# a = input('Введите номер билета: ')
# summa1 =int((a[0] + a[1] + a[2]))
# summa2 =int((a[3] + a[4] + a[5]))
# if summa1 == summa2:
#     print('yes')
# else: print('no')


#Задача 8. 
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
#  (то есть разломить шоколадку на два прямоугольника).

