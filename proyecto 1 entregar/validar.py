

def validar_codigo(cls,codigo):
    #cod=codigo

    bandera=cls.existe(codigo)
    while bandera:

      try:    
        print("el codigo ya existe, ingrese otro codigo")
        cod=int(input("ingrese el codigo: "))
        bandera=cls.existe(cod)
                
        
        codigo=cod

      except:
        print("error")
        continue


    return codigo,True



def validar_datos(lista:list):

    bandera=[]

    for i in range(len(lista)):
        
        if(isinstance(lista[i], str) ):
           
            "Es una cadena string"

            if( not lista[i].strip() ):
                
                bandera.append(False)
            
            else:
                bandera.append(True)

        elif ( isinstance(lista[i], int) or isinstance(lista[i], float) ):
            "Es un número int "

            if(lista[i]<0 ):

                bandera.append(False)
            
            else:
                bandera.append(True)

        else:
            "No es ni una cadena ni un número"

    if( False in bandera):
        return False
    else:
        return True



def validar_datos_producto(codigo,stock,precio,nombre):
    
    bandera=True

    if( precio<0 or stock<0 or codigo<0  or  not nombre.strip() ):
                
        bandera=False
            
    
    return bandera


def validar_datos_libro(autor,anio,editorial):

    bandera=True

    if( not autor.strip() or not anio.strip() or not editorial.strip() ):
        bandera=False
    

    return bandera



def validar_datos_hoja(tamanio,marca,color,cantidad_paquete):

    bandera=True

    if( not tamanio.strip() or not marca.strip() or not color.strip() or cantidad_paquete<=0 ):
        bandera=False
    

    return bandera




def validar_impuesto(n):

    impuesto=n
    
    if(n == None):
        
        while True:
                
            try:
                   
                imp=float(input("ingrese el impuesto del producto en porcentaje: "))
                
                bandera=validar_datos([imp])
                
                if(bandera):
                        #Libro.__impuesto=imp
                    impuesto=imp
                    break
                
                else:
                    print("intente otra vez")

            except:
                print("error, intente otra vez")
    
    
    return impuesto