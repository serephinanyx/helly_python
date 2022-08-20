from secrets import choice
from telnetlib import STATUS
from unicodedata import name


data="""
            Welcome to Amazing Pizza and Pasta Pizzeria

                press 1 : order menu

                 press 2 : Exit

"""
class pizzeria:
    
        choice=int(input("what do you want to order:"))
        if choice==1:
            
            print("1 large pizza = 10.99 AUD" )

            print("2 large Pizzas = 20.99 AUD")

            print("3 Large Pizzas = 29.99 AUD")

            print("***Buy 4 or more pizza and get 1.5lt of soft drink free***")
           
            print("-------------------------------------------------------------------------")
           
            print("1 large pasta = 9.5 AUD" )

            print("2 large pastas = 17.00 AUD" )

            print ("3 large pastas = 27.50 AUD ")           

            print("***Buy 4 or more pastas and get 2 bruschetta free.***")

            print("***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.")
           
            print("----------------------------------------------------------------------------")
         
        def setname(self,name):
            name=input("enter your name:")
            self.name=name
        def getname(self):
            return self.name
        def order_menu(self,order_no):
            STATUS:True
            while STATUS:
                order_no=int(input("enter no. of pizza you want:"))
                print(" *** Congratulations !! 1.5lt softdrink free ***")
                
            

            

obj=pizzeria()
obj.setname(name)
print("WELCOME",obj.getname())
          
   
        