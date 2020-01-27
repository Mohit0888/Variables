class Foo:
    def __init__(self):
        print('__init__ called')
    def __enter__(self):
        print('__enter__ called')
        return self
    def __exit__(self, *a):
        print('__exit__ called')

myobj = Foo()

print('\nabout to enter with 1')
with myobj:
    print('with 1')

print('\nabout to enter with 2')
with myobj:
    print('with 2')