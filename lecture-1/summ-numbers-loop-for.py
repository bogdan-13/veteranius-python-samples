print('Обчислення суми чисел від 1 до n')  # Виводимо на екран повідомлення що робить програма
summ = 0  # Ініціюємо змінну в якій будемо зберігати результат (суму)
n = int(input("Введіть n = "))  # Запитуємо у користувача число до якого будемо рахувати суму та перетворюємо в в число
for count in range(1, n + 1):  # Ініціюємо цикл по змінній count від 1 до n
    summ = summ + count  # На кожній ітераціїї суму попередніх чисел збільшуємо на число зі змінної count
print("Сума чисел 1 + 2 + ... +", n, " = ", summ)  # Виводимо результат на екран
