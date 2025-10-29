
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
        
