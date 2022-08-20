data ="""
          Welcome to Amazing Pizza and Pasta Pizzeria

press 1 : Order menu
press 2 : Exit

"""
menu="""             1 large pizza = 10.99 AUD 

                     2 large Pizzas = 20.99 AUD 

                     3 Large Pizzas = 29.99 AUD

                     **Buy 4 or more pizza and get 1.5lt of soft drink free**


                    1 large pasta = 9.5 AUD 

                    2 large pastas = 17.00 AUD 

                    3 large pastas = 27.50 AUD

                    **Buy 4 or more pastas and get 2 bruschetta free.**

                    ***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free."""

print(data)
class pizzeria1:
   choice=int(input("which pizza do you want to choose:"))
   if choice==1:
    
    
    class pizzeria:
        name = input("Enter Your Name :")
        def setName(self,name):
        
            self.name = name

        def getName(self):
         return self.name
   obj = pizzeria()
   print("WELCOME",obj.getName())

choice=int(input("Enter Your Choice here:"))
if choice==1:
                print(menu)                             
elif choice==2:
     exit()
def pizza():
    
      pizza=input("enter the name of pizza you want")
      
      if pizza==1:
        print("1 large pizza=10.29AUD")
      elif pizza==2:
        print("2 large pizza=20.99AUD")
      elif pizza==3:
        print("3 large pizza=30.99AUD")

choice = int(input("Enter number of pizza order you want :"))
if choice>=4:
        print("* Congratulations !! 1.5lt softdrink free * ") 
else:
        print("your pizza order amount is",choice)
obj = pizzeria1()

obj = pizza()

def pasta():
    choice = int(input("Enter number of pasta order you want :"))
    if choice>=6:
        print("""
        * Congratulations !! get 2 bruschetta free * 

		* Congratulations !! get 2 chocco brownies ice cream free * """) 
    else:
        print("your pizza order amount is",choice)

obj = pasta()