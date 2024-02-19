
import os

ruta = "C:/Users/FACU/Desktop/facu/python/cursatec/python avanzado/clase 5"
archivo="archivo2.txt"

def crear_archivo(ruta:str,nombre_archivo:str):

    if(os.path.isfile(ruta+"/"+nombre_archivo) ):
        print("El archivo ya existe")

    else:
        with open(ruta+"/"+nombre_archivo,"w") as archivo:
            print(f"El archivo {nombre_archivo} se creo correctamente")
    


def escribir(ruta,archivo,lineas):
    with open(ruta+"/"+archivo,"a") as archivo:
        for linea in lineas:
            archivo.write(str(linea + "\n"))


def leer(ruta:str,archivo:str):
    with open(ruta+"/"+archivo,"r") as archivo:
        return archivo.read()

#crear_archivo(ruta,archivo)

#escribir(".","archivo.txt",["hola","que tal", "como estas"])
#print(leer(".","archivo.txt"))
v=["hola","que tal", "como estas"]

with open("archivo.txt","w") as archivo:
    
    for i in range(len(v)):
        archivo.write(str(v[i]+"\n"))
    
    

print(leer(".","archivo.txt"))

def lista(*l):

    for i in l:
        print(i)

lista(v)
