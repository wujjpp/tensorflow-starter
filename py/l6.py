L = [x * x for x in range(10)]
print(L)

print('#################################################')
k = (x * x for x in range(10))
print(next(k))
print(next(k))
print(next(k))

print('#################################################')
print()
g = (x * x for x in range(10))
for n in g:
    print(n)

print('#################################################')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(10)

print('##################################################')


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib2(10):
    print(n)

print('##################################################')


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


o = odd()
print(next(o))
print(next(o))
print(next(o))

print('##################################################')
g = fib(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print('##################################################')

print('杨辉三角')


def triangles():
    last = [1]

    while True:
        yield last
        results = []
        # n > 0 && n < len(l)
        for n in range(1, len(last)):
            results.append(last[n - 1] + last[n])
        results.insert(0, last[0])
        results.append(last[len(last) - 1])
        last = results


results = []
n = 0
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

if results == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],
               [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1],
               [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1],
               [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]:
    print('测试通过!')
else:
    print('测试失败!')
