class LinearSearch:


    def search(self,list,n):

        for i in range(len(list)):
            if list[i]==n:
                return True
        return False



list = [1,2,3,4,5]
obj=LinearSearch();
result =obj.search(list,7);
if result:
    print("found")
else:
    print("not found")