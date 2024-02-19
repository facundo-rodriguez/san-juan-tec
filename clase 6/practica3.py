
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

import smtplib


servidor="smtp.gmail.com"
puerto=587
contrasenia=1234

emisor="aa@hotmail.com"

mail=MIMEMultipart()
mail['From']=emisor
mail['To']=emisor
mail['Subject']="Asunto del correo electronico"

with open("archivo.txt", "rb") as archivo:

    adjuntar=MIMEApplication(archivo.read(), _subtype="txt")
    adjuntar.add_header("Content-Disposition", "attachment", filename="archivo de prueba.txt")
    mail.attach(adjuntar)


with open("img.jpg", "rb") as imagen:
    adjuntar=MIMEImage(imagen.read(), _subtype="jpg")
    adjuntar.add_header("Content-Disposition", "attachment", filename="Mi imagen.jpg")
    mail.attach(adjuntar)


texto=f'''

    cuerpo del correo
    este es el cuerpo del correo

'''

texto_insertar=MIMEText(texto, "plain")
mail.attach(texto_insertar)


print(mail.items())

for adjunto in mail.get_payload():
    print("\nnombre del archivo: ", adjunto.get_filename())
    print("tipo de contenido: ",adjunto.get_content_type())
    print("content disposition: ",adjunto.get_content_disposition() )


with smtplib.SMTP(servidor,puerto) as servidor:
    servidor.starttls()
    servidor.login(emisor,contrasenia)
    servidor.sendmail(emisor,emisor,mail.as_string())
