
from dataclasses import dataclass, asdict,field
from typing import Any,List,ClassVar
from productos import Producto
from validar import validar_impuesto

@dataclass(order=True)
class  Libro(Producto):
    """Clase que representa un libro"""
    
    #__lista:ClassVar[List["Libro"]]=[]
    __autor:str
    __anio:str
    __editorial:str
    __impuesto:ClassVar[float]=field(init=False,repr=True,default=None)

    tipo:ClassVar[str] = "Libro"

    def __post_init__(self):

        #imp=validar_impuesto(Libro.__impuesto)
        Libro.__impuesto=validar_impuesto(Libro.__impuesto)
    
        self.precio= self.precio + ( (self.precio*Libro.__impuesto)/100 )
        super().__post_init__()
        #Libro.__lista.append(self)
        

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        self.__anio = anio

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, editorial):
        self.__editorial = editorial

    
    @property
    def impuesto(self):
        return self.__impuesto

    @impuesto.setter
    def impuesto(self,impuesto):
        self.__impuesto=impuesto


    
    def __str__(self) -> str:
        
        return f"codigo: {self.codigo}, nombre: {self.nombre}, autor: {self.autor}, año: {self.anio}, editorial: {self.editorial} precio: {self.precio}, stock: {self.stock}"

    @classmethod
    def listar(cls):

        libros = [producto for producto in super().listar() if producto.tipo == "Libro"]
        
        return sorted(libros)

