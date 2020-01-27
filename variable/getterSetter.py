class Person:
    def __init__(self, age=0):
        self._age = age


    def get_age(self):
        return self._age

    def set_age(self, x):
        self._age = x

obj = Person();
obj.set_age(12);
print(obj.get_age())
