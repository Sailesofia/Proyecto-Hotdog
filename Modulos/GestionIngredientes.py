from rich import print

#Funciones para listar todos los ingredientes de una categoría

def listar_ingredientes_categoria_ver(panes, salchichas, acompañantes, salsas, toppings):
        """Funcion para seleccionar la categoría de ingredientes a gestionar 
        """  

#Funciones para listar todos los productos en esa categoria de un tipo

def listar_ingredientes_categoria_tipo(panes, salchichas, acompañantes, salsas, toppings):
        """Funcion para seleccionar la categoría de ingredientes a gestionar por tipo
        """  

def listar_ingredientes_tipo(ingredientes_categoria):
    """Función para listar todos los ingredientes de un tipo dentro de una categoría
    """

#Funciones para agregar ingredientes con validaciones

def listar_ingredientes_categoria(panes, salchichas, acompañantes, salsas, toppings):
        """Funcion para seleccionar la categoría de ingredientes a gestionar 
        """   

def agregar_ingrediente_categoria(ingredientes: list, nuevo_ingrediente):
    """Función para agregar un nuevo ingrediente a la categoría correspondiente
    """

def verify_within_ingredients(ingredient_name, ingredients_list):
    """Función para verificar si un ingrediente ya existe en la lista de ingredientes
    """
    for ingredient in ingredients_list:
        if ingredient.nombre == ingredient_name:
            print(f"\n[italic red] El ingrediente {ingredient_name} ya existe. Inténtelo de nuevo.\n")
            return True
    return False

def registrar_pan (panes_app):
        """Función para registrar un nuevo ingrediente
        """ 

def registrar_acompañante (acompañantes_app):
        """Función para registrar un nuevo acompañante
        """  

def registrar_salchicha (salchichas_app):
        """Función para registrar una nueva salchicha
        """  

def registrar_salsa (salsas_app):
        """Función para registrar una nueva salsa
        """  

def registrar_topping (toppings_app):
        """Función para registrar una nueva salchicha
        """  

# Funciones para eliminar ingredientes con validaciones

def eliminar_ingrediente_categoria(ingredientes: list, nombre_ingrediente, hotdogs_app):
    """Función para eliminar un ingrediente de la categoría correspondiente
    """

def encontrar_hotdog_ingredientes (hotdogs_app, ingrediente):
    """Función para encontrar hotdogs que contienen un ingrediente específico
    """  

def eliminar_ingrediente (ingredientes_app, hotdogs_app, hotdogs: list, nombre_ingrediente):
    """Función para eliminar un ingrediente seleccionado
    """ 


def menu_para_eliminar(panes, salchichas, acompañantes, salsas, toppings, hotdogs):
    """Funcion para seleccionar la categoría del ingrediente a eliminar 
    """        

    while True:
            opcion = input ("""
    ¿Qué tipo de ingrediente desea eliminar?
                                
    1. Pan 
    2. Salchicha
    3. Acompañante
    4. Salsa
    5. Topping
    6. Regresar
                                                        
    ---> """)
            
            if opcion =="1":
                seleccionado = input (" Nombre del ingrediente que desea eliminar:      ")
                eliminar_ingrediente_categoria(panes, seleccionado, hotdogs)
                break
            elif opcion =="2":
                seleccionado = input (" Nombre del ingrediente que desea eliminar:      ")
                eliminar_ingrediente_categoria(salchichas, seleccionado, hotdogs)
                break
            elif opcion =="3":
                seleccionado = input (" Nombre del ingrediente que desea eliminar:      ")
                eliminar_ingrediente_categoria(acompañantes, seleccionado, hotdogs)
                break
            elif opcion =="4":
                seleccionado = input (" Nombre del ingrediente que desea eliminar:      ")
                eliminar_ingrediente_categoria(salsas, seleccionado, hotdogs)
                break
            elif opcion =="5":
                seleccionado = input (" Nombre del ingrediente que desea eliminar:      ")
                eliminar_ingrediente_categoria(toppings, seleccionado, hotdogs)
                break
            elif opcion =="6":
                print ("\n[italic blue]Regresando al menú de gestión de ingredientes...\n")
                break
            else:
                print ("[italic red]Opción inválida")



# Menu general de gestión de ingredientes
def gestion_ingredientes(self):
        """Funcion para llamar al módulo de gestión de ingredientes. 
        """        
        while True:
            opcion = input ("""
    ¿Qué desea realizar?
                                
    1. Listar todos los productos de una categoría 
    2. Listar todos los productos de un tipo dentro de una categoría
    3. Agregar un ingrediente
    4. Eliminar un ingrediente
    5. Regresar
                                                        
    ---> """)
            
            if opcion =="1":
                listar_ingredientes_categoria_ver(self.pan, self.salchicha, self.acompañantes, self.salsa, self.toppings)
                break
            elif opcion =="2":
                listar_ingredientes_categoria_tipo(self.pan, self.salchicha, self.acompañantes, self.salsa, self.toppings)
                break
            elif opcion =="3":
                listar_ingredientes_categoria(self.pan, self.salchicha, self.acompañantes, self.salsa, self.toppings)
                break
            elif opcion =="4":
                menu_para_eliminar(self.pan, self.salchicha, self.acompañantes, self.salsa, self.toppings, self.hotdogs)
                break
            elif opcion =="5":
                break
            else:
                print ("[italic red]Opción inválida")