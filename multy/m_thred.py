import concurrent.futures
from concurrent.futures.thread import ThreadPoolExecutor

import requests
import time

url = 'https://en.wikipedia.org/wiki/Political_impact_of_the_COVID-19_pandemic'




def req(url=url):

    print("starting")
    r = requests.get(url)
    print("ending")
    return r


tasks = [url for x in range(100)]


if __name__ == "__main__":
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=100) as executor:
        pool = [executor.submit(req, url) for x in range(100)]
        for result in concurrent.futures.as_completed(pool):
            print(result.result())

    print(time.time() - start_time)