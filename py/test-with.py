class Foo(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print('hello %s' % self.name)
        raise ValueError('TestError')

    def __enter__(self):
        print('__enter__ called')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('---------__exit__  start---------')
        print('__exit__ called')
        print('--------------------------------')
        print(exc_type)
        print('--------------------------------')
        print(exc_value)
        print('--------------------------------')
        print(traceback)
        print('---------__exit__  end---------')


with Foo('Jane') as foo:
    foo.say()
