
class Toppings():
    
    def __init__(self, nombre: str, tipo: str, presentacion: str):

        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.presentacion = presentacion
        self.stock = 1

    def dar_stock(self):
        """Función para obtener el stock de la salsa
        """
        if self.stock <= 0:
            return "No disponible"
        else:
            return "Disponible"
        
    def info_topping(self):
        """Función para obtener la información de la salsa
        """        
        info = {
            "Nombre": self.nombre,
            "Tipo": self.tipo,
            "Presentacion": self.presentacion,
            "Stock": self.dar_stock()
        }
        return info