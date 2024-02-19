


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def enviar_email(smtp_server, smtp_port,smtp_user,smtp_pass,from_email,to_email,subject,message):
    
    smtp_server = smtp_server  
    smtp_port = smtp_port
    smtp_user = smtp_user
    smtp_pass = smtp_pass 

    from_email = from_email
    to_email = to_email  
    subject = subject 
    message = message

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))


    archivo=open("archivo.txt","rb")

    
    adjuntar=MIMEApplication(archivo.read(), _subtype="txt")
    adjuntar.add_header("Content-Disposition", "attachment", filename="archivo.txt")
    msg.attach(adjuntar)


    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(smtp_user, smtp_pass)

        server.sendmail(from_email, to_email, msg.as_string())

        server.quit()
        print("Correo enviado con éxito")
    except Exception as e:
        print(f"No se pudo enviar el correo. Error: {str(e)}")



