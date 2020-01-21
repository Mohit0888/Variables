def add(x,y):
    c=x+y;
    print(c);

add(5,3)


def update(list):
    print(id(list))
    list[1]=24;
    print(id(list))
    print(list);

list=[2,3,4,5]
print(list)
update(list);
print(list)

