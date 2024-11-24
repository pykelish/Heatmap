import folium
from folium.plugins import HeatMap
from scipy.stats import gaussian_kde
import numpy as np

# Tus datos de ejemplo
latitude = [24.134754344857537, 24.135495355880455, 24.136726223669292, 24.1354276268424]
longitude = [-110.42728494986633, -110.42484175916617, -110.4267442862976, -110.428223772566]
intensity = []

data = np.vstack([latitude, longitude])
kde = gaussian_kde(data)

for i in range(len(latitude)):
    punto = np.array([latitude[i], longitude[i]])
    intensidad = kde(punto)  
    intensity.append(intensidad[0])

# Filtrar los datos para los puntos específicos
heat_data = [[lat, lon, inten] for lat, lon, inten in zip(latitude, longitude, intensity)]


# Crear el mapa base centrado en el área de los 4 puntos
mapa = folium.Map(
    location=[24.135837305821877, -110.42623237443854], # Centrado en los 4 puntos
    zoom_start=17,                                      # Zoom inicial más cercano
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="ESRI"
)

# Agregar HeatMap con gradiente y tamaño constante para los puntos
HeatMap(
    heat_data,
    radius=80,            # Radio fijo para los puntos
    blur=15,              # Desenfoque entre los puntos
    max_zoom=18,          # Aumentar el zoom máximo
    min_opacity=0.5,      # Opacidad mínima para que las áreas de baja intensidad sean visibles
    gradient={            # Gradiente personalizado de colores
        0.0: 'blue',
        0.5: 'lime',
        1.0: 'red'
    }
).add_to(mapa)

# Guardar y mostrar
mapa.save('heatmap.html')
print("Si se guardo el mapa")
