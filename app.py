from flask import Flask, jsonify, request, render_template 
from flask_cors import CORS
from caja import Caja
from utilidad import generar_clientes

app = Flask(__name__)
CORS(app) 

@app.route('/')
def index():
    return render_template('simulacion.html')



def ejecutar_simulacion_caja(cantidad, tipo_cajero="normal", tipo_cliente="normal"):
    caja_simulada = Caja(tipo_cajero)   
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
    n1 = int(request.args.get('n1', 0))
    tipo1 = request.args.get('tipo1', 'normal') 
    
    n2 = int(request.args.get('n2', 0))
    tipo2 = request.args.get('tipo2', 'normal') 
    
    n3 = int(request.args.get('n3', 0))
    tipo3 = request.args.get('tipo3', 'normal') 
    
    n4 = int(request.args.get('n4', 0))
    tipo4 = request.args.get('tipo4', 'normal') 
    

    
    n_exp = int(request.args.get('n_exp', 0))
    tipo_exp = request.args.get('tipo_exp', 'normal') 

    
    tiempos1, arts1, total1 = ejecutar_simulacion_caja(n1, tipo1)
    tiempos2, arts2, total2 = ejecutar_simulacion_caja(n2, tipo2)
    tiempos3, arts3, total3 = ejecutar_simulacion_caja(n3, tipo3)
    tiempos4, arts4, total4 = ejecutar_simulacion_caja(n4, tipo4)

    
    tiempos_exp, arts_exp, total_exp = ejecutar_simulacion_caja(n_exp, tipo_exp, "express")
    
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