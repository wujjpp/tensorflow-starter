import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{ name: %s, age: %d }' % (self.name, self.age)


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name, age):
    # 绑定ThreadLocal的student:
    local_school.student = Student(name, age)
    process_student()


t1 = threading.Thread(target=process_thread,
                      args=('Alice', 25),
                      name='Thread-A')

t2 = threading.Thread(target=process_thread, args=('Bob', 26), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
