class A:

    def execute(self):
        print("hello");

class B:

    def execute(self):
        print("World");

class C:
    def print(type):
        type.execute();

objC= C();
objA= A();
objB= B();
objC.print(objA);
objC.print(objB);