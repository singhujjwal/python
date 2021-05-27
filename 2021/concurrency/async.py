#!/home/centos/p38/bin/python
import asyncio

async def print_after(delay: int, what: str) -> None :
    await asyncio.sleep(1)
    print (what)


async def run_print():
    task = asyncio.create_task(print_after(4, 'Hi There...'))
    await task

async def run_factorial():
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 5),
        factorial("C", 11)
    )


def main():
    print ("This is main function")
    asyncio.run(print_after(2, 'Ujjwal'))
    asyncio.run(run_print())
    asyncio.run(run_factorial())

async def factorial(name: str, number: int):
    f = 1
    for i in range(2, number + 1):
        print (f"Task {name}: Compute Factorial({number}), Currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print (f"Task {name}: factorial({number}) = {f}")
    return f





if __name__ == '__main__':
    main()