# -*- coding:utf8 -*-
import asyncio


async def visit_url(url, time):
    print(f'start visiting {url}')
    await asyncio.sleep(time)
    print(f'finished visiting {url}')


async def main():
    task1 = asyncio.create_task(visit_url('https://www.python.org', 3))
    task2 = asyncio.create_task(visit_url('https://www.google.com', 3))
    task3 = asyncio.create_task(visit_url('https://www.github.com', 3))
    await task1
    await task2
    await task3
    print('all tasks finished')


if __name__ == '__main__':
    asyncio.run(main())
