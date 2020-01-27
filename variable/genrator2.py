#This is normal fun which return list
lis=[1,2,3,4]
def a():
    my_list=[]
    for i in lis:
        my_list.append(i*i)
    return my_list

result = a()
print(result)


#This is the fun which uses genrator
#yield return the Genrator Object which we can iterator further
#it also saves the memory as we do not have to create the other list as we have created in the above EXAMPLE
lis2=[5,6,7,8]

def b():

    for i in lis2:
        yield i*i


result2 =b()
print(list(result2))
