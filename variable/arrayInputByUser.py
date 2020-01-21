from _ast import arg
from array import *

arr =array('i',[])

n=int(input("Enter the length of the array"))

for i in range(n):
    x= int(input("Enter the Number"))
    arr.append(x)

print(arr)