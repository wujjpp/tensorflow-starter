from contextlib import contextmanager, closing
from urllib.request import urlopen


########################################################
class Query1(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query1('Bob') as q:
    q.query()


##########################################################
class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()


##########################################################
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

##########################################################
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
