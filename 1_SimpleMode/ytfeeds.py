import requests
import re
import pandas as pd

def obtener_info_canales_youtube(urls):
    data = []
    
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            original_url = url
            match = re.search(r'type="application/rss\+xml" title="RSS" href="(.+?)"', response.text)
            if match:
                rss_url = match.group(1)
                data.append({'originalUrl': original_url, 'rssUrl': rss_url})
            else:
                data.append({'originalUrl': original_url, 'rssUrl': ''})
        else:
            data.append({'originalUrl': url, 'rssUrl': ''})
    
    dataframe = pd.DataFrame(data)
    return dataframe

# Ejemplo de uso
urls = [
    "https://www.youtube.com/@LocosporLinux",
    "https://www.youtube.com/@OfficeMilMil",
    "https://www.youtube.com/@espndeportes",
    "https://www.youtube.com/@LinusTechTips",
]

dataframe_resultado = obtener_info_canales_youtube(urls)

# Directorio para guardar el archivo
directorio = '~/'

# Nombre del archivo
nombre_archivo = 'rssfeed.csv'

# Ruta completa del archivo
ruta_archivo = directorio + nombre_archivo

# Guardar el dataframe en un archivo CSV en el directorio especificado
dataframe_resultado.to_csv(ruta_archivo, index=False)

print(f"El dataframe se ha guardado en el archivo: {ruta_archivo}")
