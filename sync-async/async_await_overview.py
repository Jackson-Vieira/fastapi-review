import asyncio

# EVENT LOOP (orquestrador de funcoes assincronas)
# ASYNC FUNCTION -> async def function_name

async def sum(a, b):
    return a + b

async def print_sum(a, b):
    return print(f'resultado igual a {await sum(a, b)}')

event_loop = asyncio.new_event_loop()


event_loop.run_until_complete(print_sum(4, 3))
