print('Обчислення суми чисел від 1 до n') # Виводимо на екран повідомлення що робить програма
summ = 0  # Ініціюємо змінну в якій будемо зберігати результат (суму)
count = 1  # Ініціюємо змінну в якій будемо зберігати лічильник ( поточне число яке плюсується до суми попередніх)
n = int(input("Введіть n= "))  # Запитуємо у користувача число до якого будемо рахувати суму та перетворюємо в в число
while count <= n: # Ініціюємо цикл доки змінна count не перевищить змінну n
    summ = summ + count  # На кожній ітераціїї суму попередніх чисел збільшуємо на число зі змінної count
    count += 1  # Збільшуємо лічильник (поточне число) на 1 це можна зробити також так: count = count + 1
print("Сума чисел 1 + 2 + ... +", n, " = ", summ)  # Виводимо результат на екран
