class A:

    def __init__(self):
        self.a=1;
        self.b=0;

    def aa(self):
        try:
            print(self.a/self.b);
        except Exception as e:
            print("zero in denominator is not alowd" , e);

obj = A();
obj.aa();
