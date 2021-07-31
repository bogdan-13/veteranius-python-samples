import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print(f'Воркер {number} спав {sleep} секунд')


for i in range(10):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()

print('Потоки запущено, чекаємо виконання')
