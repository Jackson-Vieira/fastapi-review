# chapar pao
# fritar hamburger
# montar sanduiche
# fazer milkshake

# sync

import asyncio
import time

st = time.time()

event_loop = asyncio.new_event_loop()

async def cook_bread():
    await asyncio.sleep(2)
    
async def cook_hamburger():
    await asyncio.sleep(2)

async def make_milkshake():
    await asyncio.sleep(2)

async def mount_sandwich():
    await asyncio.sleep(2)

async def make_sandwich():
    await asyncio.gather(
        cook_bread(),
        cook_hamburger(), 
    )
    event_loop = asyncio.get_running_loop()
    event_loop.create_task(mount_sandwich())

async def cook():
    await asyncio.gather(
        make_milkshake(),
        make_sandwich()
    )

asyncio.run(cook())
et = time.time()

print('Async Execution time:', (et-st), 'seconds')