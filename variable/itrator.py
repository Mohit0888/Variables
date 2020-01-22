list=[1,2,3,4]

it= iter(list)

print(it.__next__())
print(it.__next__())
print("continue")

for i in it:
   print(i)