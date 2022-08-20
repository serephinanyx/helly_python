class sample:
    num1=10
    num2=20

obj=sample()
print(obj.num1)
print(obj.num2)
#self:which is represent current class properties

class student:
    def display(self,fname,lname):
     print("hello")
     print("fname=",fname)
     print("lname=",lname)
obj=student()
obj.display("helly","bhatt")

