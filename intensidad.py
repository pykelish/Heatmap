import numpy as np
from scipy.stats import gaussian_kde

# Tus datos de ejemplo (varios puntos)
latitude = [24.134754344857537, 24.136003105594042, 24.136726223669292, 24.1354276268424]
longitude = [-110.42728494986633, -110.42534242145408, -110.4267442862976, -110.428223772566]

# Preparar los datos para el KDE (apilar latitudes y longitudes)
data = np.vstack([latitude, longitude])

# Crear el objeto gaussian_kde
kde = gaussian_kde(data)

# Coordenada específica para la cual queremos calcular la intensidad
punto = np.array([24.135837305821877, -110.42623237443854])  # Por ejemplo, una nueva coordenada

# Calcular la intensidad (densidad) en ese punto
intensidad = kde(punto)  # Devuelve la densidad estimada

# Mostrar la intensidad
print(f'La intensidad en el punto {punto} es: {intensidad[0]}')
