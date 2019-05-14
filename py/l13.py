class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


# 能跑的
class RunnableMixIn(object):
    def run(self):
        print('Running...')


# 能飞的
class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


# 肉食动物
class CarnivorousMixIn(object):
    pass


# 植食动物
class HerbivoresMixIn(object):
    pass


# 定义一个狗类型，动物、能跑、肉食动物
class Dog2(Animal, CarnivorousMixIn, RunnableMixIn):
    pass
