


from clases import Orden,Producto,OrdenProducto,Cliente,Base

from imports import *

from conexionDB import conexion

session=conexion(Base)

def menu():

    print("1-registar cliente")
    print("2-registrar producto")
    print("3-ver un producto")
    print("4-ver todos los productos")
    print("5-vender productos")
    print("6-ver todos los clientes")
    print("7-enviar email con lista de clientes")
    print("cualquier otro numero para salir")
    print("elija el numero de opcion que quiera")


def programa():
    while(True):
        
        menu()

        try:
            opcion = int(input("opcion: "))

            if(opcion == 1):
            
                Cliente.registrar_cliente(session)

            elif(opcion == 2):
                Producto.registrar_producto(session)

            elif(opcion == 3):
                
                producto=Producto.buscar_producto(session)
                
                if(producto):
                    print(producto)
                else:
                    print("producto no encontrado")

            
            elif(opcion == 4):
                Producto.listar_productos(session)

            elif(opcion == 5):

                Orden.crear_orden(session)

            elif(opcion == 6):

                Cliente.listar_clientes(1,session)

            elif(opcion == 7):

                
                Cliente.listar_clientes(2,session)
                
            else:
                print("fin del programa")
                break

        except Exception as e:
            print("error ")
            print(e)


