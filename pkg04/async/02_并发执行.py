import asyncio


async def request_api(url):
    print(f"Starting request for {url}")
    await asyncio.gather(
        asyncio.sleep(3),
        asyncio.sleep(3),
        asyncio.sleep(3))
    print(f"finished request for {url}")


if __name__ == '__main__':
    asyncio.run(request_api("https://www.python.org"))
    print("main Finished")
