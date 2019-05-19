import asyncio


async def hello():
    print("Hello world")
    await asyncio.sleep(2)
    print("Hello again!")


print('step - 1')
# 获取EventLoop:
loop = asyncio.get_event_loop()
print('step - 2')
# 执行coroutine
loop.run_until_complete(hello())
print('step - 3')
loop.close()
print('step - 4')
