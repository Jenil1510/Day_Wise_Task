import asyncio
print("The text will be print after the delay")
async def hello_after_delay(delay):
    await asyncio.sleep(delay)
    print("i am learning the python")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_after_delay(5))
loop.close()