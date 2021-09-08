""" Коли ви пишете код, ви пишете його для двох основних аудиторій:
ваших користувачів та ваших розробників (включаючи вас). Обидві аудиторії однаково важливі. """

""" Загалом, коментування - це опис вашого коду розробникам.
Призначена основна аудиторія - це супроводжувачі та розробники коду Python. 
У поєднанні з добре написаним кодом коментарі допомагають читачеві краще зрозуміти ваш код, 
його призначення та дизайн:

Код підказує вам, як; Коментарі говорять вам чому """

"""
Документальний код описує користувачам його використання та функціональні можливості. 
Хоча це може бути корисним у процесі розробки, основна цільова аудиторія - це користувачі. 

Коментарі створюються на Python за допомогою знака фунта (#) 
і мають бути короткими висловлюваннями, що не перевищують кількох речень. Ось простий приклад:
"""

def hello_world():
    # A simple comment preceding a simple print statement
    print("Hello World")

"""
Відповідно до PEP 8, коментарі повинні мати максимальну довжину 72 символи. 
Це вірно, навіть якщо у вашому проекті максимальна довжина рядка перевищує
 рекомендовані 80 символів. Якщо коментар буде перевищувати ліміт символу коментаря,
  доцільно використовувати кілька рядків для коментаря
"""
def hello_long_world():
    # A very long statement that just goes on and on and on and on and
    # never ends until after it's reached the 80 char limit
    print("Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooo World")

"""
Commenting your code serves multiple purposes, including:
    Планування та перегляд: Коли ви розробляєте нові частини коду, можливо,
     доцільно спочатку використовувати коментарі як спосіб планування або окреслення 
     цього розділу коду. Не забудьте видалити ці коментарі після того, як кодування буде
      реалізовано та перевірено/перевірено:
"""
# First step
# Second step
# Third step

"""
Опис коду: Коментарі можна використовувати для пояснення намірів окремих розділів коду:
"""
# Attempt a connection based on previous settings. If unsuccessful,
# prompt user for new settings.

"""
Опис алгоритму: Коли використовуються алгоритми, особливо складні,
 може бути корисно пояснити, як працює алгоритм або як він реалізований у вашому коді. 
 Також може бути доречним описати, чому конкретний алгоритм був обраний замість іншого.
"""
# Using quick sort for performance gains

"""
Тегування: Використання тегів може бути використано для позначення певних розділів коду, 
де знаходяться відомі проблеми або сфери вдосконалення.
 Деякі приклади: BUG, FIXME та TODO.
"""
# TODO: Add condition for when val is None

"""
Коментування коду за допомогою підказки типу (Python 3.5+)

Підказка на тип була додана до Python 3.5 і є додатковою формою, 
яка допоможе читачам вашого коду. 
 Це дозволяє розробнику розробляти та пояснювати частини свого коду без коментарів.
  Ось короткий приклад:
"""
def hello_name(name: str) -> str:
    return(f"Hello {name}")

"""
Вивчивши натяк на тип, можна негайно сказати, що функція очікує, 
що ім'я вводу буде мати тип str або string. Ви також можете сказати, 
що очікуваний вихід функції буде мати тип str або рядок. 
Хоча натяки на типи допомагають зменшити коментарі, враховуйте, 
що це також може зробити додаткову роботу під час створення або оновлення проектної документації.
"""

"""
Базове документування коду з використанням Docstrings
"""

"""
1. Docstrings Background
Документація вашого коду Python зосереджена на docstrings.
Це вбудовані рядки, які при правильному налаштуванні можуть 
допомогти вашим користувачам і вам самим з документацією вашого проекту. 
Поряд з docstrings, Python також має вбудовану функцію help (), 
яка роздруковує об'єкти, що позначають docstrings, на консолі.
"""
# help(str)
# Help on class str in module builtins:
#
# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object. If encoding or
#  |  errors are specified, then the object must expose a data buffer
#  |  that will be decoded using the given encoding and error handler.
#  |  Otherwise, returns the result of object.__str__() (if defined)
#  |  or repr(object).
#  |  encoding defaults to sys.getdefaultencoding().
#  |  errors defaults to 'strict'.
 # Truncated for readability
# str = "!!"

dir(str)
print(str.__doc__)

"""
Вуаля! Ви виявили, де рядки документів зберігаються в об’єкті. Це означає, що ви можете
безпосередньо маніпулювати цією властивістю. Однак існують обмеження для вбудованих пристроїв:
"""
# >>> str.__doc__ = "I'm a little string doc! Short and stout; here is my input and print me for my out"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can't set attributes of built-in/extension type 'str'

"""Але, якщо ми використаємо це для будь якого іншого об'єкту, то все праюватиме нормально"""

def say_hello(name):
    print(f"Hello {name}, is it me you're looking for?")
say_hello.__doc__ = "A simple function that says hello... Richie style!"

help(say_hello)
# Help
# on
# function
# say_hello in module
# __main__:
#
# say_hello(name)
# A
# simple
# function
# that
# says
# hello...Richie
# style

"""
У Python є ще одна функція, яка спрощує створення рядків документів. 
Замість того, щоб безпосередньо маніпулювати властивістю __doc__, 
стратегічне розміщення рядкового літералу безпосередньо під об'єктом 
автоматично встановить значення __doc__. Ось що відбувається з тим самим прикладом, 
як описано вище:
"""


def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")

# help(say_hello)

# Help
# on
# function
# say_hello in module
# __main__:

# say_hello(name)
# A
# simple
# function
# that
# says
# hello...Richie
# style

"""
Docstring Types
 Їх мета - надати користувачам короткий огляд об'єкта. Вони повинні бути 
достатньо стислими, щоб їх було легко обслуговувати, але при цьому були достатньо інформативними,
щоб нові користувачі зрозуміли їх призначення та спосіб використання задокументованого об’єкта.

У всіх випадках рядки документів повинні використовувати формат рядка з потрійними 
 лапками (""" """). Це слід робити незалежно від того, чи є рядок документів багаторядковим чи ні.
Як мінімум, рядок документів повинен бути коротким підсумком того, 
що ви описуєте і має розміщатися в одній лінії:
"""
"""This is a quick summary line used as a description of the object."""

"""
Багаторядкові рядки документів використовуються для подальшого детального опрацювання об’єкта, 
окрім резюме. Усі багаторядкові струнні стрічки мають такі частини:

Однорядковий підсумковий рядок
Пустий рядок, що йде за підсумком
Будь -які подальші розробки для рядка документів
Ще один порожній рядок
"""

"""This is the summary line

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

# Notice the blank line above. Code should continue on this line.

"""
Усі рядки документів мають мати таку ж максимальну довжину символів, 
що й коментарі (72 символи). Докстринги можна розділити на три великі категорії:

 --Class Docstrings: Class and class methods
 --Package and Module Docstrings: Package, modules, and functions
 --Script Docstrings: Script and functions
"""

"""
Class Docstrings
Class Docstrings створюються для самого класу, а також для будь -яких методів класу.
 Рядки документів розміщуються одразу за класом або методом класу з відступом на одному рівні: 
"""
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""

        print(f'Hello {name}')

"""
Class docstrings повинні містити таку інформацію:

 --Короткий опис  мети та поведінки класу
 --Будь -які публічні методи разом з коротким описом
 --Будь -які властивості класу (атрибути)
 --Все, що стосується інтерфейсу для підкласів, якщо клас призначений для підкласизації
 
Параметри конструктора класу повинні бути задокументовані в методі класу __init__ docstring. 
Окремі методи повинні бути задокументовані з використанням їх окремих docstrings. 
Docstrings методу класу повинні містити наступне:

Короткий опис того, що це за метод і для чого він використовується
Будь -які аргументи (обов'язкові та необов'язкові), які передаються, включаючи аргументи ключового слова
Позначте всі аргументи, які вважаються необов’язковими або мають значення за замовчуванням
Будь -які побічні ефекти, що виникають під час виконання методу
Будь -які винятки
Будь -які обмеження щодо того, коли можна викликати метод

"""

class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs=4):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))


"""  
Package and Module Docstrings

Docstrings пактів слід розміщувати у верхній частині файлу __init__.py пакета. 
У цьому рядку документів має бути перелік модулів та підпакетів, які експортуються пакетом.

Docstrings модуля схожі на Docstrings класу. Замість того, щоб класифікувати класи 
та методи класів, тепер це модуль та будь -які функції, що знаходяться всередині. Docstrings 
 модуля розміщуються у верхній частині файлу навіть перед будь -яким імпортом. 
 Структурні рядки модуля повинні містити наступне:
 
 --Короткий опис модуля та його призначення
 --Список будь -яких класів, винятків, функцій та будь -яких інших об’єктів, експортованих модулем
 --Docstrings для функції модуля повинен містити ті ж елементи, що і метод класу:
    -Короткий опис того, що таке функція і для чого вона використовується
    -Будь -які аргументи (обов'язкові та необов'язкові), які передаються, включаючи аргументи ключового слова
    -Позначте всі аргументи, які вважаються необов’язковими
    -Будь -які побічні ефекти, що виникають під час виконання функції
    -Будь -які винятки
    -Будь -які обмеження щодо того, коли можна викликати функцію
"""

"""
Script Docstrings

Scripts вважаються виконуваними файлами, що запускаються з консолі. Структурні підказки для скриптів 
розміщуються у верхній частині файлу і мають бути задокументовані достатньо добре, щоб користувачі могли мати достатнє розуміння того,
як використовувати сценарій. Він повинен бути придатним для використання у повідомленні "використання", 
коли користувач неправильно передає параметр або використовує параметр -h.

If you use argparse, then you can omit parameter-specific documentation, 
assuming it’s correctly been documented within the help parameter of the argparser.parser.add_argument function. 
It is recommended to use the __doc__ for the description parameter within argparse.ArgumentParser’s constructor. 

Нарешті, будь-який власний або сторонній імпорт має бути перерахований у Docstrings, 
щоб користувачі могли знати, які пакети можуть знадобитися для запуску сценарію. Ось приклад сценарію, 
який використовується для простого роздрукування заголовків стовпців електронної таблиці:
"""
"""Spreadsheet Column Printer

This script allows the user to print to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

This tool accepts comma separated value files (.csv) as well as excel
(.xls, .xlsx) files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""

import argparse

import pandas as pd


def get_spreadsheet_cols(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is
        False)

    Returns
    -------
    list
        a list of strings used that are the header columns
    """

    file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=str,
        help="The spreadsheet file to pring the columns of"
    )
    args = parser.parse_args()
    get_spreadsheet_cols(args.input_file, print_cols=True)


if __name__ == "__main__":
    main()