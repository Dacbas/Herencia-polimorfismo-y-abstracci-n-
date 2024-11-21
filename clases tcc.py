
#Herencia y polimorfismo aqui:
class Servicio:

    def __init__(self, idServicio, descripcion, costo):
        self.idServicio = idServicio
        self.descripcion = descripcion
        self.costo = costo

    def __str__(self):
        return f"Servicio[ID: {self.idServicio}, Descripción: {self.descripcion}, Costo: {self.costo}]"

class ServicioReparacion(Servicio):
    def __init__(self, idServicio, descripcion, costo):
        self.idServicio = idServicio
        self.descripcion = descripcion
        self.costo = costo      

class ServicioSoporteIT(Servicio):
    def __init__(self, idServicio, descripcion, costo):
        self.idServicio = idServicio
        self.descripcion = descripcion
        self.costo = costo
