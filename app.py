from flask import Flask, render_template, request, jsonify

# --- Importamos tu lógica existente ---
from caja import Caja
from cliente import Cliente
from cliente_express import ClienteExpress 
from utilidad import generar_clientes

# --- Lógica de Simulación (MODIFICADA) ---
def ejecutar_simulacion(n1, n2, n3, n4, n_express, tipo1, tipo2, tipo3, tipo4, tipo_express):
    
    # 1. Crear las cajas (¡USA EL TIPO SELECCIONADO!)
    caja1 = Caja(tipo1) # ej: 'normal' o 'principiante'
    caja2 = Caja(tipo2)
    caja3 = Caja(tipo3)
    caja4 = Caja(tipo4)
    caja_express = Caja(tipo_express) 

    # 2. Asignar clientes
    generar_clientes(caja1, n1)
    generar_clientes(caja2, n2)
    generar_clientes(caja_express, n_express, tipo="express")
    generar_clientes(caja3, n3)
    generar_clientes(caja4, n4)

    # 4. Calcular tiempos
    tiempo1_total, tiempos1_lista = caja1.calcular_tiempo_total()
    tiempo2_total, tiempos2_lista = caja2.calcular_tiempo_total()
    tiempo_express_total, tiempos_express_lista = caja_express.calcular_tiempo_total()
    tiempo3_total, tiempos3_lista = caja3.calcular_tiempo_total()
    tiempo4_total, tiempos4_lista = caja4.calcular_tiempo_total()

    # 5. Preparar diccionario de resultados para el HTML
    tiempos = {
        # Añadimos el tipo de cajero al nombre
        f"Caja 1 ({tipo1})": {
            "tiempo_total_seg": tiempo1_total,
            "personas_iniciales": n1,
            "tiempos_clientes": tiempos1_lista 
        },
        f"Caja 2 ({tipo2})": {
            "tiempo_total_seg": tiempo2_total,
            "personas_iniciales": n2,
            "tiempos_clientes": tiempos2_lista
        },
        f"Caja Express ({tipo_express})": {
            "tiempo_total_seg": tiempo_express_total,
            "personas_iniciales": n_express,
            "tiempos_clientes": tiempos_express_lista
        },
        f"Caja 3 ({tipo3})": {
            "tiempo_total_seg": tiempo3_total,
            "personas_iniciales": n3,
            "tiempos_clientes": tiempos3_lista
        },
        f"Caja 4 ({tipo4})": {
            "tiempo_total_seg": tiempo4_total,
            "personas_iniciales": n4,
            "tiempos_clientes": tiempos4_lista
        }
    }
    
    # Encontrar el mejor
    mejor_caja = min(tiempos, key=lambda k: tiempos[k]["tiempo_total_seg"])
    
    return tiempos, mejor_caja
# -----------------------------------------------


# --- Configuración de Flask ---
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/simular', methods=['POST'])
def simular():
    try:
        # Leemos la cantidad de personas
        n1 = int(request.form['n_caja1'] or 0)
        n2 = int(request.form['n_caja2'] or 0)
        n3 = int(request.form['n_caja3'] or 0)
        n4 = int(request.form['n_caja4'] or 0)
        n_express = int(request.form['n_express'] or 0)

        # Leemos el tipo de cajero para cada caja
        tipo1 = request.form['tipo_caja1']
        tipo2 = request.form['tipo_caja2']
        tipo3 = request.form['tipo_caja3']
        tipo4 = request.form['tipo_caja4']
        tipo_express = request.form['tipo_express']

        # Pasamos todos los valores
        tiempos, mejor = ejecutar_simulacion(
            n1, n2, n3, n4, n_express,
            tipo1, tipo2, tipo3, tipo4, tipo_express
        )
        
        return render_template('index.html', tiempos=tiempos, mejor=mejor)

    except ValueError:
        error_msg = "Error: Por favor, ingrese números válidos."
        return render_template('index.html', error=error_msg)

if __name__ == '__main__':
    app.run(debug=True)