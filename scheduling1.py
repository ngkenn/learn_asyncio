import asyncio
import time


start=time.time()


# Return a string with 'at {current time}'
def progtime():
    return 'at %1.1f seconds' % (time.time()-start)


# Random task 1
async def f1():
    print('f1 started: {}'.format(progtime()))
    await asyncio.sleep(3)  # Block this coroutine for 3 seconds
    print('f1 finished: {}'.format(progtime()))


# Random task 2
async def f2():
    print('f2 started: {}'.format(progtime()))
    await asyncio.sleep(3)  # Block this coroutine for 3 seconds
    print('f2 finished: {}'.format(progtime()))

# Random task 3
async def someothertask():
    print("beep bop beep: {}".format(progtime()))
    await asyncio.sleep(2)  # Block this coroutine for 2 seconds
    print("the beep was bopped. {}".format(progtime()))


async def main():
    tasks=[f1(),f2(), someothertask()]
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
