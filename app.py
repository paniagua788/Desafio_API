import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

def validar_fecha(fecha):
     # Retornamos mensajes en caso de que la fecha proporcionada este fuera del rango aceptado
    if fecha.year < 2013:
        raise ValueError("Fecha inválida: Sólo se muestran los valores desde 2013 en adelante")
    elif fecha.year > datetime.today().year:
        raise ValueError("Fecha inválida: No se muestran valores de años posteriores al actual.")

def validar_valor(valor):
    # En caso de que se consulte un valor que aun no esta cargado en la tabla
    valor = valor.strip()
    if not valor:
        return "Valor aún no registrado"
    else:
        return valor

@app.route('/uf', methods=['GET'])
def obtener_UF():
    # Obtengo el parámetro fecha de la url
    fecha =request.args.get("fecha")
    fecha_dt= datetime.strptime(fecha, "%Y-%m-%d")
    
    # Llamamos a una funcion para validar la fecha antes de continuar
    validar_fecha(fecha_dt)

    anio= fecha_dt.year
    dia= fecha_dt.day
    mes= fecha_dt.month

    
    
    # Hace un GET a la página de los valores UF y guardo la salida HTML en una variable 'r'
    r = requests.get(f"https://www.sii.cl/valores_y_fechas/uf/uf{anio}.htm")

    # Se crea una instancia de BeautifulSoup pasandole el HTML y especificandole el tipo de parseo (HTML.parser)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Encuentra la tabla correspondiente en el HTML
    tabla_uf = soup.find('table', {'id': 'table_export'})

    # Encuentra la fila de la tabla que contiene el valor de UF buscado
    fila_uf = tabla_uf.find('th', string= dia).find_parent('tr')

    #Encuentra todas las celdas de la fila
    celdas = fila_uf.find_all('td')

    #Encuentra el valor de UF específico en la fila
    valor_uf = celdas[mes-1].get_text().replace('.', '').replace(',', '.')
    valor_uf = validar_valor(valor_uf)

    # Creamos un diccionario con la fecha y su valor UF correspondiente, para luego convertirlo a JSON y retornar
    UF_info= {"Fecha": fecha, "Valor de UF" : valor_uf}
    return jsonify(UF_info)


#Lanzamos la app Flask en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True)