from cliente import Cliente
import random

class ClienteExpres(Cliente):
    def __init__(self):
        super().__init__() 


    def set_articulos(self):
        #entre 1 y 10 artículos
        self.articulos = random.randint(1, 10)