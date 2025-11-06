from cliente import Cliente
import random

class ClienteExpres(Cliente): 
    def __init__(self):
        super().__init__() 

    def set_articulos(self):
        self.articulos = random.randint(1, 10)