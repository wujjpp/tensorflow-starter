import itertools
from functools import reduce


def pi(N):
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    l1 = itertools.count(1)
    l2 = (x for x in l1 if x % 2 != 0)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    l3 = itertools.takewhile(lambda x: x <= (2 * N - 1), l2)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    l4 = list()
    for n, x in enumerate(l3):
        if n % 2 == 0:
            l4.append(4 / x)
        else:
            l4.append(-4 / x)
    # step 4: 求和:
    return reduce(lambda x, y: x + y, l4)


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

b = b'Hello, world!'
print(type(b))
print(b)
s = b.decode('ascii')
print(type(s))
print(s)
