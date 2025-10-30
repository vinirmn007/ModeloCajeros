import random

class Cliente:
    def __init__(self):
        self.articulos = 0
        self.tiempo_escaneo = 0
        self.tipo_pago = random.choice(["efectivo", "tarjeta"])
        self.set_articulos()

    # Setters y getters
    def set_articulos(self):
        self.articulos = random.randint(1, 40)
    
    def set_t_escaneo(self, t_escaneo):
        self.tiempo_escaneo = t_escaneo

    def get_tipo_pago(self):
        return self.tipo_pago

    def get_articulos(self):
        return self.articulos

    def t_cobro(self):
        if self.tipo_pago == "efectivo":
            return random.randint(5, 30)
        if self.tipo_pago == "tarjeta":
            return random.randint(5, 10)
        
    # Cálculo del tiempo total del cliente
    def calcular_tiempo_total(self):
        t_escaneo = self.articulos * self.tiempo_escaneo
        t_cobro = self.t_cobro()
        return t_escaneo + t_cobro
