# Декоратори
"""
І так, декоратори це можливо одна з найбільш спірних і цікавих тем в Python, їм присвячено купу книг і статей, в тому
числі і на хабрі, але для багатьох розробників, особливо початківців, до кінця не зрозуміло навіщо вони потрібні,
оці ваші декоратори :)

Поняття роботи декораторів починається з одної базової концепції мови програмування Python - усі функції являються
об'єктами. Тоб-то, будь-яка функція може бути прив'язана до перемінної чи бути повернена іншою функцією і стати аргументом
Коли у функції декілька декораторів, то вони визиваються в зворотньому порядку відносно того, як вони були визвані
Також, і в сам декоратор і у функцію-обгортку можна передавати як позиційні так і іменовані аргументи (args і kwargs)
Декоратори розміщаються перед функцією, яку потрібно декорувати та при їх вказуванні починаються з символа @

Деякі особливості декораторів:
- їх можливо використовувати повторно
- вони можуть отримувати параметри та повертати значення
- вони можуть зберігати значення
- вони можуть декорувати класи
- вони можуть додавати функціональність в інші функції(чи класи)

Також Декоратори можливо використовувувати разом з іншими методами, наприклад "магічними", щоб розширити можливості
класів та всього проекту.


В двух словах декоратор, це функція, яка додає новий функціонал до іншої функції без зміни її коду. Тоб-то він ніби
обгортає (декорує) основну функцію, і розширяє її можливості

Дуже простий приклад для розігріву і розуміння концепції:
def function (drinks="Whisky"):
    return drinks.capitalize() + "!"
#виведемо функцію
print(function())
bottle = function
#виведемо перемінну
print(bottle())
#видалимо функцію та спробуємо вивести її та перемінну
del function
try:
    print(function())
except NameError:
    print("Нема такої функції")
print(bottle())


Наступний приклад демонструє роботу декораторів:
def decorator_1(func):
    print('перший декоратор =>')

    def wrapper():
        print('-- до функції', func.__name__)
        func()

    return wrapper

def decorator_2(func):
    print('другий декоратор =>')

    def wrapper():
        func()
        print('-- після функції', func.__name__)

    return wrapper

@decorator_1
@decorator_2
def wrapped():
    print('--- обгорнута(декорована) функція')

print('- старт')
wrapped()
print('- кінець')


Тут запис:
@decorator_1
@decorator_2
def wrapped():
    print('--- обгорнута(декорована) функція')

print('- старт')
wrapped()
print('- кінець')

рівнозначний запису:
def wrapped():
    print('--- обгорнута(декорована) функція')

my_decor = decorator_1(decorator_2(wrapped))
print('- старт')
my_decor()
print('- кінець')


Трохи більш реальний приклад, це вимірювання часу виконання GET запиту:
def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Час виконання: {} секунд.'.format(end - start))
    return wrapper

@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://www.python.org')
    print(webpage)

fetch_webpage()


# - клас Декоратор

Додавши метод __call__ до класу, вім стає об'єктом, який можна визвати. А оскільки декоратор це всього лиш функція,
тоб-то це об'єкт, який можна визвати, то і клас в нас буде декоратором за допомогою функції __call__

Приклад:
class MyDecorator:
    def __init__(self, func):
        print('> Клас Decorator метод __init__')
        self.func = func

    def __call__(self):
        print('> перед визовом класу...', self.func.__name__)
        self.func()
        print('> після визову класу')

@MyDecorator
def wrapped():
    print('функція wrapped')

print('>> старт')
wrapped()
print('>> кінець')


Відмінність декорації класу від методу у тому, що клас ініціюється при оголошенні, тоб-то, клас повинен отримати функцію
в якості аргументу для метода __init__. При визові декорованої функції визивається екземпляр класу, а оскільки він є
об'єктом, який можна визвати то визивається функція __call__


# - Функція з аргументами

Якщо фукнція яка потребує декорації повинна отримувати аргументи, то декоратор повинен повернути функцію з тою самою
сигнатурою, що і у функції, яку він огортає

Приклад:
import logging

def logger(func):
    log = logging.getLogger(__name__)
    def wrapper(a, b):
        log.info("Визов функції ", func.__name__)
        ret = func(a, b)
        log.info("Функція, яку визвали ", func.__name__)
        return ret
    return wrapper

@logger
def add(a, b):
    print('a + b:', a + b)
    return a + b

print('>> старт')
add(10, 20)
add(20, 30)
print('>> кінець')


# - Функція зворотнього виклику

це функція, яка визивається при спрацюванні певних подій(перехід на сторінку, отримання повідомлення, закінчення обробки
процесором). Це використовується наприклад в HTTP серверах для відповіді на URL запит

Приклад:
app = {}

def callback(route):
    def wrapper(func):
        app[route] = func
        def wrapped():
            ret = func()
            return ret
        return wrapped
    return wrapper

@callback('/')
def index():
    print('index')
    return 'OK'

print('> старт')
route = app.get('/')
if route:
    resp = route()
    print('відповідь:', resp)

print('> кінець')


# - Singleton

singleton це клас з одним екземпляром, його можна зберігати як атрибут функцыъ обгортки та повертати при запиты. Це
корисно наприклад коли ведеться робота з базою данних:

def singleton(cls):
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass

print('старт')
first_one = TheOne()
second_one = TheOne()
print(id(first_one))
print(id(second_one))
print('кінець')


# - Встроєні декоратори

У Python є встроєні декоратори, серед них найбільш важливими(які найчастіше використовуються) є трійця:
@classmethod
@staticmethod
@property

Перші два використовуються, щоб визначити методи всередині простору імен класів, які не пов'язані з конкретним
екземпляром класу. Декоратор @property використовується для налаштування гетерів і сетерів атрибутів класу.

Декоратор <*@classmethod>* може бути викликаний за допомогою екземпляра класу, або безпосередньо, через власний клас
Python як перший аргумент. Відповідно до документації Python: він може бути викликаний як в класі (наприклад, C.f()),
або в екземплярі (наприклад, C().f()). Екземпляр ігнорується, за винятком його класу. Якщо метод класу викликаний
для виведеного класу, то об'єкт виведеного класу передається в якості першого аргумента.

Декоратор @classmethod, в першу чергу, використовується як чередований конструктор або допоміжний метод для
ініціалізації.

Декоратор <*@staticmethod>* - це просто функція всередині класу. Можна викликати їх обох як з ініціалізацією класу так
і без створення екземпляра класу. Зазвичай це застосовується в тих випадках, коли у вас є функція, яка, за вашим
переконанням, має зв'язок з класом. Здебільшого, це вибір стилю.

Приклад:
class DecoratorTest(object):
    #Тестуємо звичайний метод проти @classmethod і проти @staticmethod

    def __init__(self):
        #Конструктор
        pass

    def doubler(self, x):
        print("множимо на 2")
        return x * 2

    @classmethod
    def class_tripler(klass, x):
        print("множимо на 3: %s" % klass)
        return x * 3

    @staticmethod
    def static_quad(x):
        print("множимо на 4")
        return x * 4


if __name__ == "__main__":
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(decor.static_quad(3))
    print(DecoratorTest.class_tripler(3))
    print(DecoratorTest.static_quad(2))
    #print(DecoratorTest.doubler(2))

    print(decor.doubler)
    print(decor.class_tripler)
    print(decor.static_quad)

Тут останні 3 вивода це показники, чим вони являються, останній повертає звичайну функцію замість пов'язаного метода.
Цей приклад демонструє, що ви можете визвати звичайний метод і обидва метода декоратора одним і тим же шляхом.
Обидва декотратори можливо визвати на пряму з екземпляра класа, але якщо намагатись визвати звичайну функцію за
допомогою класа:
print(DecoratorTest.doubler(2))
це дасть помилку TypeError


@property
Один з найпростіших способів використання @property, це використовувати його в якості декоратора методу. Це дозволить
перетворити метод класу в атрибут класу. Тому @property дуже часто використовують для реалізайцій гетерів і сетерів

Приклад:
class Person(object):

    def __init__(self, first_name, last_name):
        #Конструктор
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        #Повертаємо ім'я
        return "%s %s" % (self.first_name, self.last_name)

person = Person("Mike", "Driscoll")
print(person.full_name)
print(person.first_name)

#person.full_name = "Jackalope"   #дасть помилку, так як ми намагаємось змінити його на пряму

Щоб виконати зміну успішно, потрібно робити зміни його атрибутів
person.first_name = "Dan"
print(person.full_name)

Якщо ж ми приберемо декоратор @property то побачимо, що ми повертаємо об'єкти а не їх значення.

Далі приклад реалізації сетеру і гетеру без декотраторів:
from decimal import Decimal

class Fees(object):

    def __init__(self):
        self._fee = None

    def get_fee(self):

        return self._fee

    def set_fee(self, value):

        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value


f = Fees()
f.set_fee("1")
print(f.get_fee())

f.set_fee("2")
print(f.get_fee())

І ця сама реалізація але з декораторами:
from decimal import Decimal

class Fees(object):

    def __init__(self):

        self._fee = None

    @property
    def fee(self):

        return self._fee

    @fee.setter
    def fee(self, value):

        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value


if __name__ == "__main__":
    f = Fees()

f = Fees()
f.fee = "1"
print(f.fee)

f = Fees()
f.fee = "2"
print(f.fee)

Схожим чином можна виконувати і set і get і навіть видалення (@fee.deleter*)


Висновок:
І так, відповім на питання: навіщо ж потрібні декоратори? Як їх можна використовувати?
Декоратори можуть бути використані для розширення можливостей функцій з сторонніх бібліотек (код яких ми не можемо
змінювати), або для спрощення налагодження (ми не хочемо змінювати код, який ще не сформувався).
Так само корисно використовувати декоратори для розширення різних функцій одним і тим же кодом, без повторного його
переписування кожен раз.
У Django декоратори використовуються для управління кешуванням, контролем прав доступу і визначення обробника адрес.
У Twisted - для створення підроблених асинхронних inline-викликів.

Приклад на кінець :)
def benchmark(func):
    #Декоратор, що виводить час, яке зайняло
    #виконання декорованої функції.
    import time
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time() - t)
        return res

    return wrapper


def logging(func):
    #Декоратор, який логує роботу коду.

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print (func.__name__, args, kwargs)
        return res

    return wrapper


def counter(func):
    #Декоратор, який рахує і виводить кількість викликів
    #декорованої функції.

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print ("{0} була визвана: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


@benchmark
@logging
@counter
def reverse_string(string):
    return string[::-1]


print(reverse_string("На дворі трава, на траві дрова"))
print(reverse_string(
    "A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))


Трохи літератури:
https://wiki.python.org/moin/PythonDecorators
https://habr.com/en/post/524052/
https://habr.com/en/post/141411/
https://habr.com/en/post/141501/
"""
