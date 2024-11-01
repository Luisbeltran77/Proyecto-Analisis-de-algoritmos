import numpy as np 

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


# Diccionario que asocia letras con índices de columnas
columna_indices = {"A": 0, "B": 1, "C": 2, "D": 3}

def mostrar_columna(letra):
    """Muestra los valores de la columna indicada por 'letra'."""
    indice = columna_indices.get(letra.upper())
    if indice is None:
        print(f"Columna '{letra}' no válida. Debe ser A, B, C o D.")
        return
    
    print(f"Columna {letra}")
    for combinacion in combinaciones:
        print(combinacion[indice])

def eliminar_columna(letra):
    """Muestra las combinaciones sin la columna indicada por 'letra'."""
    indice = columna_indices.get(letra.upper())
    if indice is None:
        print(f"Columna '{letra}' no válida. Debe ser A, B, C o D.")
        return

    print(f"Combinaciones sin la columna {letra}")
    for combinacion in combinaciones:
        combinacion_sin_columna = tuple(
            valor for i, valor in enumerate(combinacion) if i != indice
        )
        print(combinacion_sin_columna)

# Ejemplos de uso
mostrar_columna("d")  # Mostrar solo la columna A
#eliminar_columna("d")  # Mostrar combinaciones sin la columna B

def obtener_probabilidad(trans_matrix, combinaciones, estado_t, estado_t1):
    """Obtiene la probabilidad de transición del estado_t al estado_t1."""
    # Encontrar los índices de las combinaciones en la lista
    try:
        indice_t = combinaciones.index(estado_t)
        indice_t1 = combinaciones.index(estado_t1)
        # Obtener la probabilidad de la matriz de transición
        probabilidad = trans_matrix[indice_t, indice_t1]
        return probabilidad
    except ValueError:
        print("Uno de los estados no se encuentra en las combinaciones.")
        return None

def obtener_independencia_condicional(matriz, estado_t1):
    

# Ejemplo de uso: probabilidad de pasar de 0000 en t a 0001 en t+1
estado_t = (0, 0, 0, 0)
estado_t1 = (0, 0, 0, 0)
probabilidad = obtener_probabilidad(trans_matrix, combinaciones, estado_t, estado_t1)
print(f"La probabilidad de pasar de {estado_t} a {estado_t1} es {probabilidad}")