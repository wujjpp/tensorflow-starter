import os

try:
    f = open('io1.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()

print('')

with open('io1.py', 'r') as f1:
    print(f1.read())

with open('test-tmp.txt', 'w') as fw:
    fw.write('Hello world')

with open('test-tmp.txt', 'r') as fr:
    print(fr.read())


os.remove('test-tmp.txt')
