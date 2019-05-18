from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
point = Point(1, 2)
print('%s, x = %s, y = %s' % (point, point.x, point.y))

print('isinstance(point, Point)=%s, isinstance(point, tuple)=%s' %
      (isinstance(point, Point), isinstance(point, tuple)))

Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(10, 10, 100)
print(circle)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q)
q.popleft()
print(q)

dic = defaultdict(lambda: 'N/A')
dic['k1'] = 'val1'
dic['k2'] = 'val2'
print('k1 = %s, k2 = %s, k3 = %s' % (dic['k1'], dic['k2'], dic['k3']))

d = dict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
# dict的Key是无序的
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# OrderedDict的Key是有序的，注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
print(od)


# 利用OrderedDict构建可配置容量的FIFO容器
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


counter = Counter()
for ch in 'programming':
    counter[ch] = counter[ch] + 1

print(counter)