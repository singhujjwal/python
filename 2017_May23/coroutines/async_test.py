import asyncio

async def slow_operation(n):
    print("Slow operation {} started".format(n))
    await asyncio.sleep(1)
    print("Slow operation {} complete".format(n))


async def main():
    print("main: awaiting slow operations...")
    await asyncio.wait([
        slow_operation(1),
        slow_operation(2),
        slow_operation(3),
    ])
    print("main: complete.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
