

def venta(cls):    
    
    """         
        Hacer una venta – Solicitar codigo de producto y cantidad a
        vender 
    """
    try:
        venta_codigo=int(input("ingrese el codigo del producto que quiere vender: "))
        
        if( cls.existe(venta_codigo) ):
            
            venta_cantidad=int(input("ingrese la cantidad del producto a vender: "))

            producto=cls.traer_un_producto(venta_codigo)

            if( producto.stock >= venta_cantidad ):
                
                print("el precio total de la venta es de: ",producto.precio * venta_cantidad)

                producto.stock-=venta_cantidad
                print("el stock actual es de ", producto.stock, "unidades")

                producto.cantidad_vendida+=venta_cantidad
                print("la cantidad total vendida del producto es de: ", producto.cantidad_vendida)

                precio_venta=producto.precio * venta_cantidad
                producto.recaudacion+=precio_venta
                    
                print("la recuadacion total del producto es de: ", producto.recaudacion)
            
                print("venta realizada con exito")
        
            else:
                
                print("no hay stock suficiente")
                print("el stock actual es de ", producto.stock, "unidades")
             

        else:
            print("no existe el producto")

    except:
        print("error")



def mostrar_cadena(cls,n:int,producto_mostar=None):
    
    """
        se muestra una lista o un solo producto
    """

    if(n==1):
        
        productos=cls.listar()
        representaciones_en_cadena =  " ,\n".join([str(producto) for producto in productos])
        print(representaciones_en_cadena)
    
    elif(n==2):
        
        if(producto_mostar !=None):
            print(str(producto_mostar))



def borrar_un_articulo(cls):
    
    try:
        codigo=int(input("ingrese el codigo del producto a borrar: "))

        if( cls.existe(codigo) ):

            if( cls.eliminar_producto(codigo) ): 
                print("se elimino el producto")

            else:
                print("no se pudo eliminar el producto")

        else:
            print("no existe el producto") 
        
    except:
        print("error")

    
def borrar_todos(cls):
   
    cls.listar().clear()
    
    if(len(cls.listar())==0):
       
        print("se eliminaron todos los productos")
    
    else:
        print("no se eliminaron los productos")




def menu():
    
    print("1-introducir un nuevo articulo: ")
    print("2-hacer venta: ")
    print("3-mostrar informacion de todos los productos")
    print("4-mostrar informacion de un producto")
    print("5-borrar un articulo")
    print("6-borrar todos los articulos")
    print("7-salir")


def elegir_opcion(msj:str):
     
    while True:

        try:
            opcion=int(input(msj))

            break

        except:
            print("error, intente nuevamente")
        
            continue

    return opcion