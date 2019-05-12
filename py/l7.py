from collections import Iterable
from collections import Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance(100, Iterator))

print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))


def iter2(args):
    for x in args:
        yield x


print(isinstance(iter2([]), Iterator))
print(isinstance(iter2('abc'), Iterator))
