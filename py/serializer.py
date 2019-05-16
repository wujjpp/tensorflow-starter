from io import BytesIO
import pickle
import json

ms = BytesIO()
d = dict(name='Bob', age=20, score=88)

# 二进制序列化
pickle.dump(d, ms)

ms.seek(0)
dump = ms.read()
print(dump)

ms.seek(0)
# 二进制反序列化
d2 = pickle.load(ms)
print(d2)

# JSON
str = json.dumps(d)
print(str)
d3 = json.loads(str)
print(d3['name'])

print('---------------------对象序列化-------------------------')


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'name: %s, age: %s, score: %s' % (self.name, self.age,
                                                 self.score)


def student2dict(std):
    return {'name': std.name, 'age': std.age, 'score': std.score}


s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
s2 = json.loads(json_str, object_hook=dict2student)
print(s2)

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
# True: {"name": "\u5c0f\u660e", "age": 20}
# False: {"name": "小明", "age": 20}
