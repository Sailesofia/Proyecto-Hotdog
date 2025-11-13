from rich import print

#Función para ver los hotdogs disponibles
def ver_hotdogs_disponibles(hotdogs):
    """Función para ver los hotdogs disponibles.
    """

#Funcion para verificar la disponibilidad de un hotdog especifico
def verificar_disponibilidad_hotdog(hotdogs):
    """Función para verificar la disponibilidad de hotdog especifico.
    """

#Funcion para agregar un hotdog

def agregar_hotdog(hotdogs, panes, salchichas, acompañantes, salsas, toppings):
    """Función para agregar un hotdog al menu.
    """

def armar_hotdog(nombre, nuevo_pan, nueva_salchicha, nuevas_salsas, nuevos_toppings, nuevo_acompañante):
    """Función para armar un hotdog con los ingredientes seleccionados.
    """


def tiene_stock(ingrediente):
    """Función para ver el stock de un hotdog específico.
    """

#Funciones para eliminar un hotdog
def eliminar_hotdog_menu(hotdogs):   
    """Función para eliminar un hotdog del inventario mediante un menú.
    """

def eliminar_hotdog(hotdogs, hotdog_eliminar):
    """Función para eliminar un hotdog del inventario.
    """

#Funcion para gestionar el menu de hotdogs
def gestion_menu(self):
    """Menu para gestionar los hot dogs que se venden.
    """        

    while True:
        print ("\n[italic blue]---------- Acciones ---------- ")
        opcion = input ("""                                                                 
    1. Ver hotdogs disponibles
    2. Ver inventario de un hotdog específico
    3. Agregar un hotdog
    4. Eliminar un hotdog
    5. Regresar
                        
---> """)

        if opcion == "1":
            ver_hotdogs_disponibles(self.hotdogs)
            break
        elif opcion == "2":
            verificar_disponibilidad_hotdog(self.hotdogs)
            break
        elif opcion == "3":
            agregar_hotdog(self.hotdogs, self.pan, self.salchicha, self.acompañantes, self.salsa, self.toppings)
            break
        elif opcion == "4":
            eliminar_hotdog_menu(self.hotdogs)
            break
        elif opcion == "5":
            break
            
        else:
            print("\n[italic red]Opción inválida. Introduzca una opción válida por favor.\n")