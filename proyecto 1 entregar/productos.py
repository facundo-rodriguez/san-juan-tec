"""
Descripción técnica
Todos los productos deben tener los atributos: impuesto (float; atributo de clase),
__lista (list que contendrá los productos que vayan cargándose; atributo de
clase), código (int), nombre (str), precio (float que debe ser el precio cargado más el
impuesto) y stock (int).
Debe existir una clase padre Producto y clases hijas como Libro, Lápiz, etc., que
representen los distintos productos de la tienda y tengan atributos y/o métodos
específicos además de los de la clase padre.
Las clases deben ser dataclasses, tener las propiedades (property) correspondientes
a sus atributos y seguir las buenas prácticas vistas en clase (como anotaciones de
tipo, excepciones y estructurar el proyecto separando por módulos).
Debe existir al menos una validación de datos ingresados por el usuario, por
ejemplo, para que no se seleccione un número de opción que no corresponda a ese
menú. Si no se realizan menús hacer alguna otra validación.

"""
from dataclasses import dataclass, asdict,field
from typing import Any,List,ClassVar
from abc import ABC, abstractmethod,ABCMeta

from validar import validar_codigo



@dataclass(order=True)
class  Producto() :

    
    sort_index:Any= field(init=False, repr=False)

    __lista:ClassVar[List]=[]

    __codigo:int
    __nombre:str
    
    
    "precio (float que debe ser el precio cargado más el impuesto)"
    __precio:float
    __stock:int
    __recaudacion:float=field(init=False, repr=False, default=0)
    __cantidad_vendida:int=field(init=False, repr=False, default=0)

    tipo: ClassVar[str] = "Producto"

    def __post_init__(self):

        
        self.sort_index=self.__precio
        #self.agregar_producto()
        #Producto.__lista.append(self)
        Producto.agregar_producto(self)
      

        

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @property
    def recaudacion(self):
        return self.__recaudacion

    @property
    def cantidad_vendida(self):
        return self.__cantidad_vendida

    
   
    @codigo.setter
    def codigo(self,codigo):

        #cod=validar_codigo(codigo)
        self.__codigo=codigo
                

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

   
    @precio.setter
    def precio(self,precio):
        self.__precio=precio

    @stock.setter
    def stock(self,stock):
        self.__stock=stock


    @recaudacion.setter
    def recaudacion(self,recaudacion):
        self.__recaudacion=recaudacion


    @cantidad_vendida.setter
    def cantidad_vendida(self,cantidad_vendida):
        self.__cantidad_vendida=cantidad_vendida


    @classmethod
    def listar(cls):

        productos = sorted(cls.__lista, key=lambda producto: producto.sort_index )
 
        return productos


    @classmethod
    def agregar_producto(cls,self):
      
        self.codigo=validar_codigo(Producto,self.codigo)[0]
        cls.__lista.append(self)


        

    @classmethod
    def existe(cls,codigo):
        for producto in cls.__lista:
            if producto.codigo==codigo:
                return True
        return False


    @classmethod
    def traer_un_producto(cls,codigo):
        
        encontrado=None
        try:

            if( cls.existe(codigo) ):

                for producto in cls.__lista:
                    
                    if producto.codigo==codigo:
                        
                        encontrado= producto

            else:
                print("no existe el producto") 
            
        except:
            print("error")

        return encontrado
       

    @classmethod
    def buscar_producto_por_nombre(cls,nombre):
        for producto in cls.__lista:
            if producto.nombre==nombre:
                return producto
        return None
    
  
    @classmethod
    def eliminar_producto(cls,codigo):
        
        try:
            
            if( cls.existe(codigo) ):

                
                cls.__lista.remove(cls.traer_un_producto(codigo)) 
                print("se elimino el producto")

            else:
                print("no existe el producto") 
            
        except:
            print("error")

        

    @classmethod
    def eliminar_todo(cls):

        cls.__lista.clear()
        
        if(len(cls.__lista)==0):
       
            print("se eliminaron todos los productos")
    
        else:
            print("no se eliminaron los productos")


    @classmethod
    def modificar_producto(cls,codigo,nombre,impuesto,precio,stock):
        for producto in cls.__lista:
            if producto.codigo==codigo:
                producto.nombre=nombre
                producto.impuesto=impuesto
                producto.precio=precio
                producto.stock=stock
                return True
        return False

