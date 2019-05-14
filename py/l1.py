import math

##################################################


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-199))

##################################################
# return mutil results


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(0, 0, 100, math.pi / 2)
x, y = r
print(r)
print(x, y)

##################################################


def pow2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


##################################################
def quadratic(a, b, c):
    x = (-b + math.sqrt(pow2(b) - 4 * a * c)) / (2 * a)
    y = (-b - math.sqrt(pow2(b) - 4 * a * c)) / (2 * a)
    return x, y


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


##################################################
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Jane', 'F')
enroll('Jack', 'M', city='Suzhou')
enroll('Lina', 'F', city='SZ', age=10)


###################################################
def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


###################################################
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))


def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc2(1, 2, 3))
print(calc2(1, 3, 5, 7))

nums = [1, 2, 3]
print(*nums)
print(calc2(*nums))
x, y, z = nums
a, b, c = (4, 5, 6)
print(x, y, z)
print(a, b, c)
