import requests
import json

# Acceso a la API
api_key = "live_lsujRjQIXajmXvsff3eTQIXNw34C73kU2Uo23obdu8M0tA1m6drKwDbGVZgEIPHR"
url = f"https://api.thecatapi.com/v1/images/search?limit=10&api_key=%7Bapi_key%7D"
headers = {'Content-Type': 'application/json'}
response = requests.get(url, headers=headers)

# Procesamiento de datos
if response.status_code == 200:
    data = json.loads(response.text)
    # Mezcla de datos estructurados y no estructurados
    for item in data:
        print("ID:", item['id'])
        img_url = item['url']
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img_data = img_response.content
            # Procesamiento de datos no estructurados
            # Guardar la imagen en un archivo
            with open(item['id'] + ".jpg", "wb") as img_file:
                img_file.write(img_data)
        else:
            print("Error al obtener la imagen")
else:
    print("Error al acceder a la API")