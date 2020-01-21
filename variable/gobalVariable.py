a=10;

def something():
    a=5
    x=globals()['a']
    print(x);
    print(a);
something();