from cliente import Cliente
import random

class ClienteExpres(Cliente): 
    def __init__(self):
        super().__init__() 

    def set_articulos(self):
        # Límite de 10 artículos (según el PDF)
        self.articulos = random.randint(1, 10)