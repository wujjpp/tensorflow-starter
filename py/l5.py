print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

##############################################################

import os
print([d for d in os.listdir('.')])


y = 'alais'

d = {'x': 'A', y: 'B', 'z': 'C'}
for k, v in d.items():
    print(k, ' = ', v)

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

###############################################################
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [v.lower() for v in L1 if isinstance(v, str) ]

print(L2)

if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
