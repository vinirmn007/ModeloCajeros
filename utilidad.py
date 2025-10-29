<<<<<<< HEAD
from cliente import Cliente
from cliente_express import ClienteExpress 

def generar_clientes(caja, cantidad, tipo="normal"):
    """
    Genera una cantidad de clientes y los agrega a una caja.
    """
    for _ in range(cantidad):
        if tipo == "express":
            cliente = ClienteExpress()
        else:
            cliente = Cliente()
            
        cliente.set_articulos() 
        
=======
from cliente import Cliente
from cliente_express import ClienteExpres

def generar_clientes(caja, cantidad, tipo="normal"):
    for _ in range(cantidad):
        if tipo == "express":
            cliente = ClienteExpres()
            cliente.set_articulos()  # entre 1 y 10
        else:
            cliente = Cliente()
            cliente.set_articulos()  # entre 1 y 50
>>>>>>> c6601120c11d8d736bc00e67922cf509b4982c0a
        caja.agregar_cliente(cliente)