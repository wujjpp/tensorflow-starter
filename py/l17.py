from hello import Hello

h = Hello()
h.hello()

print(type(h))
print(type(Hello))


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello2 = type('Hello2', (object, ), dict(hello=fn))

h2 = Hello2()
print(type(h2))
print(type(Hello2))
