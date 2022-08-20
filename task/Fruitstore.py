Fruits ={}

menu = """
        
                            PRESS 1 FOR ADD FRUITS
                        
                            PRESS 2 FOR VIEW FRUIT
        
                            PRESS 3 FOR PURCHASE FRUIT
                           
                            PRESS 4 FOR EXIT
"""
Status = True
while Status:

    print(menu)
    Specifications = {}
    choice = int (input("Enter Your Choice : "))
     choice==1:
try:
        fruit_name = input("Enter Fruit name : ")
        qty = int(input("Enter qty of fruit : "))
        price = int(input("Enter price of fruit : "))

        Specifications['qty']=qty
        Specifications['price']=price
        Fruits[fruit_name]=Specifications
try: choice==2:
        for k in Fruits.keys():
            print("---------------------------------------")
            print(f"Fruit Name : {k}")
            print(f"Fruit Qty : ",+Fruits[k]["qty"])
            print(f"Fruit Price : ",+Fruits[k]["price"])

try choice==3:
        for k in Fruits.keys():
            print("---------------------------------------")
            print(f"Fruit Name : {k}")
            print(f"Fruit Price : (for 5 piece)",+Fruits[k]["price"])

    fruit_name = input("Enter fruit which you want to purchase : ")
    if fruit_name in Fruits.keys():
        qty = int(input("Enter no of quantity you want: "))

        price = qty * Fruits[fruit_name]["price"]
        print("PRICE = ",price)
finally: choice==4:
        Status=False
        break
    user_choice= input("Do you want to continue ? press 'y' for yes and press 'n' for no : ")
    if user_choice== 'n':
        Status=False

    else:
        Status=True