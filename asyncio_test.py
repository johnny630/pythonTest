# -*- coding: utf-8 -*-
"""
reference: https://www.jianshu.com/p/b5e347b3a17c
"""
import asyncio
import time

now = lambda: time.time()

async def do_some_work(x):
    # time.sleep(3)
    print("Waiting: ", x)
    await asyncio.sleep(x)
    print("Go: ", x)
    return 'Done after {}s'.format(x)


start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# task = loop.create_task(coroutine)
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]
# task.add_done_callback(callback)


# print(task)
loop.run_until_complete( asyncio.wait(tasks) )
# print(task)

for task in tasks:
    print('Task ret: {}'.format(task.result()))

print('TIME: ', now() - start)