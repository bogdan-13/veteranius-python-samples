# for the CPU-bound tasks multiprocessing module is the best fit, 
# because it is able to execute code in parallel on several cores

from time import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

COUNT = 50_000_000
WORKERS_NUMBER = 2

def countdown_sync(count):
    n = count
    while (n > 0):
        n -= 1

# threading module gives no improvement due to infamous GIL
def countdown_thread(count):
    splitted = [ count // WORKERS_NUMBER ] * WORKERS_NUMBER
    with ThreadPoolExecutor() as pool:
        pool.map(countdown_sync, splitted)

def countdown_proc(count):
    splitted = [ count // WORKERS_NUMBER ] * WORKERS_NUMBER
    with Pool() as pool:
        pool.map(countdown_sync, splitted)

if __name__ == "__main__":
    start = time()
    countdown_proc(COUNT)
    duration = time() - start
    print(f'Counted down for {duration} seconds')