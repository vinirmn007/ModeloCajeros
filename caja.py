class Caja:
    def __init__(self, tipo_cajero):
        self.tipo_cajero = tipo_cajero
        self.clientes = []

        # Tiempo de escaneo (según el PDF)
        if tipo_cajero == "principiante":
            self.tiempo_escaneo = 9
        elif tipo_cajero == "normal":
            self.tiempo_escaneo = 5
        else:
            raise ValueError("Tipo de cajero no válido")

    def agregar_cliente(self, cliente):
        cliente.set_t_escaneo(self.tiempo_escaneo)
        self.clientes.append(cliente)

    def calcular_tiempo_total(self):
        tiempo_total = 0
        # ¡IMPORTANTE! Esta es la lista para la animación
        tiempos_individuales = [] 
        
        for i, cliente in enumerate(self.clientes, start=1):
            tiempo_cliente = cliente.calcular_tiempo_total()
            
            # Guarda el tiempo de este cliente en la lista
            tiempos_individuales.append(tiempo_cliente)
            
            # Esto se verá en tu terminal MINGW64
            print(f"Cliente {i}: {cliente.get_articulos()} artículos - {cliente.get_tipo_pago()} - Tiempo total: {tiempo_cliente}s")
            
            tiempo_total += tiempo_cliente
            
        # --- ¡ESTA ES LA LÍNEA CLAVE! ---
        # Devuelve DOS valores: el total Y la lista
        return tiempo_total, tiempos_individuales