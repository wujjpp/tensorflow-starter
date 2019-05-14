class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    pass


animal = Animal()
dog = Dog()
cat = Cat()
animal.run()
dog.run()
cat.run()
