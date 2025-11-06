from caja import Caja

from utilidad import generar_clientes

try:
    caja1 = Caja('normal')
    caja2 = Caja('normal')
    caja3 = Caja('normal')
    caja4 = Caja('normal')
    caja_express = Caja("normal") 

    generar_clientes(caja1, 10)
    generar_clientes(caja2, 10)
    generar_clientes(caja3, 10)
    generar_clientes(caja4, 10)
    generar_clientes(caja_express, 25, tipo="express")

    #calcular tiempos
    print("\n--- Detalle de atención Caja 1 ---")
    tiempo1 = caja1.calcular_tiempo_total()
    print("\n--- Detalle de atención Caja 2 ---")
    tiempo2 = caja2.calcular_tiempo_total()
    print("\n--- Detalle de atención Caja Express ---")
    tiempo_express = caja_express.calcular_tiempo_total()
    print("\n--- Detalle de atención Caja 3 ---")
    tiempo3 = caja3.calcular_tiempo_total()
    print("\n--- Detalle de atención Caja 4 ---")
    tiempo4 = caja4.calcular_tiempo_total()

    #resultados finales
    print("\n=== RESULTADOS FINALES ===")
    minutos1 = tiempo1 // 60
    minutos2 = tiempo2 // 60
    minutos_express = tiempo_express // 60
    minutos3 = tiempo3 // 60
    minutos4 = tiempo4 // 60


    print(f"Caja 1: {tiempo1}s → {minutos1} min")
    print(f"Caja 2: {tiempo2}s → {minutos2} min")
    print(f"Caja Express: {tiempo_express}s → {minutos_express} min")
    print(f"Caja 3: {tiempo3}s → {minutos3} min")
    print(f"Caja 4: {tiempo4}s → {minutos4} min")

 
    
    tiempos = {
        "Caja 1": tiempo1,
        "Caja 2": tiempo2,
        "Caja Express": tiempo_express,
        "Caja 3": tiempo3,
        "Caja 4": tiempo4
    }
    mejor = min(tiempos, key=tiempos.get)
    print(f"\n🟢 La mejor opción para un nuevo cliente es: {mejor}")

except:
    print("Ha ocurrido un error en la simulación.")