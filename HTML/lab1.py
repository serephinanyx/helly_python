f_name=input("please enter your name:")

if f_name=="":
    print("you did not enter any character.")
elif len(f_name.title())==1:
 print("there is",len(f_name),"letter in",f_name)

elif f_name.isalpha():
 for index,letter in enumerate(f_name.title(),1):
  print(index,"",letter)
 print("there are",len(f_name),"letter in",f_name)

elif f_name.isalnum():

    print("Non alphabetic character were entered")
else:
    f =filter(str.isalpha,f_name)
    str1="".join(f)
    print(str1)
    for index,letter in enumerate(f_name.title(),1):
        print(index,":",letter)
    print("There are ",len(str1),"letters in" ,f_name.title())


