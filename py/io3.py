import os

print(os.name)

print(os.uname())

print(os.environ)

print(os.environ.get('PATH'))

print(os.path.abspath('.'))

print(os.path.join('/Users/JP', 'tensorflow'))

print(os.path.split('/Users/JP/tensorflow/file.txt'))

print(os.path.splitext('/path/to/file.txt'))

print(os.path.dirname('/Users/JP/a.txt'))

p = os.path.join(os.path.abspath('.'), '..', '..')

print(p)

print([x for x in os.listdir(p) if os.path.isdir(os.path.join(p, x))])
