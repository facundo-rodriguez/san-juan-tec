
"""
El sistema debe permitir:
 Cargar al menos un tipo de producto, como por ejemplo libros. Además,
podrían cargarse otros como lápices, libretas, etc.
 Buscar un producto previamente cargado y ver sus datos. Notificar si no se
encuentra el producto.
 Listar junto con sus datos, ordenados por el precio, todos los productos que
hayan sido cargados.
 Vender unidades de alguno de los productos cargados, actualizando el stock
de ese producto. Notificar si no se encuentra el producto o el stock es menor
a lo que se desea vender.
Deben en el main cargarse varios productos y probar cada una de las
funcionalidades mencionadas. Puede esto también realizarse (recomendable, para
practicar más y darle una mejor forma al programa) a través de menús donde el
usuario seleccione lo que desea realizar.

"""

from productos import Producto
from libros import Libro
from hoja import Hoja
from funciones import menu,venta,elegir_opcion,mostrar_cadena
from carga_datos import *




def programa():
        
    while True:
        
        menu()
        
        opcion=elegir_opcion("elija la opcion que quiera: ")
        
        if(opcion==1):

            print("que quiere cargar? 1-Libro, 2-recma de hojas, cualquier otro numero para salir")
            
            sub_opcion=elegir_opcion("elija la opcion que quiera: ")

            if(sub_opcion!=1 and sub_opcion!=2):
                    break
            
            else:

                codigo,nombre,precio,stock=datos_producto()

                if(sub_opcion==1):

                    autor,anio,editorial=datos_libro()

                    Libro(codigo,nombre,precio,stock,autor,anio,editorial)


                elif(sub_opcion==2):

                    tamanio,marca,color,cantidad_paquete=datos_hojas()

                    Hoja(codigo,nombre,precio,stock,tamanio,marca,color,cantidad_paquete)



            
        elif(opcion==2):

            venta(Producto)
            

        
        elif(opcion==3):

            print("que quiere mostrar? 1-Libro, 2-recma de hojas, 3-todos los productos, cualquier otro numero para salir")
            
            sub_opcion=elegir_opcion("elija la opcion que quiera: ")

            if(sub_opcion!=1 and sub_opcion!=2 and sub_opcion!=3):
                    break
                
            else:
                if(sub_opcion==1):
                    #print(Libro.listar())
                    mostrar_cadena(Libro,1)
                
                elif(sub_opcion==2):
                    #print(Hoja.listar())
                    mostrar_cadena(Hoja,1)


                elif(sub_opcion==3):
                    mostrar_cadena(Producto,1)

        elif(opcion==4):

        
            codigo=elegir_opcion("ingrese el codigo del producto que quiere ver: ")        
            producto=Producto.traer_un_producto(codigo)
            mostrar_cadena(Producto,2,producto)
           

        elif(opcion==5):
            
            codigo=elegir_opcion("ingrese el codigo del producto que quiere borrar: ")
            Producto.eliminar_producto(codigo)
        

        elif(opcion==6):
            
            Producto.eliminar_todo()
        

        elif(opcion==7):
            break


