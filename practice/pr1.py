# EXCEPTION:"""


try:
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))

    ans=num1/num2
    
except ZeroDivisionError:
    print("make sure entered number is greater than 0")
except:
    print("invalid input")
else:
     print(ans)
finally:
    print("THANKYOU FOR USING THIS APP")
   
   
   
   
  #  """
    # try: which contain error block

    # except: which call when errror occurs

    # finally: it always execute whether there is an exception or not

    # else: it always execute when there is no exception
    


