import requests
from bs4 import BeautifulSoup

# URL de la publicación
url = 'https://articulo.mercadolibre.com.ar/MLA-800947708-lora-sx1276-esp32-bt-wifi-kit-desarrollo-con-display-arduino-_JM'

# Hacer la solicitud a la página
response = requests.get(url)

# Analizar el HTML de la página
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('h1', class_='ui-pdp-title').text
price = soup.find('span', class_='andes-money-amount__fraction').text
stock = soup.find('span', class_="ui-pdp-buybox__quantity__available").text

# Extraer la información deseada
print(title)
print(price)
print(stock)
