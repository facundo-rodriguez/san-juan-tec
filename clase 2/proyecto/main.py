

from validaciones.validar import cadena_no_vacia
import menu.opciones as menu

def main():

   menu_finalizado= menu.mostrarMenu("Panaderia",["1-Pan","2-Facturas","3-Tortas"])

   if(menu_finalizado):
        menu.mostrarMenu("Libreria",["1-Hojas","2-Mapas","3-Lapices"])

   opcion=input("ingrese una opcion a validar: ")
   opcion_validada=False

   while(opcion_validada==False):

     opcion_validada=cadena_no_vacia(opcion)
     opcion=input("ingrese una opcion a validar: ")
    
    


if __name__=="__main__":
    main()