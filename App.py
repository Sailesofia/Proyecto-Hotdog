
from rich import print
import os
import sys

class App():
    """Es la encargada de abrir y gestionar todas las operaciones que se tienen que llevar a cabo para gestionar la aplicación.
    """

    def __init__(self):
        """Constructor de la clase App. Contiene todas las listas donde se almacena la información.
        
        self.hotdogs = Lista de todos los hotdogs registrados.
        self.pan = Lista de tipos de pan registrados en la sede.
        self.salchicha = Lista de salchichas registradas.
        self.salsa = Lista de salsas registradas.
        self.toppings = Lista de toppings disponibles.
        self.acompañantes = Lista de acompañantes registrados en la plataforma.
        
        """        
        self.hotdogs = []   
        self.pan =  []
        self.salchicha = []
        self.salsa = []
        self.toppings = []
        self.acompañantes = []
        self.resultados_simulaciones = []   #Lista de dia de ventas

                    
    def obtener_json_desde_url(self, url: str):
        """
        Obtiene y parsea el contenido JSON desde una URL.
        """
    
    def abrir_API (self): 
        """Función para crear objetos a partir de la API y almacenarlos en las listas de la instancia App.
        """ 

    def guardar_datos_json(self, nombre_archivo: str = "datos_hotdogs.json"):
        """
        Serializa toda la información disponible (ingredientes y hotdogs)
        y la guarda en un archivo JSON.
        """
 
    def cargar_datos_json(self, nombre_archivo: str = "datos_hotdogs.json"):
        """
        Lee el archivo JSON guardado y reconstruye los objetos de HotDogs e ingredientes 
        almacenándolos en las listas de la instancia App.
        """
     
    def gestion_ingredientes(self):
        """Funcion para llamar al módulo de gestión de ingredientes. 
        """        
        while True:
            option = input ("""
    ¿Qué desea realizar?
                                
    1. Listar todos los productos de una categoría 
    2. Listar todos los productos de un tipo dentro de una categoría
    3. Agregar un ingrediente
    4. Eliminar un ingrediente
    5. Regresar
                                                        
    ---> """)
            
            if option =="1":
                break
            elif option =="2":
                break
            elif option =="3":
                break
            elif option =="4":
                break
            elif option =="5":
                break
            else:
                print ("[italic red]Opción inválida")

    def ver_estadisticas (self):
        """Función para ver las estadisticas de las simulaciones. 
        """  
        

    def gestion_inventario(self):
        """Menu de las acciones del inventario.
        """        
        os.system('cls')

        while True:
            print ("\n[italic magenta]---------- Acciones ---------- ")
            listener_option = input ("""                            
    1. Visualizar todo el inventario 
    2. Buscar un ingrediente específico 
    3. Tipos de ingredientes por categoría
    4. Actualizar la existencia de un producto específico 
    5. Regresar
                                
    ---> """)
            if listener_option == "1":
                pass

            elif listener_option == "2":
                pass

            elif listener_option == "3":
                pass

            elif listener_option == "4":
                pass

            elif listener_option == "5":
                App.menu(self)
                break

            else:
                print("\n[italic red]Opción inválida. Introduzca una opción válida por favor.\n")


    def gestion_menu(self):
        """Menu para gestionar los hot dogs que se venden.
        """        
        os.system('cls')

        while True:
            print ("\n[italic magenta]---------- Acciones ---------- ")
            artist_option = input ("""                                                                 
    1. Ver hotdogs disponibles
    2. Ver inventario de un hotdog específico
    3. Agregar un hotdog
    4. Eliminar un hotdog
    5. Regresar
                        
    ---> """)

            if artist_option == "1":
                pass
                break
            elif artist_option == "2":
                pass
                break
            elif artist_option == "3":
                pass
                break
                
            elif artist_option == "4":
                break
            elif artist_option == "5":
                App.menu(self)
                break
            else:
                print("\n[italic red]Opción inválida. Introduzca una opción válida por favor.\n")
            

    def principal_menu(self):
        """Menu principal. Posee las acciones principales para gestionar el programa.
        """   

        while True:
            print ("\n[italic blue]---------- Acciones ---------- ")
            choice = input("""              
0. Cargar API                          
1. Cargar data de la aplicación                          
2. Gestionar ingredientes                                                                                                                       
3. Gestionar inventario                                                                                                                               
4. Gestionar menú                                             
5. Simulación de un día de ventas                                             
6. Ver estadísticas                                            
7. Guardar y salir                                                                          

---> """)
            
            if choice == "0":
                App.abrir_API(self)

            elif choice == "1":
                App.cargar_datos_json(self)
                print ("\n[italic green] ...Cargando datos\n")
                
            elif choice == "2":
                print ("\n[italic green] ...Accediendo a interfaz\n")
    
            elif choice == "3":
                print ("\n[italic green] ...Accediendo a interfaz\n")
                
            elif choice == "4":
                print ("\n[italic green] ...Accediendo a interfaz\n")

            elif choice == "5":
                print ("\n[italic green] ...Accediendo a interfaz\n")

            elif choice == "6":
                print ("\n[italic green] ...Accediendo a interfaz\n")

            elif choice == "7":
                App.guardar_datos_json(self)
                print ("\n[italic green]Cerrando programa...")
                sys.exit()
 
            else:
                print ("\n[italic red]Opción inválida\n")
                os.system('cls')

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def start_app(self):
        """Función para darle inicio al programa
        """            
        print ("\n[italic blue]Inicializando programa...")
        print ("""
[bold yellow]🌭🌭   Bienvenido a Hotdog   🌭🌭""")
        App.principal_menu(self)


