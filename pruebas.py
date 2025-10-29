import sys
import os
from contextlib import redirect_stdout
import random

# Importa tus clases y funciones existentes
from caja import Caja
from utilidad import generar_clientes

def ejecutar_una_simulacion_silenciosa():
    """
    Ejecuta una ronda completa de la simulación SIN imprimir 
    los detalles de cada cliente.
    Devuelve el nombre de la caja ganadora.
    """
    try:
        # 1. Configuración de cajas (igual que en tu script)
        caja1 = Caja('normal')
        caja2 = Caja('normal')
        caja3 = Caja('normal')
        caja4 = Caja('principiante')

        caja_express = Caja('normal') #random.choice(["normal", "principiante"])

        # 2. Generar clientes (igual que en tu script)
        # (Esta función 'generar_clientes' no imprime nada, 
        # así que puede ejecutarse normalmente)
        generar_clientes(caja1, 10)
        generar_clientes(caja2, 10)
        generar_clientes(caja3, 10)
        generar_clientes(caja4, 10)
        generar_clientes(caja_express, 20, tipo="express")

        tiempos = {}

        # 3. Calcular tiempos (AQUÍ ESTÁ LA MAGIA)
        # Usamos 'os.devnull' como un "agujero negro" para
        # descartar todas las sentencias 'print' que ocurran
        # dentro de este bloque 'with'.
        
        with open(os.devnull, 'w') as f_null:
            with redirect_stdout(f_null):
                # Estas llamadas a .calcular_tiempo_total()
                # intentarán imprimir, pero todo se irá a f_null.
                tiempos["Caja 1"] = caja1.calcular_tiempo_total()
                tiempos["Caja 2"] = caja2.calcular_tiempo_total()
                tiempos["Caja Express"] = caja_express.calcular_tiempo_total()
                tiempos["Caja 3"] = caja3.calcular_tiempo_total()
                tiempos["Caja 4"] = caja4.calcular_tiempo_total()
        
        # 4. Determinar ganador (igual que en tu script)
        mejor_caja = min(tiempos, key=tiempos.get)
        
        return mejor_caja

    except Exception as e:
        # Es bueno saber si una de las 100 simulaciones falla
        print(f"Error en una simulación: {e}", file=sys.stderr)
        return None

# --- Función Principal ---
def ejecutar_simulacion_masiva(numero_de_rondas=100):
    """
    Ejecuta la simulación silenciosa el número de veces
    especificado e imprime al ganador de cada ronda.
    """
    
    print(f"--- 🏁 Iniciando {numero_de_rondas} simulaciones ---")
    
    # Un diccionario para llevar la cuenta de las victorias
    conteo_victorias = {
        "Caja 1": 0,
        "Caja 2": 0,
        "Caja 3": 0,
        "Caja 4": 0,
        "Caja Express": 0
    }
    
    # 1. El bucle de 100 ejecuciones
    for i in range(numero_de_rondas):
        ganador = ejecutar_una_simulacion_silenciosa()
        
        if ganador:
            # 2. Imprimir solo el ganador de la ronda (como pediste)
            print(f"Ronda {i + 1}: El ganador es 🟢 {ganador}")
            
            # 3. Contar la victoria
            if ganador in conteo_victorias:
                conteo_victorias[ganador] += 1

    # 4. Mostrar un resumen final
    print("\n--- 🏆 Resumen de Victorias (de 100 simulaciones) ---")
    for nombre, victorias in conteo_victorias.items():
        print(f"{nombre}: {victorias} victorias")


# --- Punto de entrada ---
if __name__ == "__main__":
    ejecutar_simulacion_masiva(100)