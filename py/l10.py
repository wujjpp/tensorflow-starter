import utils
from my_mods import utils as utils2
import sys

import student as stu

utils.hello('Jane')
utils2.hello2('Jack')

print(sys.path)

student1 = stu.Student1('Jane', 90)
student1.print_score()
student1.score = 100
student1.print_score()

student2 = stu.Student2('Jack', 90)
student2.print_score()
student2.set_score(99)
student2.print_score()
print(student2._Student2__score)  # 强烈不建议这么干啊

bart = stu.Student3('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
