

list=[1,2,3,4,5,6,7,8]

def a():
    for i in list:
        print("ss",i)
        yield i

obj=a()
#print(next(obj))
#for i in obj:
 #   print(i)
