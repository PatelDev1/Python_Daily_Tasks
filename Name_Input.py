class Sample:

    def __int__(self,fn,ln):
        self.a=fn
        self.b=ln

    def __str__(self):
        return self.a+" "+self.b

fname=input("Enter Name: ")
iname=input("Enter Surname: ")

obj=Sample(f.name,lname)
print(obj)
