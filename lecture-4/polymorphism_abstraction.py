# Поліморфізм
# Поліморфім це різна поведінка одного й того самого метода в різних класах.
# Можемо скласти числа, а можемо поєднати їх як строки.
# Поліморфізм - дуже важлива ідея в програмуванні. Вона полягає в використанні єдиною сутності (метод, оператор або об'єкт)
#  для представлення різних типів в різних сценаріях використання

print(5 + 5) # 10
print('5' + '5') # '55'

# поліморфізм оператор додавання 

num1 = 1
num2 = 2
print(num1 + num2) # 3

str1 = "Python"
str2 = "Programming"
print(str1+" "+str2) # Python Programming.


# Поліморфізм функцій
# У Python є деякі функції, які можуть приймати аргументи різних типів.

print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))

# Відповідь
# 9
# 3
# 2
# 
# Поліморфізм у класах
# Поліморфізм - дуже важлива ідея в об'єктно-орієнтованому програмуванні.
# 
# Ми можемо використовувати ідею поліморфізму для методів класу, так як різні класи в Python можуть мати методи з одинаковим іменем.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Мяу")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Гав гав")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

# Мяу
# I am a cat. My name is Kitty. I am 2.5 years old.
# Мяу
# Гав гав
# I am a dog. My name is Fluffy. I am 4 years old.
# Гав гав

# protocol is a common polymorphism tool in Python
# it signals to user which functionality is expected
from typing import Protocol

class SoundMaker(Protocol):
    def info(self) -> str: ...

    def make_sound(self) -> str: ...

# here we don't create concrete SoundMakers but we signal to users of function 
# which object structure is expected
def make_sound_polymorphically(maker: SoundMaker): 
    return maker.make_sound()

#Абстракції - це конструктори, що дозволяють створити послідовність з інших послідовностей. 

#Напишемо функцію котра буде прораховувати скільки потрібно буде солі на довільну кількість продукту.
#Якщо на 1 кг продукту в нас іде 15 гр солі :

ingredients = {
    'salt' : 15,
    'pepper' : 2,
    'coriander' : 1.5
}

def get_ingredient_mass(m, ingr):
	return m * ingredients.get(ingr, 0) / 1000

print(get_ingredient_mass(1500, 'coriander'))


# Правильні абстракції можуть зробити код більш читабельним, 
# адаптованим і обслуговуємим, приховуючи деталі, які не важливі для поточного контексту,
#  і зменшуючи обсяг коду, необхідний для виконання тієї ж роботи - часто в кілька разів.


# Узагальнення - абстаркція це видалення частей коду котрі повторюються, або є абстрактними.

def double_list(other: list) -> list:
    result = []
    for item in other:
        result.append(item * 2)
    return result

double_list([1, 2, 3]) # [2, 4, 6]

# Нічого з цього не потрібно. Все це можна спрятати за абстракцією.
# У цьому випадку, настільки універсальної абстракції, 
# яка змінила можливість створення сучасних додатків та зменшила число явних циклів для, які нам потрібно написати.

list(map(lambda item: item * 2, [1, 2, 3])) # [2, 4, 6]

# Python map() - це вбудована функція, яка дозволяє обробляти та перетворювати всі елементи
# у ієруєрованому об'єкті без використання явного цикла for,
# методу, широко відомого як сопоставлення (mapping). map () корисний,
# коли вам потрібно змінити функцію перетворення до кожного елемента в колекції або в массив та перетворити їх у новий масив.

# ABC module has several tools to work with abstract functionality
# It enforces abstract constraints at a runtime
from abc import ABC, abstractmethod

class BaseSoundMaker(ABC, SoundMaker):
    def info(self) -> str: 
        return 'Default info'

    # method marked as abstract doesn't have implementation 
    # but requires to be overridden by child classes
    @abstractmethod
    def make_sound(self) -> str: ...


class Duck(BaseSoundMaker):
    # method override, without it TypeError is thrown
    def make_sound(self) -> str:
        return 'Quack!!'

    # we have 'magical' methods that are used by interpreter 
    # to execute operators against objects
    # For example with this add we can sum two Ducks
    def __add__(self, other: 'Duck') -> str:
        return 'DoubleDuck!!!'

my_duck = Duck()
second_duck = Duck()

my_duck + second_duck
