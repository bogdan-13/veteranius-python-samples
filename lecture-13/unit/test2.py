#Виконуємо тестування чесно спізженого класу кальнулятора юніт-тестом
#тут ми додали пропуск одного тесту за допомогою декоратора skip()
import unittest
from main import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    @unittest.skip("цей тест ми скіпаємо, бо нам хочеться!")
    def test_add(self):
        self.assertEqual(self.calculator.add(4,7), 11)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10,5), 5)

    @unittest.skipIf(7 > 1, "а тут невірна умова!")
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3,7), 21)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10,2), 5)


if __name__ == "__main__":
    unittest.main()