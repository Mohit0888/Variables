class Computer:

    def __init__(self):
        self.name="Mohit";
        self.id=1;

    def compare(self,other):
        if self.id==other.id:
            return  True
        else:

            return False

c1 = Computer()
c2 = Computer()

c1.id=21;
result = c1.compare(c2);

if result:
    print("They are same");
else:
    print("They are not same");

