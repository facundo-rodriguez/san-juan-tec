

from typing import List
from validaciones.validar import cadena_no_vacia

def mostrarMenu(titulo:str, opciones:List[str])->bool:
    
    opcion_validada=False

    while(opcion_validada==False):

        try:
            print()
            print(titulo)
            print()

            for opcion in opciones:
                print(opcion)

            opcion=input("Ingrese opción: ")
            opcion_validada=cadena_no_vacia(opcion)

            if(opcion_validada):
                print("ya lo atendemos")

            return opcion_validada

        except Exception:
            print("intente nuevamente")
            