import random   

class Caja:
    def __init__(self, tipo_cajero):
        self.tipo_cajero = tipo_cajero
        self.clientes = []

        # Definir tiempo de escaneo según tipo
        if tipo_cajero == "principiante":
            self.tiempo_escaneo = random.randint(5, 9)
        elif tipo_cajero == "normal":
            self.tiempo_escaneo = random.randint(2, 5)
        else:
            raise ValueError("Tipo de cajero no válido")

    def agregar_cliente(self, cliente):
        cliente.set_t_escaneo(self.tiempo_escaneo)
        self.clientes.append(cliente)

    def calcular_tiempo_total(self):
        tiempo_total = 0
        for i, cliente in enumerate(self.clientes, start=1):
            tiempo_cliente = cliente.calcular_tiempo_total()
            print(f"Cliente {i}: {cliente.get_articulos()} artículos - {cliente.get_tipo_pago()} - Tiempo total: {tiempo_cliente}s")
            tiempo_total += tiempo_cliente
        return tiempo_total
