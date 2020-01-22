pos=0
def search(list,n):
    l=0
    u=len(list)-1
    while l <=u:
        mid= l+u // 2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False



list=[12,33,44,55,66,77]
result=search(list,77)
if result:
   print("found on pos",pos+1)
else:
   print("not found")
