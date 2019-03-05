import smtplib

class Ge_mail():
    def __init__(self,username,password):
        self.username=str(username)
        self.password=str(password)
        self.server=smtplib.SMTP('smtp.gmail.com',587)
        self.server.starttls()
        self.server.login(self.username,self.password)
    def sendm(self,toaddr,msg):
        self.toaddr=toaddr
        self.msg=str(msg)
        self.server.sendmail(self.username,self.toaddr,self.msg)
    def quit(self):
        self.server.quit()