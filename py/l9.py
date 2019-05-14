import functools
import time


def now():
    print('2019-05-13')


print(now.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now2():
    print('2019-05-13')


print(now2.__name__)
now2()


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log2('execute')
def now3():
    print('2019-05-13')


print(now3.__name__)
now3()


def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log3
def now4():
    print('2019-05-13')


print(now4.__name__)
now4()


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log4('execute')
def now5():
    print('2019-05-13')


print(now5.__name__)
now5()


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        t = (end - start) * 1000  # convert to ms
        print('%s executed in %s ms' % (func.__name__, t))
        return result

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

int2 = functools.partial(int, base=2)
print(int2('1000000'))
