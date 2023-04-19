import requests
from bs4 import BeautifulSoup
import json

# Hago un GET a la página de los valores UF y guardo la salida HTML en una variable 'r'
r = requests.get("https://www.sii.cl/valores_y_fechas/uf/uf2022.htm")

#print(r.text)

# Creo una instancia de BeautifulSoup pasandole el HTML y especificandole el tipo de parseo (HTML.parser)
soup = BeautifulSoup(r.text, 'html.parser')

# Encuentra la tabla correspondiente en el HTML
tabla_uf = soup.find('table', {'id': 'table_export'})



# Encuentra la fila de la tabla que contiene el valor de UF buscado
fila_uf = tabla_uf.find('th', string='29').find_parent('tr')
#print(fila_uf)


#Encuentra todas las celdas de la fila
celdas = fila_uf.find_all('td')

#Encuentra el valor de UF específico en la fila
valor_uf = float(celdas[0].get_text().replace('.', '').replace(',', '.'))

print(valor_uf)

#print(valor_uf)

# Imprime el valor de UF
#print(valor_uf)

