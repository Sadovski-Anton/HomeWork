import asyncio


async def foo(j):
    for i in range(10):
        print(j, i)
        await  asyncio.sleep(1)


async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(foo(i)))

    await  asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
