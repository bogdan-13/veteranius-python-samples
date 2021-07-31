"""
Маємо асинхронну функцію display_date, що приймає число-індентифікатор та цикл подій.
Функція має нескінченний цикл, що переривається через 50 секунд. Але поки 50 секунд не минуло,
вона друкує час і засинає на випадкову кількість секунд.
Ключове слово await вказує, що під час виконання функції,
що стоїть після нього, можна перемкнутися на іншу асинхронну функцію.
Додаємо функції до циклу подій за допомогою функції ensure_future.
"""

import asyncio
import datetime
import random


async def my_sleep_func():
    await asyncio.sleep(random.randint(0, 5))


async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print(f'Loop: {num} Time: {datetime.datetime.now()}')
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()

loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
