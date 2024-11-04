import numpy as np
import string

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




    # Genera una secuencia de 0s y 1s con patrones repetitivos exponenciales
def generar_combinaciones_exponenciales_t1(n):
    # Generar los encabezados de letras
    letras = list(string.ascii_uppercase[:n])
    
    # Calcular el número total de columnas (2^n)
    num_columnas = 2**n

    # Lista para almacenar todos los patrones
    patrones = []
    
    # Para cada letra (variable)
    for i, letra in enumerate(letras):
        # Calcular el patrón de repetición para esta fila
        repeticion = 2**(i)
        # Generar el patrón de 0s y 1s
        patron = [0] * repeticion + [1] * repeticion
        # Repetir el patrón hasta completar todas las columnas
        patron_completo = patron * (num_columnas//(2*repeticion))
        # Guardar el patrón completo
        patrones.append(patron_completo)
        # Imprimir la letra seguida de su patrón
        print(letra, end=' ')
        print(' '.join(map(str, patron_completo)))
    return patrones

def generar_combinaciones_exponenciales_t(n):
    combinacion = []
    # Generar cada columna de combinaciones empezando por el cambio más significativo
    for i in range(n - 1, -1, -1):  # Empezamos desde el bit más significativo
        repeticion = 2 ** i
        array = np.tile([0] * repeticion + [1] * repeticion, 2 ** (n - i - 1))
        combinacion.append(array)
    
    # Convertimos la lista de columnas en una matriz de combinaciones (traspuesta)
    combinacion = np.array(combinacion).T
    
    # Reordenamos las columnas invirtiendo el orden (de la última a la primera)
    combinacion = combinacion[:, ::-1]
    
    # Generamos los encabezados de letras dinámicamente según el número de columnas
    letras = list(string.ascii_uppercase[:n])[::]  # Invertir para empezar desde la última
    
    # Mostrar la matriz con los encabezados de letras
    print("Combinaciones en t:")
    print(" ".join(letras))  # Imprimir encabezados
    for fila in combinacion:
        print(" ".join(map(str, fila)))  # Imprimir cada fila
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
def independicia_condicional(matriz, combinacion):

    # Identificar posiciones
    vector_0, vector_1 = identificar_posiciones(combinacion)

    # Crear una nueva matriz para almacenar los resultados
    filas = matriz.shape[0]
    nueva_matriz = np.zeros((filas, 2))

    # Sumar las columnas correspondientes a 0 y 1
    nueva_matriz[:, 0] = matriz[:, vector_0].sum(axis=1)  # Sumar columnas correspondientes a 0
    nueva_matriz[:, 1] = matriz[:, vector_1].sum(axis=1)  # Sumar columnas correspondientes a 1

    return nueva_matriz



def filtrar_combinaciones(combinaciones_originales, estado_inicial, sistema_candidatos, trans_matrix):
    # Convertimos el estado inicial a una lista de 0s y 1s
    estado = list(map(int, estado_inicial))
    
    # Generamos las letras originales dinámicamente según la longitud del estado inicial
    n = len(estado_inicial)
    letras_originales = list(string.ascii_uppercase[:n])
    
    # Encontramos las letras a eliminar
    letras_eliminar = set(letras_originales) - set(sistema_candidatos)
    
    # Creamos una lista de índices a eliminar
    indices_eliminar = []
    for letra in letras_eliminar:
        indices_eliminar.append(letras_originales.index(letra))
    
    # Filtramos las filas que cumplan con todos los valores del estado inicial
    combinaciones_filtradas = []
    indices_originales = []  # Para mantener un registro de los índices originales
    
    for i, fila in enumerate(combinaciones_originales):
        incluir_fila = True
        nueva_fila = list(fila)
        
        # Verificamos cada letra a eliminar
        for indice in indices_eliminar:
            if fila[indice] != estado[indice]:
                incluir_fila = False
                break
        
        if incluir_fila:
            # Eliminamos las columnas de las letras que no están en sistema_candidatos
            for indice in sorted(indices_eliminar, reverse=True):
                nueva_fila.pop(indice)
            combinaciones_filtradas.append(nueva_fila)
            indices_originales.append(i)
    
    # Filtramos solo las filas de la matriz de transición
    trans_matrix_filtrada = trans_matrix[indices_originales]
    
    return combinaciones_filtradas, [letra for letra in letras_originales if letra in sistema_candidatos], trans_matrix_filtrada



def marginalizar_matriz(trans_matrix):
    """
    Marginaliza la matriz sumando las columnas correspondientes de la primera
    y segunda mitad de la matriz.
    """
    n_filas, n_columnas = trans_matrix.shape
    mitad_columnas = n_columnas // 2
    
    # Creamos una nueva matriz con la mitad de columnas
    matriz_marginalizada = np.zeros((n_filas, mitad_columnas))
    
    # Sumamos las columnas correspondientes
    for i in range(mitad_columnas):
        matriz_marginalizada[:, i] = trans_matrix[:, i] + trans_matrix[:, i + mitad_columnas]
    
    return matriz_marginalizada

# Función completa que combina el filtrado y la marginalización
def filtrar_y_marginalizar(combinaciones_originales, estado_inicial, sistema_candidatos, trans_matrix):
    # Primero filtramos las filas como antes
    combinaciones_filtradas = []
    indices_originales = []
    
    estado = list(map(int, estado_inicial))
    n = len(estado_inicial)
    letras_originales = list(string.ascii_uppercase[:n])
    letras_eliminar = set(letras_originales) - set(sistema_candidatos)
    indices_eliminar = [letras_originales.index(letra) for letra in letras_eliminar]
    
    for i, fila in enumerate(combinaciones_originales):
        incluir_fila = True
        for indice in indices_eliminar:
            if fila[indice] != estado[indice]:
                incluir_fila = False
                break
        if incluir_fila:
            indices_originales.append(i)
    
    # Filtramos las filas de la matriz
    trans_matrix_filtrada = trans_matrix[indices_originales]
    
    # Marginalizamos la matriz
    trans_matrix_marginalizada = marginalizar_matriz(trans_matrix_filtrada)
    
    return trans_matrix_marginalizada


# Ejemplo de uso
n = 4  # Nivel de profundidad
print("Combinaciones en t + 1 ")
combinaciones_t1 = generar_combinaciones_exponenciales_t1(n)
combinaciones_t = generar_combinaciones_exponenciales_t(n)

# Ejemplo de uso
estado_inicial = "1000"  # Puede ser cualquier longitud
sistema_candidatos = "ABC"  # Puede incluir cualquier letra del estado inicial

resultado, letras_restantes, trans_matrix_filtrada = filtrar_combinaciones(combinaciones_t, estado_inicial, sistema_candidatos, trans_matrix)

# Imprimir resultado
print("Letras restantes:")
print(" ".join(letras_restantes))
print("\nCombinaciones filtradas:")
for fila in resultado:
    print(" ".join(map(str, fila)))

# Imprimir resultado
print("Matriz de transición filtrada:")
print(trans_matrix_filtrada)

estado_inicial = "1000"
sistema_candidatos = "ABC"  # Note que D no está incluida
matriz_resultado = filtrar_y_marginalizar(combinaciones_t, estado_inicial, sistema_candidatos, trans_matrix)
profundidad = len(sistema_candidatos)



print("Matriz marginalizada: ")
print(matriz_resultado)


resultadoA = independicia_condicional(matriz_resultado, resultado)
print("Matriz A: ")
print(resultadoA)
resultadoB = independicia_condicional(matriz_resultado, resultado)
print("Matriz B: ")
print(resultadoB)
resultadoC = independicia_condicional(matriz_resultado, resultado)
print("Matriz C: ")
print(resultadoC)
matriz_condicional = [resultadoA, resultadoB, resultadoC]
print("Matriz: ")
print(matriz_condicional)

"""
# Encabezados de las matriz_condicional
headers = ["A", "B", "C", "D", "E"]  # Puedes añadir más nombres si hay más matriz_condicional

# Imprimir encabezados con tabulación entre ellos
print("\t".join([f"{header}" for header in headers]))

# Imprimir cada fila de las matriz_condicional con tabulación
for row in range(matriz_condicional[0].shape[0]):
    print("\t".join(["\t".join(map(str, matriz_condicional[i][row])) for i in range(len(matriz_condicional))]))
"""

def generar_tablas_transicion(combinaciones_t, trans_matrix):
    """
    Genera tablas de transición para cada variable en t+1 basado en las combinaciones en t.
    
    Args:
        combinaciones_t: Lista de combinaciones en tiempo t
        trans_matrix: Matriz de transición marginalizada
    
    Returns:
        Dict con las tablas de probabilidad para cada variable
    """
    # Determinar el número de variables basado en la longitud de las combinaciones
    n_variables = len(combinaciones_t[0])
    n_combinaciones = len(combinaciones_t)
    
    # Crear el sistema de variables automáticamente (A, B, C, etc.)
    variables = list(string.ascii_uppercase[:n_variables])
    
    tablas = {}
    
    for i, variable in enumerate(variables):
        # Crear tabla para la variable actual
        tabla = np.zeros((n_combinaciones, 2))  # 2 columnas: para 0 y 1 en t+1
        
        # Para cada combinación en t
        for j, comb_actual in enumerate(combinaciones_t):
            # Obtener las filas de la matriz de transición donde la variable i es 0 y 1
            prob_0 = 0
            prob_1 = 0
            
            # Recorrer la fila correspondiente en la matriz de transición
            fila_trans = trans_matrix[j]
            for k, prob in enumerate(fila_trans):
                if prob > 0:
                    # Determinar si en esta transición la variable i es 0 o 1
                    # Para esto, necesitamos convertir k a binario y ver el bit i
                    estado_siguiente = format(k, f'0{n_variables}b')
                    if estado_siguiente[i] == '0':
                        prob_0 += prob
                    else:
                        prob_1 += prob
            
            tabla[j, 0] = prob_0
            tabla[j, 1] = prob_1
            
        tablas[variable] = tabla
        
    return tablas

def imprimir_tablas_transicion(tablas, combinaciones_t):
    """
    Imprime las tablas de transición en un formato legible
    """
    variables = list(tablas.keys())
    
    for variable in variables:
        print(f"\nTabla de transición para {variable}(t+1):")
        print(f"{' '.join(variables)} | 0 1")
        print("-" * (len(variables)*2 + 6))
        
        for i, comb in enumerate(combinaciones_t):
            comb_str = " ".join(map(str, comb))
            probs = tablas[variable][i]
            print(f"{comb_str} | {probs[0]:.1f} {probs[1]:.1f}")


# Generar y mostrar las tablas
tablas = generar_tablas_transicion(combinaciones_t, trans_matrix_filtrada)
imprimir_tablas_transicion(tablas, combinaciones_t)