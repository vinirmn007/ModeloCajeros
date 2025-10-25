from cliente import Cliente
from cliente_expres import ClienteExpres

def generar_clientes(caja, cantidad, tipo="normal"):
    for _ in range(cantidad):
        if tipo == "express":
            cliente = ClienteExpres()
            cliente.set_articulos()  # entre 1 y 10
        else:
            cliente = Cliente()
            cliente.set_articulos()  # entre 1 y 50
        caja.agregar_cliente(cliente)