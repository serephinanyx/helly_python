class studentclass:
 name =""
 email =""
 contact=""
 
 subject=""
 marks=""
 fees=""
 dict={}

 def createstudent(self,firstname,email,number,subject,marks,fee):
   innerdict={}
   self.name=firstname
   self.email=email
   self.subject=subject
   self.number=number
   self.marks=marks
   self.fees=fee

   innerdict['email']=self.email
   innerdict['subject']=self.subject
   innerdict['number']=self.number
   innerdict['marks']=self.marks
   innerdict['fees']=self.fees

   self.dict['firstname']=innerdict
   print(self.dict)