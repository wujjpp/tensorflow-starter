from functools import reduce


# 高阶函数
def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


def f(x):
    return x * x


r = map(f, range(10))
print(r)  # r是map object
print(list(r))

# map
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce
def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(char2num, s))


print(str2int('12345'))


def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, char2num(s))


print(str2int('12345'))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n)
    else:
        break
