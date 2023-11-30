from math import sin, cos, sqrt, atan2, radians

# Função para calcular a distância entre dois pontos geográficos
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Raio da Terra em km
    raio_terra = 6371.0

    # Conversão de graus para radianos
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Diferença entre as longitudes e latitudes dos pontos
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Fórmula de Haversine para calcular a distância entre dois pontos
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = raio_terra * c

    return distancia

# Coordenadas do totem
totem_latitude = -15.828286
totem_longitude = -48.066610

# Coordenadas do restaurante (exemplo)
restaurante_latitude = -15.822093
restaurante_longitude = -48.053929

# Calcular a distância entre o totem e o restaurante
distancia = calcular_distancia(totem_latitude, totem_longitude, restaurante_latitude, restaurante_longitude)
print(f"A distância entre o totem e o restaurante é aproximadamente {distancia:.2f} km.")