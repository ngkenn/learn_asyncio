import asyncio
import random
from time import sleep
import time

# Methods defining synchronous and asynchronous tasks respectively

def task(taskNumber):
    # Synchronous task
    # Sleep for a random amount of time
    sleep(random.randint(0,2)*0.001)
    print("Task %s finished" % taskNumber)


async def task_coro(taskNumber):
    # Asynchronous task (coroutine)
    # Sleep for a random amount of time
    await asyncio.sleep(random.randint(0,2) * 0.001)
    print('Task %s finished' % taskNumber)


# Methods creating the tasks

def synchronous():
    for i in range(1,10):
        task(i)


async def asynchronous():
    tasks=[task_coro(i) for i in range(1,10)]
    await asyncio.gather(*tasks)


# Start synchronous tasks. Print the length of time taken in seconds
print("Synchronous tasks:")
syncStart = time.time()
synchronous()
syncEnd = (time.time())-syncStart
print("Synchronous End: %s s" % syncEnd)

# Start asynchronous tasks. Print the length of time taken in seconds
print("\nAsynchronous tasks:")
asyncStart = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(asynchronous())
asyncEnd = (time.time())-asyncStart
print("Asynchronous End: %s s" % asyncEnd)



