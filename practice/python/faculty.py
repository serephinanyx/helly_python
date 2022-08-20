


class facultyclass:
 name =""
 email =""
 contact=""
 city=""
 subject=""
 
 dict={}

 def createfaculty(self,firstname,email,contact,subject,city):
   innerdict={}
   self.name=firstname
   self.email=email
   self.subject=subject
   self.number=contact
   self.city=city

   innerdict['email']=self.email
   innerdict['subject']=self.subject
   innerdict['number']=self.number
   innerdict['city']=self.city
   self.dict['firstname']=innerdict
   print(self.dict)



 #def createfaculty(self,name,email,number,subject,city):
    #self.name=name
    #self.email=email
    #self.subject=subject
    #self.contact=number
    #self.city=city

   