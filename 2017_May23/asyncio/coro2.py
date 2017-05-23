import asyncio
import datetime

async def testfn(name, count):
    for i in range(count):
        print("In {}: counting {}".format(name, count))
        await asyncio.sleep(0)

loop = asyncio.get_event_loop()
loop.run_until_complete(
         asyncio.gather(
             testfn("foo", 10),
             testfn("bar", 20),
             testfn("baz", 15)))

loop.close()

