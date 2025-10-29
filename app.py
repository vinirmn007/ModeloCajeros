# Importamos 'render_template' para servir el HTML
from flask import Flask, jsonify, request, render_template # <--- ¡LÍNEA MODIFICADA!
from flask_cors import CORS

# Importamos tus clases y funciones exactas
from caja import Caja

from utilidad import generar_clientes

app = Flask(__name__)
CORS(app) 

# --- ¡NUEVA RUTA AÑADIDA! ---
@app.route('/')
def index():
    """Esta ruta servirá tu archivo simulacion.html"""
    return render_template('simulacion.html')
# -----------------------------


def ejecutar_simulacion_caja(cantidad, tipo_cajero="normal", tipo_cliente="normal"):
    """
    Esta función usa tus clases originales para simular una caja
    y devolver los datos que el frontend necesita.
    """
    caja_simulada = Caja("normal") 
    generar_clientes(caja_simulada, cantidad, tipo=tipo_cliente)

    tiempos_individuales = []
    articulos_individuales = []
    
    for cliente in caja_simulada.clientes:
        tiempo_cliente = cliente.calcular_tiempo_total()
        articulos_cliente = cliente.get_articulos()
        
        tiempos_individuales.append(tiempo_cliente)
        articulos_individuales.append(articulos_cliente)

    tiempo_total = sum(tiempos_individuales)
    
    return tiempos_individuales, articulos_individuales, tiempo_total


@app.route('/simular', methods=['GET'])
def simular():
    """Esta es tu API, no cambia nada."""
    n1 = int(request.args.get('n1', 0))
    n2 = int(request.args.get('n2', 0))
    n3 = int(request.args.get('n3', 0))
    n4 = int(request.args.get('n4', 0))
    n_exp = int(request.args.get('n_exp', 0))

    tiempos1, arts1, total1 = ejecutar_simulacion_caja(n1, "normal") #cambiar a principiante
    tiempos2, arts2, total2 = ejecutar_simulacion_caja(n2, "normal")
    tiempos3, arts3, total3 = ejecutar_simulacion_caja(n3, "normal")
    tiempos4, arts4, total4 = ejecutar_simulacion_caja(n4, "normal")
    tiempos_exp, arts_exp, total_exp = ejecutar_simulacion_caja(n_exp, "normal", "express")
    
    datos_simulacion = {
        "caja1": {"tiempos": tiempos1, "articulos": arts1},
        "caja2": {"tiempos": tiempos2, "articulos": arts2},
        "caja3": {"tiempos": tiempos3, "articulos": arts3},
        "caja4": {"tiempos": tiempos4, "articulos": arts4},
        "caja_express": {"tiempos": tiempos_exp, "articulos": arts_exp}
    }
    
    totales = {
        "Caja 1": total1,
        "Caja 2": total2,
        "Caja 3": total3,
        "Caja 4": total4,
        "Caja Express": total_exp,
    }

    return jsonify({
        "plan_simulacion": datos_simulacion,
        "totales_backend": totales
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)