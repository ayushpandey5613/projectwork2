import smtplib,getpass

while(True):
  try:
      #set up smtp server #
     c=smtplib.SMTP("smtp.gmail.com",587)
     
     x=input("enter email : ") 
      #for checking the format of email address is correct or not#
     if(x[-10:]=='@gmail.com'):
                #to mask hide the password#
     
              y=getpass.getpass("enter password : ")

              
              try:
                 
                  c.ehlo()
                  c.starttls()
                  #for login to email#
                  c.login(x,y)
              except:
                  print("either email address or password are incorrect")
                  continue
              else:
                  print("you are successfully logged in")
                  while(True):
                      z=input("enter recievers email address : ")
                #again for checking format#
                      if(z[-10:]=='@gmail.com'):

                           subject=input("Subject : ")
                           message=input("Message : ")
                           
                           
                           try:
                             #trying to sendmail#
                              c.sendmail(x,z,("Subject :"+str(subject)  +"\n\n" +str(message)))
                              c.quit()             
                              break  
                      
                          
                           except:
                              print("entered email address does not exist")
                              continue
                          

                           else:
                              print("entered reciepent email address is invalid,enter again.")
                              continue   
                      else:
                        print("entered email address does not exist,please enter valid email address")     

                  print(" email sent successfully,thaknyou")
                  break

              
     else:
        print("entered email address is invalid,please enter valid email address")  
  except:
    print("please check your network connection ")
    break  
