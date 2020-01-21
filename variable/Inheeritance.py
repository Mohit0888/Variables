class A:

    def a(self):
        print("This is method a");
        self.p=1
        self._q=2
        self.__r=3

class B(A):

    def b(self):
        print("This is method b");


obj = B()
obj.a()
obj.b()
print(obj.p)
print(obj._q)