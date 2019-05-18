import time
from datetime import datetime


def odd():
    print('step - 1')
    yield 1
    print('step - 2')
    yield 3
    print('step - 3')
    yield 5


print(datetime.now(), 'create generator')
g = odd()
print(datetime.now(), 'generator created')
print(datetime.now(), 'waiting for 2 seconds then next')
time.sleep(2)
print(datetime.now(), 'execute next')
n = next(g)
print(n)
print(datetime.now(), 'waiting for 2 seconds then next')
time.sleep(2)
print(datetime.now(), 'execute next')
n = next(g)
print(n)
print(datetime.now(), 'waiting for 2 seconds then next')
time.sleep(2)
print(datetime.now(), 'execute next')
n = next(g)
print(n)
time.sleep(2)
print('done')
