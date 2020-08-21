class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()


cat = Cat()
cat.run()
Animal()

def run_twice(animal):
    animal.run()


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


class Timer(object):
    def run(self):
        print('Start...')

run_twice(Tortoise())
run_twice(Timer())