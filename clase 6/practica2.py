
from dataclasses import asdict, dataclass
from datetime import datetime
from email.mime.multipart import MIMEMultipart
import json
import os

import smtplib
from email.mime.text import MIMEText



@dataclass
class Persona:

    nombre:str
    fecha_nacimiento:datetime
    email:str

    @classmethod
    def crear_persona(cls):
        nombre:str = input("Ingrese el nombre: ")
        fecha_nacimiento= input("Ingrese la fecha de nacimiento separado con guiones: ")
        email:str = input("Ingrese el email: ")

        persona=cls(nombre,datetime.strptime(fecha_nacimiento,"%d-%m-%Y"))
        persona_dict=asdict(persona)

        if( os.path.isfile("persona.json") ): #esta linea pregunta si el archivo existe
            
            with open("persona.json","r") as archivo:
                
                data=json.load(archivo)

             
            with open("persona.json","w") as archivo:

                persona_dict.pop("nombre")
                data[nombre]=persona_dict

                json.dump(data,archivo,default=str)

        else:
            with open("persona.json","w") as archivo:

                persona_dict.pop("nombre")
                json.dump({nombre:persona_dict},archivo,default=str)



Persona.crear_persona()

nombre=input("ingrese el nombre de la persona a la que desea enviarle el mail: ")

with open("persona.json","r") as archivo:
    data=json.load(archivo)
    receptor=data[nombre]["email"]

    servidor="smtp.gmail.com"
    puerto=587
    contrasenia=1234
    emisor="aa@hotmail.com"

    mail=MIMEMultipart()
    mail['From']=emisor
    mail['To']=receptor
    mail['Subject']="Asunto del correo electronico"

    texto=f''' 
    fuiste registrado con exito 

    nombre: {nombre}
    correo: {receptor}
    fecha de nacimiento: {data[nombre]["fecha_nacimiento"]}

    '''

    texto_insertar=MIMEText(texto, "plain")
    mail.attach(texto_insertar)


with smtplib.SMTP(servidor,puerto) as servidor:
    servidor.starttls()
    servidor.login(emisor,contrasenia)
    servidor.sendmail(emisor,receptor,mail.as_string())
