import asyncio
import datetime

async def foo():
    for i in range(10):
        print("In foo: counting", i)
        await asyncio.sleep(0)

async def bar():
    for i in range(10):
        print("In bar: counting", i)
        await asyncio.sleep(0)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(foo(), bar()))
loop.close()

