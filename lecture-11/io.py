from requests import get
from time import time
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import asyncio
import aiohttp

# Get http://olympus.realpython.org/dice 80 times
URL = 'http://olympus.realpython.org/dice'
TIMES = 80

def get_url(url):    
    response = get(url)
    print(f'Read {len(response.content)} from {url}')

# Sync version
def get_urls_sync(urls):
    for index, url in enumerate(urls):
        get_url(url)

# Processing version
# massive improvement in comparison to sync version
def get_urls_proc(urls):
    with Pool() as pool:
        pool.map(get_url, urls)

# Threading version
# improvement in comparison to multiprocessing version, because thread is lighter than process
def get_urls_thread(urls):
    with ThreadPoolExecutor() as pool:
        pool.map(get_url, urls)

# Asyncio version
# improvement in comparison to threading version, because only 1 thread is needed to event loop to run
def get_urls_async(urls):
    async def get_url(session, url):
        async with session.get(url) as response:
            html = await response.text()
            print(f'Read {len(html)} from {url}')

    async def internal_get():
        async with aiohttp.ClientSession() as session:
            tasks = map(lambda url: get_url(session, url), urls)
            await asyncio.gather(*tasks)

    asyncio.run(internal_get())

    
if __name__ == '__main__':
    urls = [ URL ] * TIMES
    start = time()
    get_urls_async(urls)
    duration = time() - start
    print(f'\nLoaded {URL} {TIMES} times in {duration} seconds')