import asyncio

async def delay(delay_second: int) -> int:
    print(f'засыпаю на {delay_second} с')
    await asyncio.sleep(delay_second)
    print(f'сон в течение {delay_second} с закончился')
    return delay_second
