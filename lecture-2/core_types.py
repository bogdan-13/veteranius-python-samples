''' ТИПИ ДАНИХ
ЧИСЛА

int (підписані цілі числа) - їх часто називають просто цілими числами,
це додатні чи від’ємні цілі числа без десяткової коми.

long (long integers ) - їх також називають довгими, це цілі числа необмеженого розміру,
що записуються як цілі числа, після яких слідує велика чи мала літера L.

float - реальні значення з плаваючою точкою) - їх також називають плаваючими,
вони представляють дійсні числа і записуються з десятковою точкою,
що ділить цілу і дробову частини. Поплавки також можуть бути в наукових позначеннях,
при цьому E або e позначають потужність 10 (2,5e2 = 2,5 x 102 = 250).
'''

int_example = 10
print(int_example)
print(type(int_example))


float_example = 10.45
print(float_example)
print(type(float_example))


'''
З ними виконуються усі математичні операції: +Addition\\-Subtraction\\*Multiplication\\/Division\\%Modulus\\
**Exponent\\//Floor Division

Також з числами виконуються усі операції порівняння: ==	\\ != \\ > \\ < \\ >= \\ <=
'''

var1 = 12
var2 = 5

print(var1 - var2)
print(var1 / var2)
print(var1 % var2)

'''
STRINGS - рядки, або текст
є одними з найпопулярніших типів у Python. Ми можемо створити їх, просто вклавши символи в лапки. 
Python трактує одинарні лапки так само, як подвійні лапки. 
Створення рядків просте, як присвоєння значення змінній. Наприклад -
'''

example1 = 'I studying Python'
exapmle2 = "Hello World!"

print(example1)
print(exapmle2)

'''Операції, які можна виконувати з рядками
У Пайтоні, кожен символ у рядку вважається підрядком цього рядка, і до нього можна звернутися за допомогою 
квадратних дужок
'''

example1 = 'I studying Python'
exapmle2 = "Hello World!"
print("example1[0]: ", example1[0])
print("exapmle2[1:5]: ", exapmle2[1:5])

'''
Updating Strings Оновлення рядків
Ви можете "оновити" існуючий рядок, (пере) призначивши змінну іншому рядку. 
Нове значення може бути пов’язане з попереднім значенням або взагалі із
 зовсім іншим рядком. Наприклад - 
 '''

var1 = 'Hello World!'
print("Updated String :- ", var1[:6] + 'Python')

'''
Також ми можемо 
+	Concatenation - Adds values on either side of the operator	a + b will give HelloPython
*	Repetition - Creates new strings, concatenating multiple copies of the same string	a*2 will give -HelloHello
[]	Slice - Gives the character from the given index	a[1] will give e
[ : ]	Range Slice - Gives the characters from the given range	a[1:4] will give ell
in	Membership - Returns true if a character exists in the given string	H in a will give 1
not in	Membership - Returns true if a character does not exist in the given string	M not in a will give 1
'''
a = 'Hello'
b = 'Python'
print(a + b)
print(a*3)
print('H' in a)
print('W' in b)
print('P' not in b)

'''
Екранування лапок
'''
# print('Ми екрануємо лапки обов'язково, щоб не було помилки')
print('Ми екрануємо лапки обов\'язково, щоб не було помилки')



'''
За допомогою потрійних лапок ми можемо записувати у змінну текст за обсягом більший за один рядок
'''
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB  and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets , or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)

'''В пайтоні існує багато методів для роботи з рядками'''
#Отримати кількість символів у рядку
print(len(para_str))

#Повертає рядок записаний великими літерами
print(para_str.upper())

#Знаходить вказаний рядок у іншому рядку, повертає індекс позиції, якщо знаходить і -1, якщщо ні
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB  and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets , or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str.find('long'))
print(para_str.find('long', 11))
print(para_str.find('long', 1, 9))

var = 'Evgen is'
age = 32
str_age = '32'

print('I know what', var, age)

str_age = int(str_age)

if age == str_age:
    print('OK')












