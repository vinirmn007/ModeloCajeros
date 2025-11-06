import sys
import os
from contextlib import redirect_stdout
import random

from caja import Caja
from utilidad import generar_clientes

def ejecutar_una_simulacion_silenciosa():
    """
    Ejecuta una ronda completa de la simulación SIN imprimir 
    los detalles de cada cliente.
    Devuelve el nombre de la caja ganadora.
    """
    try:
        caja1 = Caja('normal')
        caja2 = Caja('normal')
        caja3 = Caja('normal')
        caja4 = Caja('normal')

        caja_express = Caja('normal')

        generar_clientes(caja1, 10)
        generar_clientes(caja2, 10)
        generar_clientes(caja3, 10)
        generar_clientes(caja4, 10)
        generar_clientes(caja_express, 20, tipo="express")

        tiempos = {}

    
        with open(os.devnull, 'w') as f_null:
            with redirect_stdout(f_null):
                tiempos["Caja 1"] = caja1.calcular_tiempo_total()
                tiempos["Caja 2"] = caja2.calcular_tiempo_total()
                tiempos["Caja Express"] = caja_express.calcular_tiempo_total()
                tiempos["Caja 3"] = caja3.calcular_tiempo_total()
                tiempos["Caja 4"] = caja4.calcular_tiempo_total()
        
        mejor_caja = min(tiempos, key=tiempos.get)
        
        return mejor_caja

    except Exception as e:
        print(f"Error en una simulación: {e}", file=sys.stderr)
        return None

def ejecutar_simulacion_masiva(numero_de_rondas=100):
    print(f"--- 🏁 Iniciando {numero_de_rondas} simulaciones ---")

    conteo_victorias = {
        "Caja 1": 0,
        "Caja 2": 0,
        "Caja 3": 0,
        "Caja 4": 0,
        "Caja Express": 0
    }
    
    for i in range(numero_de_rondas):
        ganador = ejecutar_una_simulacion_silenciosa()
        
        if ganador:
            # ganador
            #print(f"Ronda {i + 1}: El ganador es 🟢 {ganador}")
            
            #contar victorias
            if ganador in conteo_victorias:
                conteo_victorias[ganador] += 1

    #resumen final
    print("\n---Resumen de Victorias---")
    for nombre, victorias in conteo_victorias.items():
        print(f"{nombre}: {victorias} victorias")

if __name__ == "__main__":
    ejecutar_simulacion_masiva(1000)