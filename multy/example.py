import asyncio

async def our_func():
    for i in range(5):
        await new_func()
        print(f"Our running {i}")


async def new_func():
    for i in range(5):
        await asyncio.sleep(1)
        print(f"New running {i}")



async def main():
    print('Hello ...')
    await our_func()
    print('... World!')

asyncio.run(main())