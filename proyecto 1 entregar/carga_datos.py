
from validar import validar_datos

def datos_producto():
        
    while True:

        try:  
            codigo=int(input("ingrese el codigo del producto: "))
            nombre=input("ingrese el nombre del producto: ").lower()
            precio=float(input("ingrese el precio del producto: "))
            stock=int(input("ingrese el stock del producto: "))
        
            bandera=validar_datos([codigo,stock,precio,nombre])

            if(bandera):
                break
                
            else:
                print("ingrese datos validos")

        except:
            print("error")
            continue        
        
   
    return codigo,nombre,precio,stock

    
def datos_libro():

    while True:

        try:  
        
            autor=input("inggrese el nombre del autor: ")
            anio=input("ingrese el año de publicacion: ")
            editorial=input("ingrese el nombre de la editorial: ")

            bandera=validar_datos([autor,anio,editorial])

            if(bandera):
                break
                
            else:
                print("ingrese datos validos")

        except:
            print("error")
            continue        
     

    return autor,anio,editorial

def datos_hojas():

    
    while True:

        try:  
        
                    
            tamanio=input("ingrese el tamanio de la hoja: ")
            marca=input("ingrese la marca: ")
            color=input("ingrese el color: ")  
            cantidad_paquete=int(input("ingrese la cantidad de hojas que trae el paquete: "))

            bandera=validar_datos([tamanio,marca,color,cantidad_paquete])

            if(bandera):
                break
                
            else:
                print("ingrese datos validos")

        except:
            print("error")
            continue        
     

    return tamanio,marca,color,cantidad_paquete


