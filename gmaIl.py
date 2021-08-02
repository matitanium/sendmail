import smtplib

user = "matinnoriyan@gmail.com" #your email
passw = "******" #your password
#code by matin nouriyan
froM = user
to  = "target@gmail.com" #target
message = "hello matin "
smtp = smtplib.SMTP()
smtp.connect("smtp.gmail.com",587)
smtp.starttls()
smtp.login(user,passw)
smtp.sendmail(froM,to ,message)
smtp.close()
