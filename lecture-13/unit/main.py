# В нас є клас кальнулятор, ніразу не вкрадений з простору інтернету, вірте мені!
class Calculator:
    # ініціалізація
    def __init__(self):
        pass

    # додавання
    def add(self, x1, x2):
        return x1 + x2

    # множення
    def multiply(self, x1, x2):
        return x1 * x2

    # віднімання
    def subtract(self, x1, x2):
        return x1 - x2

    # ділення
    def divide(self, x1, x2):
        if x2 != 0:
            return x1 / x2

