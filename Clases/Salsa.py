
class Salsa():
    
    def __init__(self, nombre: str, base: str, color: str):
        """"Constructor de la clase Salsa
        """
        self.id = id
        self.nombre = nombre
        self.base = base
        self.color = color
        self.stock = 1
    
    def dar_stock(self):
        """Función para obtener el stock de la salsa
        """
        if self.stock <= 0:
            return "No disponible"
        else:
            return "Disponible"
        
    def info_salsa(self):
        """Función para obtener la información de la salsa
        """        
        info = {
            "Nombre": self.nombre,
            "Base": self.base,
            "Color": self.color,
            "Stock": self.dar_stock()
        }
        return info