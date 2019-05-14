import types

print(type(123))
print(type('abc'))
print(type(None))
print(type(abs))
print(type(123) == int)
print(type('abc') == str)

print(dir(types))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x * x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print(dir('ABC'))


class MyDog(object):
    def __len__(self):
        return 100


mydog = MyDog()
print(len(mydog))


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(obj.y)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(getattr(obj, 'z', 404))


class Student(object):
    count = 0

    def __init__(self, name):
        Student.count += 1
        self.name = name


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
