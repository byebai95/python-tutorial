import asyncio
import time


async def test():
    print("test begin")
    await asyncio.sleep(3)
    await say()
    print("test finished")


async def say():
    time.sleep(3)
    print("say hello")


test()
