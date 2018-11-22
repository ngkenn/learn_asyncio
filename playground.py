import asyncio


async def f1():
    print('In F1')
    await asyncio.sleep(0)
    print('Switched to f1')


async def f2():
    print('In F2')
    await asyncio.sleep(0)
    print('Switched to f2')


async def main():
    tasks = [f1(), f2()]
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
