from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key, d[key])

for ch in 'ABC':
    print(ch)

########################################

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


########################################
def findMinAndMax(L):
    if not isinstance(L, Iterable):
        raise ('Not Iterable')

    if len(L) == 0:
        return (None, None)

    min = L[0]
    max = L[0]

    for val in L:
        if min > val:
            min = val
        elif max < val:
            max = val

    return (min, max)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
