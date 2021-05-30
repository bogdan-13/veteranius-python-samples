# Асоціація

# Крім успадкування, існує й інший спосіб організації міжкласової взаємодії - асоціація (агрегація або композиція), при якій один клас є полем іншого.
# Приклад композиції:

class Salary:
    def __init__(self,pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay*12)

class Employee:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)

    def annualSalary(self):
        return "Total: " + str(self.salary.getTotal() + self.bonus)

employee = Employee(100,10)
print(employee.annualSalary())

# Приклад агрегацiї:

class Salary(object):
    def __init__(self, pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay * 12)

class Employee(object):
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return "Total: " + str(self.pay.getTotal() + self.bonus)

salary = Salary(100)
employee = Employee(salary, 10)
print(employee.annualSalary())

# Асоційовані об'єкти можуть циклічно посилатися один на одного, що ламає стандартний механізм збору сміття.
# Уникнути подібних проблем при асоціації допомагають слабкі посилання (модуль weakref).