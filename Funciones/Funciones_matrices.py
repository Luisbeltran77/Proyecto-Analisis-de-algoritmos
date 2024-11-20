import numpy as np
import string


# Genera una secuencia de 0s y 1s con patrones repetitivos exponenciales
def generar_combinaciones_exponenciales(n):
    combinaciones = []
    for i in range(n):
        repeticion = 2**i
        array = np.tile([0] * repeticion + [1] * repeticion, 2**(n - i - 1))
        combinaciones.append(array)
    return combinaciones


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
        #print(letra, end=' ')
        #print(' '.join(map(str, patron_completo)))
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
    #letras = list(string.ascii_uppercase[:n])[::]  # Invertir para empezar desde la última
    
    # Mostrar la matriz con los encabezados de letras
    #print("Combinaciones en t:")
    #print(" ".join(letras))  # Imprimir encabezados
    #for fila in combinacion:
    #    print(" ".join(map(str, fila)))  # Imprimir cada fila
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

def imprimir_tablas_transicion(matrices):
    """
    Imprime una lista de matrices de transición en un formato legible,
    con cada matriz acomodada una al lado de la otra.
    """
    num_matrices = len(matrices)
    headers = [f"Matriz {chr(65 + i)}(t+1)" for i in range(num_matrices)]

    # Obtener la cantidad de filas en cada matriz para alineación
    num_filas = matrices[0].shape[0]
    separator = "        "  # Espacio entre matrices para alinearlas

    # Imprimir encabezado de matrices
    header_row = separator.join([f"{header:>10}" for header in headers])
    print(header_row)

    # Imprimir subencabezados de columnas
    sub_header_row = separator.join(["0         1  " for _ in range(num_matrices)])
    print(sub_header_row)

    # Separador de línea
    print(separator.join(["-" * 12 for _ in range(num_matrices)]))

    # Imprimir filas de cada matriz en paralelo
    for i in range(num_filas):
        row = separator.join([f"{int(matrices[j][i, 0])}      {int(matrices[j][i, 1])}     " for j in range(num_matrices)])
        print(row)

def producto_tensorial(matrices):
    # Inicializa el resultado con la primera matriz
    resultado = matrices[0]
    
    # Aplica el producto tensorial secuencialmente
    for matriz in matrices[1:]:
        resultado = np.kron(resultado, matriz)
    
    return resultado

