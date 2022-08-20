
import faculty,student
 
f = faculty.facultyclass()
s= student.studentclass()


# print(f.name)
# print (s.name)
# f.createfaculty("helly","h@gmail.com","787878","python","ahmedabad")

# print(f.name)
# print(f.contact)
 
# s.createstudent("helly","h@gmail.com","787878","python","66","5000")
# print(s.fees)
# print(s.marks)

# Status=True

# while Status:
#     fname= input("enter faculty name:")
#     subject=input("enter faculty subject:")
#     mobile=input("enter number")
#     city=input("enter city")
#     email=input("enter email")

#     f.createfaculty(fname,email,mobile,city,subject)
#     choice = input("do you want  more details press 'y' for yes and 'n' for no:")

#     if choice=='y':
#         status=True
#     else:
#         status=False
Status=True

while Status:
    fname= input("enter faculty name:")
    subject=input("enter faculty subject:")
    mobile=input("enter number:")
    
    email=input("enter email:")
    marks=input("enter marks:")
    fees=input("enter fees:")
    s.createstudent(fname,email,mobile,marks,subject,fees)
    choice = input("do you want  more details press 'y' for yes and 'n' for no:")

    if choice=='y':
        status=True
    else:
        status=False



