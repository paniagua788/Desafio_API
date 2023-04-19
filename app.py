import requests
from bs4 import BeautifulSoup
import json

# Hago un GET a la página de los valores UF y guardo la salida HTML en una variable 'r'
r = requests.get("https://www.sii.cl/valores_y_fechas/uf/uf2023.htm")

#print(r.text)


