
from threading import *
from time import sleep

class A(Thread):
    def run(self):
        for i in range(556):
            print("hello")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(578):
            print("hi")
            sleep(1)

t1=A()
t2=B()

t1.start()

t2.start()