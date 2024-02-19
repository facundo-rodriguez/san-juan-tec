
from datetime import date
import json

with open('data.json', 'w', encoding='utf-8') as archivo:
    
    fecha_nacimiento=date(1914,8,26)
    json.dump( {"nombre":"julio","apellido":"cortazar","nacimiento":fecha_nacimiento}, archivo, default=str, indent=4 )


with open('data.json', 'r', encoding='utf-8') as archivo:
    data=json.load(archivo)
    print(data)


apellido=data['apellido']
print(data)