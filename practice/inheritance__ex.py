data="""

           SELECT YOUR ROLE

        PRESS 1 FOR DOCTOR
        PRESS 2 FOR PAITENT
"""
print(data)
choice = int (input("Enter Your Choice : "))
if choice==1:
    class user:
   
     def __init__(self):
        print("user class")

     def input(self):
        self.email = input ("enter email:")
        self.password=input("enter password:")

    class doctor (user):
    
      def doc_input(self):
        self.specification = input("enter specification:")

      def display(self):
        print("doctor email=",self.email)
        print("doctor password=",self.password)
        print("doctor specification=",self.specification)


    doctor=doctor()

    doctor.input()
    doctor.doc_input()
    doctor.display()

elif choice==2:

    class user:
    
      def __init__(self):
        print("user class")

      def input(self):
        self.email = input ("enter email:")
        self.password=input("enter password:")

    class Patient (user):
      def patient_input(self):
        self.bloodgroup = input("enter bloodgroup:")

      def display(self):
        print("patient email=",self.email)
        print("patient password=",self.password)
        print("patient bloodgroup=",self.bloodgroup)
    obj=Patient()

    obj.input()
    obj.patient_input()
    obj.display()

