from rich import print

# 1 ---> disponible
# 0 ---> no disponible

#Funciones para listar todos los ingredientes de una categoría

def ver_inventario_completo(panes, salchichas, acompañantes, salsas, toppings):
        """Funcion para seleccionar la categoría de ingredientes a gestionar 
        """     

#Funciones para listar todos los productos en esa categoria de un tipo
def listar_ingredientes_categoria_tipo(panes, salchichas, acompañantes, salsas, toppings):
        """Funcion para seleccionar la categoría de ingredientes a gestionar por tipo
        """   

# Función para listar todos los ingredientes de un tipo dentro de una categoría
def listar_ingredientes_tipo(ingredientes_categoria):
    """Función para listar todos los ingredientes de un tipo dentro de una categoría
    """

# Función para buscar un ingrediente específico dentro de todas las categorías
def buscar_ingrediente(panes, salchichas, acompañantes, salsas, toppings):
    """Función para buscar un ingrediente específico dentro de todas las categorías.
    """

# Actualizar existencia de un producto específico
def actualizar_existencia_ingredientes(panes, salchichas, acompañantes, salsas, toppings, hotdogs):
    """Función para actualizar la existencia de un ingrediente específico dentro de una categoría.
    """

# Menu de gestión de inventario
def gestion_inventario(self):
        """Menu de las acciones del inventario.
        """        

        while True:
            print ("\n[italic blue]---------- Acciones ---------- ")
            opcion = input ("""                            
    1. Visualizar todo el inventario 
    2. Buscar un ingrediente específico 
    3. Tipos de ingredientes por categoría
    4. Actualizar la existencia de un producto específico 
    5. Regresar
                                    
    ---> """)
            if opcion == "1":
                ver_inventario_completo(self.pan, self.salchicha, self.acompañantes, self.salsa, self.toppings)
            elif opcion == "2":
                buscar_ingrediente(self.pan, self.salchicha, self.acompañantes, self.salsa, self.toppings)
            elif opcion == "3":
                listar_ingredientes_categoria_tipo(self.pan, self.salchicha, self.acompañantes, self.salsa, self.toppings)
            elif opcion == "4":
                actualizar_existencia_ingredientes(self.pan, self.salchicha, self.acompañantes, self.salsa, self.toppings, self.hotdogs)

            elif opcion == "5":
                break

            else:
                print("\n[italic red]Opción inválida. Introduzca una opción válida por favor.\n")
                
