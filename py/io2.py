from io import StringIO
from io import BytesIO

s1 = StringIO()

s1.write('hello')
s1.write(' ')
s1.write('world')
s1.write('!')
print(s1.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f1 = BytesIO()
f1.write('中文'.encode('utf-8'))
print(f1.getvalue())

f2 = BytesIO(f1.getvalue())
print(f2.read())
f2.seek(0)
b = f2.read()
print(b.decode('utf-8'))
