import requests
import time
import asyncio
url = 'https://en.wikipedia.org/wiki/Political_impact_of_the_COVID-19_pandemic'


async def req(url=url):
    print("starting")
    r = requests.get(url)
    print("ending")
    return r


tasks = []


async def main():
    for i in range(100):
        tasks.append(asyncio.create_task(req()))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(time.time() - start_time)