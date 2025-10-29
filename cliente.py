import random

class Cliente:
    def __init__(self):
        self.articulos = 0
        self.tiempo_escaneo = 0
        self.tipo_pago = random.choice(["efectivo", "tarjeta"])
        # NO llamamos a set_articulos() aquí

    # Setters y getters
    def set_articulos(self):
        # Aleatorio entre 1 y 50 (según el PDF)
        self.articulos = random.randint(1, 50)
    
    def set_t_escaneo(self, t_escaneo):
        self.tiempo_escaneo = t_escaneo

    def get_tipo_pago(self):
        return self.tipo_pago

    def get_articulos(self):
        return self.articulos

    def t_cobro(self):
        # Aleatorio entre 15 y 30 (según el PDF)
        return random.randint(15, 30) 
        
    def calcular_tiempo_total(self):
        t_escaneo = self.articulos * self.tiempo_escaneo
        t_cobro = self.t_cobro()
        return t_escaneo + t_cobro