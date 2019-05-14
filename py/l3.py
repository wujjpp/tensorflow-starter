L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L')
print(L)

print('L[0:3]')
print(L[0:3])

print('L[:3]')
print(L[:3])

print('L[1:3]')
print(L[1:3])

print('L[2:]')
print(L[2:])

print('L[-2:]')
print(L[-2:])

print('L[-2:-1]')
print(L[-2:-1])

##########################################

L = list(range(100))
print('L')
print(L)

print('L[:10]')
print(L[:10])

print('L[-10:]')
print(L[-10:])

print('L[10:20]')
print(L[10:20])

print('L[:10:2]')
print(L[:10:2])

print('L[::5]')
print(L[::5])

print('L[:]')
print(L[:])

print('(0, 1, 2, 3, 4, 5)[:3]')
print((0, 1, 2, 3, 4, 5)[:3])

print("'ABCDEFG'[:3]")
print('ABCDEFG' [:3])


def trim(s):
    if s == '':
        return s
    else:
        # head
        while s[:1] == ' ':
            s = s[1:]

        # end
        while s[-1:] == ' ':
            s = s[:len(s) - 1]

    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')
