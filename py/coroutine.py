from datetime import datetime
import time


def log(*args):
    params = list()
    params.append('[')
    params.append(datetime.now())
    params.append('] :')
    for x in args:
        params.append(x)
    print(*params)


def consumer():
    log('consumer - 1')
    r = 'First None'
    log('consumer - 2')
    while True:
        log('consumer - 3')
        n = yield r
        log('consumer: n =', n)
        log('consumer - 4')
        if not n:
            log('consumer - 5')
            return

        log('consumer - 6')
        print('[CONSUMER] Consuming %s...' % n)
        log('consumer - 7')
        r = '200 OK'


def produce(c):
    log('produce - 1')
    r1 = c.send(None)
    log('produce: r1 =', r1)
    log('produce - 2')
    n = 0
    log('produce - 3')
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
# print(c)
# print(type(c))
# print(dir(c))
produce(c)
