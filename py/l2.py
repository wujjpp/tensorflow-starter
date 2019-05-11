# 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass

    print('name:', name, 'age:', age, 'other:', kw)


person('Jane', 20)
person('Jack', 20, city='Suzhou', job='Test')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)


# 关键字参数
def person2(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)


person2('Jack', 24, city='SuZhou', job='Test')

# 关键字参数调用必须命名，下面代码将抛出异常
# person2('Jack', 24, 'Suzhou', 'Job')
# 如果函数定义中已经有了一个可变参数(*args)，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了


def person3(name, age, *args, city, job):
    print(name, age, args, city, job)


person3('Jack', 24, 'test1', 'test2', city='suzhou', job='test')


# 组合使用
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}

f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}

f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}

f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(10))


# 尾递归 - Python不支持
def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(5))


# 汉诺塔: a:原始柱子, b:辅助柱子, c:目标柱子
def move(n, a, b, c):
    if n == 1:
        print(a, ' --> ', c)
    else:
        move(n - 1, a, c, b)  # 把A柱上的n-1个珠子借助C,移到B柱 
        move(1, a, b, c)  # 把A柱上第n的珠子移到C柱
        move(n - 1, b, a, c)  # 把B柱上n-1个珠子借助A柱，移到C柱


move(3, 'A', 'B', 'C')
