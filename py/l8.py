from functools import reduce
from operator import itemgetter


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

DIGITS = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}


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

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students, key=itemgetter(0)))  # 按名字升序
print(sorted(students, key=lambda t: t[1]))  # 按分数升序
print(sorted(students, key=itemgetter(0), reverse=True))  # 按名字倒序


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def createCounter():
    current = 0

    def counter():
        nonlocal current
        current = current + 1
        return current
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
