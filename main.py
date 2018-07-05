import smtplib
from  email.mime.multipart import MIMEMultipart
from  email.mime.text import MIMEText
from  email.mime.base import MIMEBase
from  email import encoders
from  Email_id_password import email,password

sender_email=input("Enter 'TO' E-Mail Address :")
subject_contnet=input("Enter Subject Of The E-Mail:")
email_body=input("Enter Body Of The E-Mail:")

#-------------------  ADDING FROM & TO  ADDRESS OF THE MAIL AND ALSO 'SUBJECT' --------------------

msg = MIMEMultipart()
msg['From']= email ; msg['To']= sender_email ; msg['Subject']= subject_contnet
msg.attach(MIMEText(email_body,'plain'))

#--------------------------- Attaching Files --------------------------------------------

for i in range(int(input("Enter no.of files do you want to insert:"))):
    filename= input("Enter the filename:")      # EX:"workfile.txt"  "krishna_2.jpg"
    attachment= open(filename,"rb")
    part=MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)
text=msg.as_string()

#------------------- CONNECTING & LOGIN TO MAIL --------------------

server=smtplib.SMTP('smtp.gmail.com',587)# To connect the SMTP SERVER which is used by the GOOGLE.
server.starttls() # TLS = Transport Layer Security Which starts encoding.
server.login(email,password)

#------------------- SENDING EMAIL ----------------------------------

server.sendmail(email,sender_email,text)

#------------------- fetching attachment ----------------------------

server.quit()


