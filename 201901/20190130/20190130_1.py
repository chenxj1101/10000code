# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-30 14:21:32
@LastEditTime: 2019-01-30 16:10:12
@Description: 30290130_1  async实例
'''

import asyncio
import aiohttp
import concurrent.futures as cofu
from os.path import basename


def download(ways):
    if not ways:
        print('Ways list is empty. Downloading is impossible')
        return
    
    print('downloading...')

    success_files = set()
    failure_files = set()

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
            async_downloader(ways, event_loop, success_files, failure_files)
        )
    finally:
        event_loop.close()

    print('Download complete')
    print('-' * 100)

    if success_files:
        print('success:')
        for file in success_files:
            print(file)

    if failure_files:
        print('failure:')
        for file in failure_files:
            print(file)

async def async_downloader(ways, loop, success_files=set(), failure_files=set()):
    async with aiohttp.ClientSession() as session:
        coroutines = [
            download_file_by_url(
                url,
                session=session,
            ) for url in ways
        ]

        completed, pending = await asyncio.wait(coroutines, return_when=cofu.FIRST_COMPLETED)
        while pending:
            for task in completed:
                fail, url = task.result()

                if fail:
                    failure_files.add(url)
                else:
                    success_files.add(url)

            completed, pending = await asyncio.wait(pending, return_when=cofu.FIRST_COMPLETED)
        
        for task in completed:
            fail, url = task.result()
            if fail:
                failure_files.add(url)
            else:
                success_files.add(url)

async def download_file_by_url(url, session=None):

    fail = True
    file_name = basename(url)

    assert session

    try:
        async with session.get(url) as response:
            if response.status == 404:
                print(f"\t{file_name} from {url} : Failed : {'404 - Not found'}")
                return fail, url
            
            if not response.status == 200:
                print(f"\t{file_name} from {url} : Failed : HTTP response {response.status}")
                return fail, url
            
            data = await response.read()

            with open(file_name, 'wb') as file:
                file.write(data)

    except asyncio.TimeoutError as err:
        print(f"\t{file_name} from {url}: Failed : {'Timeout error'}")
    
    except aiohttp.client_exceptions.ClientConnectionError as err:
        print(f"\t{file_name} from {url}: Failed : {'Client connection error'}")

    else:
        print(f"\t{file_name} from {url} : Success")
        fail = False


def test():

    ways = [
        'https://www.wikipedia.org',
        'https://www.ya.ru',
        'https://www.duckduckgo.com',
        'https://www.fail-path.unknown',
    ]

    download(ways)

if __name__ == "__main__":
    test()