def a():

    yield 1
    yield 2
    yield 3
    yield 4

obj = a()

for i in obj:
    print(i)
