# Structures (Структури) - Структури даних
"""
Ще в далекому 1976 році швейцарський вчений Ніклаус Вірт написав книгу "Алгоритми + структури даних = програми"
І цей вислів з тих днів не змінився. (сама книга зараз не актуальна але її назва так :) )

Структура даних це контейнер (або простими словами коробка), який зберігає дані за певним макетом. Макет структури
даних дозволяє їй бути ефективною в деяких операціях та неефективною в інших. Структури даних бувають лінійними
та нелінійними
- Лінійні це коли елементи утворюють послідовність. Приклади: масиви, пов'язані списки, стеки, черги.
- Нелінійні це коли обхід вузлів нелінійний, а дані не послідовні. Приклад: граф і дерева.
Вони допомагають:
- Керувати великими наборами даних і використовувати їх
- Швидко шукати певні дані в базі даних
- Створювати чіткі ієрархічні або реляційні зв'язки між точками даних
- Спрощує і прискорює обробку даних

Основними структурами даних можливо назвати:
- масиви  (проста структура даних, де всі елементи йдуть один за одним)
(1, 2, 3, 4)

- стеки  (дані у масиві з організацією доступу по принципу LIFO - останній записаний це перший в черзі)
(початок)
3
2
1
(кінець)

- черги  (схожі зі стеком але використовують FIFO - перший записаний це перший у черзі)
як приклад звичаййна черга людей :)
(кінець)
3
2
1
(початок)

- пов'язані списки  (кожен елемент це окремий об'єкт з 2-х елементів - дані і посилання на наступний об'єкт)
посилання може бути на будь-який елемент даних у списку, що дає велику гнучкість

- графи  (набір вершин, які між собою поєднані ребрами)

- дерева  (ієрархічна структура, по суті це граф без циклів)

- префіксні дерева  (різновид дерева для строк, швидкого пошуку)
як приклад всім відомий Т9

- хеш таблиці  (унікальна ідентифікація об'єктів за розрахованим індексом(ключем у вигляді хешу), дані зберігаються
як масив у вигляді ключ - значення)


Стаття на Хабрі:
https://habr.com/ru/post/422259/


По суті структури даних, це дуже важливий елемент програмування, який застосовуються для написання складних програм.
Вони дозволяють зберігати і обробляти багато однотипних чи логічно пов'язаних данних.
Мета структур полягає у полегшенні в навігації, доступі та зміні даних. Застосовуються вони скрізь, від операційної
системи до інтерфейсної розробки та машинного навчання.

Цитата Лінуса Торвальдса(засновник ядра Linux):
«Погані програмісти думають про код. Хороші програмісти думають про структури даних та їх взаємозв'язках»

У кожної структури даних є завдання або ситуація, для вирішення якої вона найбільше підходить. Python має 4 вбудованих
структури даних, списки, словники, кортежі та набори. Більшість структур даних у Python є їх модифікованими формами або
використовують вбудовані структури в якості основи.


Давайте розглянемо ці основні 4 типи:

1. Список  (list)
схожий на масив, дозволяє зберігати набір обєктів в перемінну з можливістю їх зміни, об'являється у квадратних дужках
[...] через кому кожен елемент має індекс, який починається з 0, також можливо використовувати від'ємний індекс, який
дорівнює останньому елементу в списку
Приклад:
list('список')
що дорівнює
['с', 'п', 'и', 'с', 'о', 'к']
p = list('список')
print(p)
print(type(p))

Списки можуть бути як одного типу так і гетерогенними:
z = [3, True, 'Вітя', 2.0]
print(z)

індекси і негативні індекси
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[3])
дорівнює
print(a[-6])

Для доступу до даних можливо використовувати зрізи у вигляді 1:5 де перший вказани індекс включається а останній
вказаний не включається
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[0:4])

Зміна даних у списку выдбувається звичайним присвоєнням потрібного значення потрібному індксу у списку
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[3] = 'test'
print(a)

Python має примітивний генератор списків:
b = [b * 3 for и in 'list']
print(b)
c = [c * 3 for c in 'list' if c != 'i']
print(c)

Списки мають методи для роботи з ними, такі як count, index, sort, append, remove, pop, extend, insert та інші
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a.pop(5))
print(a)
і оператори по типу in, not in, len, min, max та інші
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(a))
print(sum(a))


2. Кортежі (tuples)
по суті це список з незміннми данними(додавати новы значення у кортеж також неможливо), кортежі об'явлені в дужки
(....), можуть включати як однорідні так і неоднорідні значення
a = ('c','a','k','e')
print(a)
print(type(a))
mixed = ('C',0,7,'K','I','E', 3.14)
for i in mixed:
    print(i,":",type(i))

Основна особливість кортежу перед списком це висока швидкість роботи
import timeit
timeit.timeit('x=(1,2,3,4,5,6,7,8,9)', number=100000)
timeit.timeit('x=[1,2,3,4,5,6,7,8,9]', number=100000)

Відповідно до основної документації Python, незмінність це "об'єкт з фіксованим значенням", тоб-то певний id визначає
розташування об'єкта в пам'яті.
Приклад кортежу зі списком
n = (1, 1, [3,4])
print(n)
id(n[0]) == id(n[1])
print(id(n[0]), id(n[1]))
print(id(n[0]), id(n[2]))

спробуємо додати до кортежу щось, буде помилка
n.append(5)
а тепер до списку у кортежі
n[2].append(5)
print(n)

При цьому айді не змінюється, хоча сам об'єк змінився, тоб-то дуже грубо кажучи айді це посилання на комірку де
зберігаються дані, які можливо в деяких випадках змінювати, але сам кортеж при цьому незмінний :)
print(id(n[0]), id(n[2]))

В основному з кортежами виконуються операції, які його не змінюють, тоб-то пошуку та перевірки наявності елемента в
масиві(in)
Зрізи, в тому числі з від'ємними значеннями
n = (0,1,2,3,4,5)
print(n[1])
print(n[-5])

Об'єднання, при умові що вони додаються у новий кортеж
x = (1,2,3,4)
print(x)
y = (5,6,7,8)
print(y)
z = x + y
print(z)

Так само виконується і множення кортежів
x = (1,2,3,4)
z = x*2
print(z)

До функцій кортежу можна перечислити функції списку, окрім тих, що можуть змінювати інформацію, тоб-то
count, len, any, tuple, min, max, sum, sorted

Ще кортежі можливо використовувати для присвоєння деяких значень одночасно
a = (1,2,3)
(one,two,three) = a
print(one)
У цьому випадку а це кортеж із 3 елементів, а (one, two, three) це кортеж 3 перемінних і кортеж присвоює кожній
перемінній кожне значення почергово


3. Набори (set та frozenset)
невпорядковані колекції, що означає, що елементи неіндексовані та не мають встановленої послідовності.
Вони оголошуються фігурними дужками {...}
Набори, на відміну від списків або кортежів, не можуть мати кілька входжень одного і того ж елемента і зберігати
невпорядковані значення, що робить набори надзвичайно корисними для ефективного видалення повторюваних значень зі
списку або кортежу і виконання загальних математичних операцій, таких як об'єднання і перетин.
a = set('hello')
print(a)
b = {'h', 'e', 'l', 'l', 'o'}
print(b)

words = ['hello', 'daddy', 'hello', 'mum']
print(words)
print(set(words))

Набори set та frozenset відрізняються тим, що frozenset неможливо змінювати а set можливо.
a = set('qwerty')
print(a)
b = frozenset('qwerty')
print(b)
print(a == b)
print(type(a))
print(type(b))
print(type(a - b))
print(type(a | b))

спробуємо щось додати до структури
a.add(1)
print(a)
b.add(1)

Ситуація з операціями та функціями з set та frozenset схожа з ситуацією зі Списком і Кортежем


4. Словник (dict)
Словник являє собою набір пар ключ/значення.Словник ініціюэться порожніми фігурними дужками {...}
і заповнюєтеься ключами і значеннями, розділеними двокрапкою. Всі ключі - унікальні та незмінні
Словники не мають порядку, тобто вони не мають першого, другого і т.д значення,
така структура націлена на швидкодію а доступ до значення надається по ключу.
p = {"Андрій": 32, "Віктор": 29, "Максим": 18}
print(p)
print(p["Максим"])

Словники можна об'єднувати і оновлювати
(|) - створює новий словник
dict1 = {"x": 1, "y":2}
dict2 = {"a":11, "b":22}
dict3 =  dict1 | dict2
print(dict3)
(|=) - оновлює перший словник
dict1 = {"x": 1, "y":2}
dict2 = {"a":11, "b":22}
dict2 |=  dict1
print(dict2)

Деякі популярні методи словника
.keys() повертає усі ключі
p = {"Андрій": 32, "Віктор": 29, "Максим": 18}
print(p.keys())

.items() повертає список кортежів
p = {"Андрій": 32, "Віктор": 29, "Максим": 18}
a = p.items()
print(a)

.get() повертає значення по ключу
p = {"Андрій": 32, "Віктор": 29, "Максим": 18}
print(p.get("Андрій"))

.clear() очищає словник від усіх елементів
p = {"Андрій": 32, "Віктор": 29, "Максим": 18}
print(p)
p.clear()
print(p)

та інш.

get() більш просунутий порівняно з підходом отримання значення по ключу.
Якщо додати в метод другий параметр, то він поверне передане значення в разі, коли ключ не буде
знайдений. Якщо другий параметр не вказувати, отримаєте none.
p = {"Андрій": 32, "Виктор": 29, "Максим": 18}
print(p.get("Михайло", "Не знайдено"))
print(p.get("Андрій", "Не знайдено"))



Тепер давайте розглянемо як ми можемо використати ці стандартні структури для створення більш складних структур

1. Масиви
Python не має встроєного типу масива, але для цього добре підходить звичайний список. Масив це набір значень одного
типу, збережених в одній перемінній.
На відміну від Java, яка має статичні масиви після їх створення, масиви в Python автоматично збільшуються чи
зменшуються при додаванні/видаленні елементів, це робить масиви в Python більш простими та адаптивними.
cars = ["Toyota", "Tesla", "Hyundai"]
print(len(cars))
cars.append("Honda")
cars.pop(1)
for x in cars:
  print(x)

Але він не підходить для наукових даних(для цього краще використовувати масив NumPy) та має керованим лише крайній
правий елемент списку....


2. Черги
це лінійна структура даних, в якій дані зберігаються в порядку(FIFO). На відміну від масивів, отримати доступ до
елементів за індексом не можна, а замість цього можна отримати тільки наступний найстаріший елемент. Це робить його
відмінним рішенням для завдань, чутливих до замовлення, таких як обробка онлайн-замовлень або зберігання голосової пошти
Ми могли б використовувати список Python з append () і pop () методами для реалізації черги. Однак це неефективно,
тому що списки повинні зрушувати всі елементи на один індекс щоразу, коли додається новий елемент на початок.
Тому для цього краще підійде крас deque з collections модуля Python.
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("queue створено та заповнено")
print(q)
# видалення елементів з queue
print("\n елементи dequeued з queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("\n queue після видалення елементів")
print(q)

Структура автоматично впорядковує дані в хронологічному порядку та має швидкий час роботи
Недолік такої структури у доступі даних лише на кінцях.


3. Стеки
це послідовна структура даних, яка діє як версія черг по (LIFO), тоб-то останній елемент, вставлений в стек, вважається
верхнім в стеку і є єдиним доступним елементом. Щоб отримати доступ до середнього елементу, потрібно спочатку видалити
достатню кількість елементів, щоб потрібний елемент перебував на вершині стека.
Реалізувати стек у Python можливо використовуючи список, в операціях push використовується append() метод, а в операціях
pop — pop().

stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print("stack заповнено")
print(stack)
print("\n popped елементи зі stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\n Stack після використання методу popped:")
print(stack)

Надає LIFO доступ до даних структури, що неможливо в масивах з автоматичним маштабуванням та очисткою
З недоліків це обмежена пам'ять та забагато об'єктів в стеці викликає помилку переповнення стека.


4. Пов'язані списки
це послідовний набір даних, який використовує реляційні покажчики на кожному вузлі даних для зв'язку з наступним вузлом
в списку. На відміну від масивів, пов'язані списки не чинні об'єктивних позицій в списку. Замість цього у них є відносні
позиції, засновані на оточуючих їх вузлах. Перший вузол у зв'язаному списку називається головним вузлом, а останній -
хвостовим вузлом та має null значеня. Python не має вбудованої реалізації пов'язаних списків і тому вимагає, самостійної
реалізації Node класу для зберігання значення даних і одного або декількох вказателів.
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
list1 = SLinkedList()
list1.headval = Node("Понеділок")
e2 = Node("Вівторок")
e3 = Node("Середа")
list1.headval.nextval = e2
e2.nextval = e3
print(list1.headval.dataval)
print(e2.dataval)
print(e2.nextval.dataval)

Легка реорганізація та ефективна вставка/видалення нових елементів
Недостатки це неефективне використання пам'яті через зберігання кожної точки вказателя та завжди повинен переміщатись
по зв'язному списку від заголока, щоб знайти наступні елементи.


5. Циклічно пов'язані списки
Основним недоліком стандартного зв'язного списку є те, що завжди потрібно починати з вузла Head. Циклічно пов'язаний
список усуває цю проблему, замінюючи null значення вузла Tail вказівником на вузол Head. При проході програма буде
слідувати вказівниками, поки не досягне вузла, на якому вона була запущена.
Перевага цієї структури полягає в тому, що можна почати з будь-якого вузла і пройти по всьому списку. Це також дозволяє
використовувати пов'язані списки в якості зацикленої структури, задавши бажану кількість циклів через структуру. Списки
з циклічним зв'язком відмінно підходять для процесів, які зациклюються протягом тривалого часу, наприклад, розподіл ЦП
в операційних системах.
class Box:
  def __init__ (self,cat = None):
    self.cat = cat
    self.nextcat = None
class LinkedList:
  def __init__(self):
    self.head = None
def contains (self, cat):
    lastbox = self.head
    while (lastbox):
      if cat == lastbox.cat:
        return True
      else:
        lastbox = lastbox.nextcat
    return False
def addToEnd(self, newcat):
    newbox = Box(newcat)
    if self.head is None:
      self.head = newbox
      return
    lastbox = self.head
    while (lastbox.nextcat):
        lastbox = lastbox.nextcat
    lastbox.nextcat = newbox
def get(self, catIndex):
    lastbox = self.head
    boxIndex = 0
    while boxIndex <= catIndex:
      if boxIndex == catIndex:
          return lastbox.cat
      boxIndex = boxIndex + 1
      lastbox = lastbox.nextcat
def removeBox(self,rmcat):
    headcat = self.head
    if headcat is not None:
      if headcat.cat==rmcat:
        self.head = headcat.nextcat
        headcat = None
        return
    while headcat is not None:
      if headcat.cat==rmcat:
        break
      lastcat = headcat
      headcat = headcat.nextcat
    if headcat == None:
      return
    lastcat.nextcat = headcat.nextcat
    headcat = None

cat = LinkedList();
cat.head = Box("Чорний")
addToEnd(cat, "Полосатий")
addToEnd(cat, "Рижий")
print(contains(cat, "Полосатий"))
removeBox(cat, "Полосатий")
print(contains(cat, "Полосатий"))


6. Дерева (затрону більше дерева двоїчного пошуку)
це ще одна заснована на відносинах структура даних, яка спеціалізується на представленні ієрархічних структур. Як і
пов'язані списки, дерева заповнюються Node об'ектами, які містять значення даних і один або кілька вказівників для
визначення його ставлення до безпосередніх вузлів.
Кожне дерево має кореневий вузол, від якого відходять всі інші вузли. Корінь містить покажчики на всі елементи
безпосередньо під ним, які відомі як його дочірні вузли. Ці дочірні вузли можуть мати власні дочірні вузли. У двоїчних
дерев не може бути вузлів з більш ніж двома дочірніми вузлами. Будь-які вузли на одному рівні називаються однорівневими
вузлами. Вузли без підключених дочірніх вузлів називаються листовими вузлами.
Найбільш поширене застосування двоїчного дерева - це двійкове дерево пошуку. Дерева двоїчного пошуку чудово підходять
для пошуку великих наборів даних, оскільки тимчасова складність залежить від глибини дерева, а не від кількості вузлів.
Під тимчасовою складністю мається на увазі час, за який виконується пошук.


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()

Має переваги у динамічному розмірі та чудовому маштабуванні, швидкі операції вставки/видалення даних
В двоїчному дереві пошука вставлені вузли відразу упорядковуються а також вони ефективні при пошуку
З недоліків це дорогий час зміни та балансування дерева, дочірні вузли не мають інформації про своїх батьків і їх важко
переміщати та працює лише для відсортованоних списків(несортовані дані відпрацьолвуються як звичайний лінійний пошук)


7. Графи
це структура даних, яка використовується для візуального представлення взаємозв'язків між вершинами даних (вузлами графа).
Зв'язки, що з'єднують вершини разом, називаються ребрами. Ребра визначають, які вершини з'єднуються, але не вказують
напрямок потоку між ними. Кожна вершина має з'єднання з іншими вершинами, які зберігаються в вершині у вигляді списку,
розділеного комами.
В Python графи найкраще реалізувати з використанням словника з ім'ям кожної вершини в якості ключа і списком ребер як
значення.
graph = {
"a" : ["b","c"],
"b" : ["a", "d"],
"c" : ["a", "d"],
"d" : ["e"],
"e" : ["d"]
}
print(graph)

Графи підходять для моделювання широкого спектра реальних проблем(мережі чи веб-структури) та мають простий для освоэння
синтаксис.
З недостатків це складність розуміння в дуже великих графах та дорогий час аналізу даних з графіку


8. Хеш таблиці
це складна структура даних, здатна зберігати великі обсяги інформації і ефективно отримувати певні елементи. У цій
структурі даних використовуються пари ключ/значення, де ключ - це ім'я бажаного елемента, а значення - це дані, що
зберігаються під цим ім'ям
Кожен вхідний ключ проходить через хеш-функцію, яка перетворює його з початкової форми в цілочисельне значення, яке
називають хешем. Хеш-функції завжди повинні генерувати один і той же хеш з одного і того ж введення, повинні швидко
обчислювати і видавати значення фіксованої довжини. Python включає вбудовану hash() функцію, яка прискорює реалізацію.
Потім таблиця використовує хеш-код для знаходження спільного розташування бажаного значення, який називають кошиком
зберігання. Після цього програмі потрібно буде шукати потрібне значення тільки в цій підгрупі, а не в усьому пулі даних.
import pprint
class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)
    def _assign_buckets(self, elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key, value))
    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None
    def __str__(self):
        return pprint.pformat(self.buckets)
if __name__ == "__main__":
     capitals = [('France', 'Paris'),
                 ('United States', 'Washington D.C.'),
                 ('Italy', 'Rome'),
                 ('Canada', 'Ottawa'),
                 ('Ukraine', 'Kyiv')]
hashtable = Hashtable(capitals)
print(hashtable)
print(f"The capital of Italy is {hashtable.get_value('Italy')}")
print(f"The capital of Ukraine is {hashtable.get_value('Ukraine')}")

Хеш-таблиці можуть приховувати ключі в любій формі в цілочисельних індексах, вони ефективні для великих наборів даних,
мають ефективний пошук та добре оптимізовані для роботи з останніми версями Python
З недоілків це потреба в унікальності хешів, помилки колізій потребують повного пересмотру хеш функцій та складні в
освоєнні


Статті про структури у Python
https://habr.com/ru/company/otus/blog/470828/
https://realpython.com/python-data-structures/
https://bestprogrammer.ru/programmirovanie-i-razrabotka/8-struktur-dannyh-python
"""
