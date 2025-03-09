import requests
import os
from urllib.parse import urlparse

# Crear el directorio de imágenes si no existe
if not os.path.exists('images'):
    os.makedirs('images')

# Lista de imágenes a descargar (usando Pexels)
imagenes = {
    # Flores existentes
    'rosa-roja': 'https://images.pexels.com/photos/56866/garden-rose-red-pink-56866.jpeg',
    'rosa-rosa': 'https://images.pexels.com/photos/39517/rose-flower-blossom-bloom-39517.jpeg',
    'tulipan-rosa': 'https://images.pexels.com/photos/1083822/pexels-photo-1083822.jpeg',
    'margarita': 'https://images.pexels.com/photos/67857/daisy-flower-spring-marguerite-67857.jpeg',
    'margarita-rosa': 'https://images.pexels.com/photos/1166869/pexels-photo-1166869.jpeg',
    'girasol': 'https://images.pexels.com/photos/46216/sunflower-flowers-bright-yellow-46216.jpeg',
    'orquidea': 'https://images.pexels.com/photos/5766927/pexels-photo-5766927.jpeg',  # Nueva URL para orquídea
    
    # Nuevas imágenes decorativas
    'hoja1': 'https://images.pexels.com/photos/2249959/pexels-photo-2249959.jpeg',
    'hoja2': 'https://images.pexels.com/photos/1048035/pexels-photo-1048035.jpeg',
    'hoja3': 'https://images.pexels.com/photos/1407305/pexels-photo-1407305.jpeg',
    'lazo': 'https://images.pexels.com/photos/1037992/pexels-photo-1037992.jpeg',  # Nueva URL para lazo
    'brillo': 'https://images.pexels.com/photos/234272/pexels-photo-234272.jpeg'   # Nueva URL para brillo
}

def descargar_imagen(url, nombre):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            ruta_archivo = os.path.join('images', f'{nombre}.png')
            with open(ruta_archivo, 'wb') as f:
                f.write(response.content)
            print(f'✓ Imagen descargada: {nombre}')
        else:
            print(f'✗ Error al descargar {nombre}: {response.status_code}')
    except Exception as e:
        print(f'✗ Error al procesar {nombre}: {str(e)}')

# Descargar todas las imágenes
print('Descargando imágenes...')
for nombre, url in imagenes.items():
    descargar_imagen(url, nombre)

print('\n¡Descarga completada! Las imágenes se han guardado en la carpeta "images"') 