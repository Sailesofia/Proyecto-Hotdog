from rich import print
from Clases.Pan import Pan
from Clases.Acompañante import Acompañante
from Clases.Salchicha import Salchicha
from Clases.Salsa import Salsa
from Clases.Toppings import Toppings

#Funciones para listar todos los ingredientes de una categoría

def listar_ingredientes_categoria_ver(panes, salchichas, acompañantes, salsas, toppings):
    """Funcion para seleccionar la categoría de ingredientes a gestionar 
    """  
    while True:
        option = input ("""
¿Qué categoría desea visualizar?
                            
1. Pan 
2. Salchicha
3. Acompañante
4. Salsa
5. Topping
6. Regresar
                                                    
---> """)
        
        if option =="1":
            for ingrediente in panes:
                print("\n"+ingrediente.info_pan())
            break
        elif option =="2":
            for ingrediente in salchichas:
                print("\n"+ingrediente.info_salchicha())
            break
        elif option =="3":
            for ingrediente in acompañantes:
                print("\n"+ingrediente.info_acompañante())
            break
        elif option =="4":
            for ingrediente in salsas:
                print("\n"+ingrediente.info_salsa())
            break
        elif option =="5":
            for ingrediente in toppings:
                print("\n"+ingrediente.info_topping())
            break
        elif option =="6":
            print ("\n[italic blue]Regresando al menú de gestión de ingredientes...\n")
            break
        else:
            print ("[italic red]Opción inválida")

#Funciones para listar todos los productos en esa categoria de un tipo

def listar_ingredientes_categoria_tipo(panes, salchichas, acompañantes, salsas, toppings):
    """Funcion para seleccionar la categoría de ingredientes a gestionar por tipo
    """  

    while True:
        option = input ("""
¿Qué categoría desea visualizar?
                            
1. Pan 
2. Salchicha
3. Acompañante
4. Salsa
5. Topping
6. Regresar
                                                    
---> """)
        
        if option =="1":
            listar_ingredientes_tipo(panes)
            break
        elif option =="2":
            listar_ingredientes_tipo(salchichas)
            break
        elif option =="3":
            listar_ingredientes_tipo(acompañantes)
            break
        elif option =="4":
            listar_ingredientes_tipo(salsas)
            break
        elif option =="5":
            listar_ingredientes_tipo(toppings)
            break
        elif option =="6":
            print ("\n[italic blue]Regresando al menú de gestión de ingredientes...\n")
            break
        else:
            print ("[italic red]Opción inválida")

def listar_ingredientes_tipo(ingredientes_categoria):
    """Función para listar todos los ingredientes de un tipo dentro de una categoría
    """

    tipo_buscar = input("Ingrese el tipo de ingrediente que desea listar: ")
    encontrados = [ingrediente for ingrediente in ingredientes_categoria if ingrediente.tipo.lower() == tipo_buscar.lower()]

    if encontrados:
        print(f"\n[italic green]Ingredientes del tipo '{tipo_buscar}':\n")
        for ingrediente in encontrados:

            if (ingrediente == Pan):
                print(ingrediente.info_pan())
            elif (ingrediente == Salchicha):
                print(ingrediente.info_salchicha())
            elif (ingrediente == Salsa):
                print(ingrediente.info_salsa())
            elif (ingrediente == Toppings):
                print(ingrediente.info_topping())
            elif (ingrediente == Acompañante):
                print(ingrediente.info_acompañante())
            else:
                print("\nIngrediente no identificado\n")
    else:
        print(f"\n[italic red]No se encontraron ingredientes del tipo '{tipo_buscar}'.\n")

#Funciones para agregar ingredientes con validaciones

def listar_ingredientes_categoria(panes, salchichas, acompañantes, salsas, toppings):
    """Funcion para seleccionar la categoría de ingredientes a gestionar 
    """   
    while True:
        option = input ("""
¿Qué tipo de ingrediente desea agregar?
                            
1. Pan 
2. Salchicha
3. Acompañante
4. Salsa
5. Topping
6. Regresar
                                                    
---> """)
        
        if option =="1":
            registrar_pan(panes)
            break
        elif option =="2":
            registrar_salchicha(salchichas)
            break
        elif option =="3":
            registrar_acompañante(acompañantes)
            break
        elif option =="4":
            registrar_salsa(salsas)
            break
        elif option =="5":
            registrar_topping(toppings)
            break
        elif option =="6":
            print ("\n[italic blue]Regresando al menú de gestión de ingredientes...\n")
            break
        else:
            print ("[italic red]Opción inválida")

def agregar_ingrediente_categoria(ingredientes: list, nuevo_ingrediente):
    """Función para agregar un nuevo ingrediente a la categoría correspondiente
    """
    ingredientes.append(nuevo_ingrediente)
    print(f"Ingrediente {nuevo_ingrediente.nombre} agregado exitosamente.")

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

    print ("\n[italic blue]------------- Introduzca los detalles del ingrediente ------------- \n")  
    panes = panes_app
    nombre = input("Introduzca su nombre: ")  
    tipo = input("Introduzca el tipo: ") 
    tamaño = input("Tamaño del pan en pulgadas: ") 

    if (nombre.isalpha() == False | verify_within_ingredients(nombre, panes) == True):
        print("\n[italic red] El nombre del ingrediente no debe contener números o caracteres especiales. Inténtelo de nuevo.\n")
        
        if (tipo.isalpha() == False):
            print("\n[italic red] El tipo del ingrediente no debe contener números o caracteres especiales. Inténtelo de nuevo.\n")
            registrar_pan(panes_app)

            if (tamaño.isdigit() == False):
                print("\n[italic red] El tamaño del ingrediente debe ser un número. Inténtelo de nuevo.\n")
                registrar_pan(panes_app)


    nuevo_pan = Pan(nombre, tipo, tamaño, "pulgadas")
    agregar_ingrediente_categoria(panes, nuevo_pan)
    print(f"\n[italic green] El pan {nuevo_pan.nombre} ha sido registrado exitosamente.\n")

def registrar_acompañante (acompañantes_app):
    """Función para registrar un nuevo acompañante
    """  
    print ("\n[italic blue]------------- Introduzca los detalles del ingrediente ------------- \n")  
    acompañantes = acompañantes_app
    nombre = input("Introduzca su nombre: ")  
    tipo = input("Introduzca el tipo: ") 
    tamaño = input("Tamaño del pan: ") 
    unidad = input("Unidad de medida: ")

    if (nombre.isalpha() == False | verify_within_ingredients(nombre, acompañantes) == True):
        print("\n[italic red] El nombre del ingrediente no debe contener números o caracteres especiales. Recuerde que el nombre debe ser único para cada ingrediente. Inténtelo de nuevo.\n")
        
        if (tipo.isalpha() == False):
            print("\n[italic red] El tipo del ingrediente no debe contener números o caracteres especiales. Inténtelo de nuevo.\n")
            registrar_acompañante(acompañantes_app)

            if (tamaño.isdigit() == False):
                print("\n[italic red] El tamaño del ingrediente debe ser un número. Inténtelo de nuevo.\n")
                registrar_acompañante(acompañantes_app)

                if (unidad.isalpha() == False):
                    print("\n[italic red] La unidad de medida no debe contener números o caracteres especiales. Inténtelo de nuevo.\n")
                    registrar_acompañante(acompañantes_app)

    nuevo_acompañante = Acompañante(nombre, tipo, tamaño, unidad)
    agregar_ingrediente_categoria(acompañantes, nuevo_acompañante)
    print(f"\n[italic green] El acompañante {nuevo_acompañante.nombre} ha sido registrado exitosamente.\n")


def registrar_salchicha (salchichas_app):
    """Función para registrar una nueva salchicha
    """  
    print ("\n[italic blue]------------- Introduzca los detalles del ingrediente ------------- \n")  
    salchichas = salchichas_app
    nombre = input("Introduzca su nombre: ")  
    tipo = input("Introduzca el tipo: ") 
    tamaño = input("Tamaño de la salchicha en pulgadas: ") 

    if (nombre.isalpha() == False | verify_within_ingredients(nombre, salchichas) == True):
        print("\n[italic red] El nombre del ingrediente no debe contener números o caracteres especiales. Recuerde que el nombre debe ser único para cada ingrediente. Inténtelo de nuevo.\n")
        
        if (tipo.isalpha() == False):
            print("\n[italic red] El tipo del ingrediente no debe contener números o caracteres especiales. Inténtelo de nuevo.\n")
            registrar_salchicha(salchichas_app)

            if (tamaño.isdigit() == False):
                print("\n[italic red] El tamaño del ingrediente debe ser un número. Inténtelo de nuevo.\n")
                registrar_salchicha(salchichas_app)

    nueva_salchicha = Salchicha(nombre, tipo, tamaño, "pulgadas")
    agregar_ingrediente_categoria(salchichas, nueva_salchicha)
    print(f"\n[italic green] La salchicha {nueva_salchicha.nombre} ha sido registrada exitosamente.\n")

def registrar_salsa (salsas_app):
    """Función para registrar una nueva salsa
    """  
    print ("\n[italic blue]------------- Introduzca los detalles del ingrediente ------------- \n")  
    salsas = salsas_app
    nombre = input("Introduzca su nombre: ")  
    base = input("Introduzca la base: ") 
    color = input("Color: ")

    if (nombre.isalpha() == False | verify_within_ingredients(nombre, salsas) == True):
        print("\n[italic red] El nombre del ingrediente no debe contener números o caracteres especiales. Recuerde que el nombre debe ser único para cada ingrediente. Inténtelo de nuevo.\n")
        
        if (base.isalpha() == False):
            print("\n[italic red] La base del ingrediente no debe contener números o caracteres especiales. Inténtelo de nuevo.\n")
            registrar_salsa(salsas_app)

            if (color.isalpha() == False):
                print("\n[italic red] El color no debe contener números o caracteres especiales. Inténtelo de nuevo.\n")
                registrar_salsa(salsas_app)

    nueva_salsa = Salsa(nombre, base, color)
    agregar_ingrediente_categoria(nueva_salsa, salsas)
    print(f"\n[italic green] La salsa {nueva_salsa.nombre} ha sido registrado exitosamente.\n")

def registrar_topping (toppings_app):
    """Función para registrar una nueva salchicha
    """  
    print ("\n[italic blue]------------- Introduzca los detalles del ingrediente ------------- \n")  
    toppings = toppings_app
    nombre = input("Introduzca su nombre: ")  
    tipo = input("Introduzca el tipo: ") 
    presentacion = input("Tamaño de la salchicha en pulgadas: ") 

    if (nombre.isalpha() == False | verify_within_ingredients(nombre, toppings) == True):
        print("\n[italic red] El nombre del ingrediente no debe contener números o caracteres especiales. Recuerde que el nombre debe ser único para cada ingrediente. Inténtelo de nuevo.\n")
        
        if (tipo.isalpha() == False):
            print("\n[italic red] El tipo del ingrediente no debe contener números o caracteres especiales. Inténtelo de nuevo.\n")
            registrar_topping(toppings_app)

            if (presentacion.isalpha() == False):
                print("\n[italic red] La presentación no debe contener números o caracteres especiales. Inténtelo de nuevo.\n")
                registrar_topping(toppings_app)

    nuevo_topping = Toppings(nombre, tipo, presentacion)
    agregar_ingrediente_categoria(toppings, nuevo_topping)
print(f"\n[italic green] El topping {nuevo_topping.nombre} ha sido registrado exitosamente.\n")


# Funciones para eliminar ingredientes con validaciones

def eliminar_ingrediente_categoria(ingredientes: list, nombre_ingrediente, hotdogs_app):
    """Función para eliminar un ingrediente de la categoría correspondiente
    """
    hotdogs = encontrar_hotdog_ingredientes(hotdogs_app, nombre_ingrediente)

    if len(hotdogs) > 0:
        print(f"\n[italic red] No se puede eliminar el ingrediente {nombre_ingrediente} porque está siendo utilizado en los siguientes hotdogs:\n")
        for hotdog in hotdogs:
            print(hotdog.info_hotdog())
    
        while True:
            option = input ("""
            ¿Desea eliminar el ingrediente de todos modos? Esta acción eliminará el hotdog que lo contenga.
                                        
            1. Sí 
            2. No
                                                                
            ---> """)
                    
            if option =="1":
                eliminar_ingrediente
            elif option =="2":
                print ("[italic blue]Volviendo al menu...")
                break
            else:
                print ("[italic red]Opción inválida. ")

def encontrar_hotdog_ingredientes (hotdogs_app, ingrediente):
    """Función para encontrar hotdogs que contienen un ingrediente específico
    """  

    hotdogs = []

    for i in hotdogs_app:
        if (i.pan == ingrediente) or (i.salchicha == ingrediente) or (i.acompañante == ingrediente) or (verify_within_ingredients(ingrediente, i.salsas) == True) or (verify_within_ingredients(ingrediente, i.toppings) == True):
            hotdogs.append(i)
        else:
            pass

    return hotdogs

def eliminar_ingrediente (ingredientes_app, hotdogs_app, hotdogs: list, nombre_ingrediente):
    """Función para eliminar un ingrediente seleccionado
    """ 

    if hotdogs < 1:
        pass
    else:
        for i in hotdogs_app:
            for j in hotdogs:
                if i == j:
                    hotdogs_app.remove(i)
                else:
                    pass
    
    for i in ingredientes_app:
        if i.nombre == nombre_ingrediente:
            ingredientes_app.remove(i)
            print(f"\n[italic green] El ingrediente {nombre_ingrediente} ha sido eliminado exitosamente.\n")
        else:
            pass


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