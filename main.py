import numpy as np

    # Genera una secuencia de 0s y 1s con patrones repetitivos exponenciales
def generar_combinaciones_exponenciales(n):
    combinacion = []
    for i in range(n):
        repeticion = 2**i
        array = np.tile([0] * repeticion + [1] * repeticion, 2**(n - i - 1))
        combinacion.append(array)
    return combinacion


    """ Identifica las posiciones de los valores 0 y 1 en una combinación binaria.
        -Args: combinacion (list): Lista de 0s y 1s.
        -Returns: tuple: Dos listas, la primera con las posiciones de los 0s y la segunda con las posiciones de los 1s. """
def identificar_posiciones(combinacion):
    
    vector_0 = []  # Almacena las posiciones de 0
    vector_1 = []  # Almacena las posiciones de 1

    # Recorrer la combinación y almacenar las posiciones
    for index, value in enumerate(combinacion):
        if value == 0:
            vector_0.append(index)  # Guardar posición de 0
        elif value == 1:
            vector_1.append(index)  # Guardar posición de 1

    return vector_0, vector_1

    """ Suma las columnas de la matriz basándose en la combinación binaria. 
        -Args: matriz (np.ndarray): La matriz de entrada. combinacion (list): Lista de 0s y 1s.
        -Returns: np.ndarray: Nueva matriz con las sumas de las columnas correspondientes. """
def sumar_columnas_por_combinacion(matriz, combinacion):

    # Identificar posiciones
    vector_0, vector_1 = identificar_posiciones(combinacion)

    # Crear una nueva matriz para almacenar los resultados
    filas = matriz.shape[0]
    nueva_matriz = np.zeros((filas, 2))

    # Sumar las columnas correspondientes a 0 y 1
    nueva_matriz[:, 0] = matriz[:, vector_0].sum(axis=1)  # Sumar columnas correspondientes a 0
    nueva_matriz[:, 1] = matriz[:, vector_1].sum(axis=1)  # Sumar columnas correspondientes a 1

    return nueva_matriz
# Crear una matriz de 16x16 
trans_matrix = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    ])
""""
combinaciones = [
    (0, 0, 0, 0), 
    (1, 0, 0, 0), 
    (0, 1, 0, 0), 
    (1, 1, 0, 0),
    (0, 0, 1, 0), 
    (1, 0, 1, 0), 
    (0, 1, 1, 0), 
    (1, 1, 1, 0),
    (0, 0, 0, 1), 
    (1, 0, 0, 1), 
    (0, 1, 0, 1), 
    (1, 1, 0, 1),
    (0, 0, 1, 1), 
    (1, 0, 1, 1), 
    (0, 1, 1, 1), 
    (1, 1, 1, 1)
]
"""
n = 4  # Nivel de profundidad
combinaciones = generar_combinaciones_exponenciales(n)

matrizCondicionalAt1 = sumar_columnas_por_combinacion(trans_matrix, combinaciones[0])
matrizCondicionalAt2 = sumar_columnas_por_combinacion(trans_matrix, combinaciones[1])
matrizCondicionalAt3 = sumar_columnas_por_combinacion(trans_matrix, combinaciones[2])
print("Nueva matriz:\n", matrizCondicionalAt1)
print("Nueva matriz:\n", matrizCondicionalAt2)
print("Nueva matriz:\n", matrizCondicionalAt3)



