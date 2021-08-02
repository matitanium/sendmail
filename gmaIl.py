import smtplib

user = "matinnoriyan@gmail.com"
passw = "******" #your password

froM = user
to  = "target@gmail.com"
message = "hello matin "
smtp = smtplib.SMTP()
smtp.connect("smtp.gmail.com",587)
smtp.starttls()
smtp.login(user,passw)
smtp.sendmail(froM,to ,message)
smtp.close()