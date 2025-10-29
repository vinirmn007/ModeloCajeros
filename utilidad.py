from cliente import Cliente
from cliente_expres import ClienteExpres

def generar_clientes(caja, cantidad, tipo="normal"):
    for _ in range(cantidad):
        if tipo == "express":
            cliente = ClienteExpres()
        else:
            cliente = Cliente()
        caja.agregar_cliente(cliente)
