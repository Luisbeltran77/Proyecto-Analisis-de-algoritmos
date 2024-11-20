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
#mostrar_columna("a")  # Mostrar solo la columna A
eliminar_columna("D")  # Mostrar combinaciones sin la columna B

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

# Ejemplo de uso: probabilidad de pasar de 0000 en t a 0001 en t+1
estado_t = (0, 0, 0, 0)
estado_t1 = (0, 0, 0, 0)
probabilidad = obtener_probabilidad(trans_matrix, combinaciones, estado_t, estado_t1)
print(f"La probabilidad de pasar de {estado_t} a {estado_t1} es {probabilidad}")

def filtrar_columnas_por_letras(letras):
    """Retorna combinaciones mostrando solo las columnas especificadas en 'letras'."""
    # Convertir letras a índices de columnas
    indices_a_mantener = [columna_indices[letra] for letra in letras if letra in columna_indices]
    
    # Filtrar y mostrar combinaciones con solo las columnas especificadas
    combinaciones_filtradas = []
    for combinacion in combinaciones:
        combinacion_filtrada = tuple(combinacion[i] for i in indices_a_mantener)
        combinaciones_filtradas.append(combinacion_filtrada)
    
    return combinaciones_filtradas


#resultado = filtrar_columnas_por_letras("ABC")
#print("Combinaciones Después")
#for comb in resultado:
#    print(comb)

def filtrar_y_eliminar(sistema, estado_sistema, subsistema):
    """Filtra combinaciones para un subsistema y elimina la columna de la letra excluida."""
    
    # Convertir letras a índices de columnas
    indices_sistema = [columna_indices[letra] for letra in sistema]
    indices_subsistema = [columna_indices[letra] for letra in subsistema]
    
    # Determinar la letra excluida del subsistema y su estado
    letra_excluida = next(letra for letra in sistema if letra not in subsistema)
    indice_excluido = columna_indices[letra_excluida]
    estado_excluido = int(estado_sistema[indice_excluido])
    
    # Filtrar combinaciones que cumplen con el estado de la letra excluida
    combinaciones_filtradas = []
    for combinacion in combinaciones:
        # Verificar si el estado de la letra excluida es el mismo que en el estado completo
        if combinacion[indice_excluido] == estado_excluido:
            # Crear una combinación solo con las columnas del subsistema
            combinacion_subsistema = tuple(combinacion[i] for i in indices_subsistema)
            combinaciones_filtradas.append(combinacion_subsistema)
    
    return combinaciones_filtradas

# Ejemplo de uso: sistema completo es "ABCD" con estado "1000", y el subsistema es "ABC"
resultado = filtrar_y_eliminar("ABCD", "1001", "ACD")
print("Combinaciones del subsistema ABC en las que D es 0:")
for comb in resultado:
    print(comb)
