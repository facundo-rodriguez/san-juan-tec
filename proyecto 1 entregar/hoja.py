
from dataclasses import dataclass, asdict,field
from typing import Any,List,ClassVar
from productos import Producto

from validar import validar_impuesto

@dataclass(order=True)
class  Hoja(Producto):
  
    __tamanio:str
    __marca:str
    __color:str
    __cantidad_paquete:int

    __impuesto:ClassVar[float]=field(init=False,repr=True,default=None)

    tipo: ClassVar[str] = "Hoja"

    def __post_init__(self):

        Hoja.__impuesto=validar_impuesto(Hoja.__impuesto)
    
        self.precio= self.precio + ( (self.precio*Hoja.__impuesto)/100 )
        
        super().__post_init__()



    @property
    def impuesto(self):
        return self.__impuesto

    @property
    def tamanio(self):
        return self.__tamanio

    @property
    def marca(self):
        return self.__marca

    @property
    def color(self):
        return self.__color

    @property
    def cantidad_paquete(self):
        return self.__cantidad_paquete


    @tamanio.setter
    def tamanio(self,tamanio):
        self.__tamanio=tamanio


    @marca.setter
    def marca(self,marca):
        self.__marca=marca

    @color.setter
    def color(self,color):
        self.__color=color

    @cantidad_paquete.setter
    def cantidad_paquete(self,cantidad_paquete):
        self.__cantidad_paquete=cantidad_paquete

    @impuesto.setter
    def impuesto(cls,impuesto):
        cls.__impuesto=impuesto

    

    def __str__(self) -> str:
        
        super().__str__()
        return f"codigo: {self.codigo}, nombre: {self.nombre}, precio: {self.precio}, stock: {self.stock}, tamaño: {self.tamanio}, marca: {self.marca}, color: {self.color}, cantidad por paquete: {self.cantidad_paquete}"

    @classmethod
    def listar(cls):
        
        hojas = [producto for producto in super().listar() if producto.tipo == "Hoja"]
        
        return sorted(hojas)



