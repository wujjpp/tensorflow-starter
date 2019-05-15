class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25

        raise AttributeError('\'Student\' object has no attribute \'%s\'' %
                             attr)


student = Student()
print(student.name)
print(student.score)
print(student.age())


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


class Student2(object):
    def __init__(self):
        self.name = 'Jane'

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student2()
s()

print(callable(Student()))  # False
print(callable(Student2()))  # True
print(callable(max))  # True
print(callable([1, 2, 3]))  # False
print(callable(None))  # False
print(callable('abc'))  # False
