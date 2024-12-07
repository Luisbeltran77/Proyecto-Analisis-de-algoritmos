import numpy as np
import string
from itertools import product
import pandas as pd
from scipy.stats import wasserstein_distance



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

    if isinstance(matriz, list):
        matriz = np.array(matriz)

    # Crear una nueva matriz para almacenar los resultados
    filas = matriz.shape[0]
    nueva_matriz = np.zeros((filas, 2))

    # Sumar las columnas correspondientes a 0 y 1
    nueva_matriz[:, 0] = matriz[:, vector_0].sum(axis=1)  # Sumar columnas correspondientes a 0
    nueva_matriz[:, 1] = matriz[:, vector_1].sum(axis=1)  # Sumar columnas correspondientes a 1

    return nueva_matriz




def background(combinaciones_originales, estado_inicial, sistema_candidatos, trans_matrix):
    # Extraemos las letras y valores del estado inicial
    letras_originales = list(estado_inicial.keys())
    estado = list(estado_inicial.values())

    # Encontramos las letras a eliminar
    letras_eliminar = set(letras_originales) - set(sistema_candidatos)

    # Creamos una lista de índices a eliminar basándonos en las letras
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
def marginalizar_columna(estado_inicial, sistema_candidatos, trans_matrix):
    #estado = list(estado_inicial.values())
    print('este es el estado: ', estado_inicial)
    print('este es el sistema candidato: ', sistema_candidatos)
    print('este es la transicion: ', trans_matrix)
    dato = len(estado_inicial)
    print('este es el dato de estado inicial: ', dato)
    dato2 = len(sistema_candidatos)
    print('este es el dato de sistema candidato: ', dato2)
    n = dato - dato2
    print('este es el n: ', n)

    matriz_marginalizada = []
    trans_matrix_marginalizada = trans_matrix
    if n == 0:
        return trans_matrix_marginalizada
    
    # Marginalizamos la matriz
    for _ in range(abs(n)):
        trans_matrix_marginalizada = marginalizar_matriz(trans_matrix_marginalizada)
        matriz_marginalizada = trans_matrix_marginalizada
    
    return matriz_marginalizada


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



def marginalizar_matriz_por_filas(trans_matrix):
    """
    Combina las filas correspondientes y redistribuye los valores de manera proporcional
    para asegurar que la suma total de la fila no exceda 1.
    """
    n_filas, n_columnas = trans_matrix.shape
    mitad_filas = n_filas // 2
    
    # Crear una nueva matriz con la mitad de filas
    matriz_marginalizada = np.zeros((mitad_filas, n_columnas))
    
    for i in range(mitad_filas):
        # Sumar las filas correspondientes
        suma = trans_matrix[i, :] + trans_matrix[i + mitad_filas, :]
        
        # Verificar si la suma total supera 1
        suma_total = np.sum(suma)
        if suma_total > 1:
            # Redistribuir proporcionalmente para que la suma total sea igual a 1
            suma = suma / suma_total
        
        # Asignar la fila procesada a la matriz marginalizada
        matriz_marginalizada[i, :] = suma
    
    return matriz_marginalizada



# Función completa que combina el filtrado y la marginalización
def marginalizar_fila(estado_inicial, sistema_candidatos, trans_matrix):
    dato = len(estado_inicial)
    dato2 = len(sistema_candidatos)
    n = dato - dato2
    print('esta es la n: ', n)
    matriz_marginalizada = []
    trans_matrix_marginalizada = trans_matrix
    print('esta es la trans_matrix: ', trans_matrix_marginalizada)
    if n == 0:
        return trans_matrix_marginalizada
    
    # Marginalizamos la matriz
    for _ in range(n):
        trans_matrix_marginalizada = marginalizar_matriz_por_filas(trans_matrix_marginalizada)
        matriz_marginalizada = trans_matrix_marginalizada
        print('esta es la mtr ya margi: ', matriz_marginalizada)
    
    return matriz_marginalizada


def producto_tensorial_matrices(matrices):
    # Convertir la lista a un arreglo de NumPy
    matrices = np.array(matrices)

   
    # Obtener el número de matrices, filas y columnas
    num_matrices = matrices.shape[0]
    num_filas = matrices.shape[1]
    print('este es el n filas: ', num_filas//2)
    
    # Generar todas las combinaciones ANTES de los bucles de filas
    combinaciones = []
    for idx in range(2**num_matrices):
        # Convertir el índice a binario y rellenar con ceros a la izquierda
        combinacion = [(idx >> (num_matrices - 1 - k)) & 1 for k in range(num_matrices)]  
        combinacion_invert = list(reversed(combinacion))
        combinaciones.append(combinacion_invert)
    
    # Crear una matriz para almacenar los resultados
    resultados_matriz = np.zeros((num_filas//2, 2**num_matrices), dtype=int)
    print('esta es la matriz de ceros: \n', resultados_matriz)
    
    # Ahora iterar por filas usando las combinaciones ya generadas
    for fila in range(num_filas//2):
        for idx, combinacion in enumerate(combinaciones):
            # Obtener los valores en la fila especificada y las columnas de la combinación
            valores = [matrices[k][fila][col] for k, col in enumerate(combinacion)]
            
            # Verificar si todos los valores son iguales y son 1
            todos_iguales = all(valor == 1 for valor in valores)
            
            # Almacenar el resultado en la matriz 
            resultados_matriz[fila][idx] = 1 if todos_iguales else 0      
           
    return resultados_matriz

def cargar_excel(ruta_archivo):
    try:
        print(ruta_archivo)
        # Lee el archivo Excel
        nombre_hoja = 'DatosRed6Nodos'
        df_hoja1 = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja)
        rango_filas = df_hoja1.iloc[2:66, 1:13].to_numpy()
        # Dividir las columnas en matrices de 2 columnas cada una
        matrices = [rango_filas[:, i:i+2] for i in range(0, rango_filas.shape[1], 2)]
        return matrices
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

def compare_matrices(matrices1, matrices2):
    # Verificar que tengan el mismo número de matrices
    if len(matrices1) != len(matrices2):
        print(f"Diferente número de matrices: {len(matrices1)} vs {len(matrices2)}")
        return False
    
    # Comparar cada matriz
    for i, (mat1, mat2) in enumerate(zip(matrices1, matrices2)):
        if not np.array_equal(mat1, mat2):
            print(f"Diferencia en matriz {i}:")
            print("Matriz 1:")
            print(mat1)
            print("Matriz 2:")
            print(mat2)
            # Mostrar dónde son diferentes
            diff = mat1 != mat2
            print("Índices diferentes:")
            print(np.argwhere(diff))
            return False
    
    return True

def particiones_subco(v):
    # Lista para las particiones w
    w = []

    # Proceso para crear las particiones
    for futuro, presente in v:
        # Primero generar particiones para el presente (t)
        for i in range(1, len(presente) + 1):
            particion = ("", presente[:i])  # Vacío en futuro para particiones de presente
            w.append(particion)
        # Luego generar particiones para el futuro (t+1)
        for i in range(1, len(futuro) + 1):
            particion = (futuro[:i], presente)  # Vacío en presente para particiones de futuro
            w.append(particion)
    return w

def complemento(futuro_completo,presente_completo,w):
    # Calcular complementos para cada partición
    complementos = []
    for particion in w:
        futuro_actual, presente_actual = particion
        complemento_futuro = "".join(char for char in futuro_completo if char not in futuro_actual)
        complemento_presente = "".join(char for char in presente_completo if char not in presente_actual)
        complementos.append((complemento_futuro, complemento_presente))
    return complementos

def procesar_particiones(particiones, estado_inicial, trans_matrix_filtrada, fila, complementos, combinacion, binary_combination):
    
    # Inicializar variables para almacenar el menor resultado, partición y complemento correspondientes
    menor_res = float('inf')  # Inicia con infinito
    mejor_particion = None
    mejor_complemento = None

    # Procesar cada partición
    for particion, complemento in zip(particiones[:-1], complementos[:-1]):
        futuro_p, presente_p = particion
        matriz_margi_col_p = marginalizar_columna(estado_inicial, futuro_p, trans_matrix_filtrada)
        matriz_res_p = marginalizar_fila(binary_combination, presente_p, matriz_margi_col_p)

        binary_combination_p = ''.join(combinacion)
        row_index_p = int(binary_combination_p, 2)

        if 0 <= row_index_p < len(matriz_res_p):
            row_part = matriz_res_p[row_index_p]
        else:
            print("El índice calculado está fuera del rango de la matriz partición.")
            continue

        futuro_c, presente_c = complemento
        if len(presente_c) > 0:
            matriz_margi_col_c = marginalizar_columna(estado_inicial, futuro_c, trans_matrix_filtrada)
            matriz_res_c = marginalizar_fila(binary_combination, presente_c, matriz_margi_col_c)

            binary_combination_c = ''.join(combinacion)
            row_index_c = int(binary_combination_c, 2)

            if 0 <= row_index_c < len(matriz_res_c):
                row_com = matriz_res_c[row_index_c]
            else:
                print("El índice calculado está fuera del rango de la matriz complemento.")
                continue

            if len(row_part) < len(row_com):
                particion_arr = np.pad(row_part, (0, len(row_com) - len(row_part)), constant_values=1)

            producto_vect = particion_arr * row_com
        else:
            num_letras = len(futuro_c)
            # Calcular el valor que debe ocupar cada posición
            valor = 1 / num_letras

            # Crear el vector con ese valor en cada posición
            vector = np.full(num_letras, valor)

            if len(row_part) < len(vector):
                particion_arr = np.pad(row_part, (0, len(vector) - len(row_part)), constant_values=1)
                vector_a = vector  # Usar el vector original cuando row_part es más pequeño

            elif len(row_part) > len(vector):
                # Rellenar vector con 1's para que coincida con el tamaño de row_part
                vector_a = np.pad(vector, (0, len(row_part) - len(vector)), constant_values=1)
                particion_arr = row_part  # Usar row_part cuando es más pequeño
            else:
                # Si tienen el mismo tamaño, solo usa el vector sin cambios
                vector_a = vector
                particion_arr = row_part

            producto_vect = particion_arr * vector_a

        # Calcular el resultado usando la distancia Wasserstein
        res = wasserstein_distance(fila, producto_vect)

        # Actualizar el menor resultado encontrado y almacenar partición/complemento
        if res < menor_res:
            menor_res = res
            mejor_particion = particion
            mejor_complemento = complemento

    return menor_res, mejor_particion, mejor_complemento

def filas_solo_ceros(matriz):
    """
    Identifica las filas de una matriz que contienen únicamente ceros.

    Args:
        matriz (list of list of int/float): Matriz a analizar.

    Returns:
        list of int: Lista de índices de las filas que tienen solo ceros.
    """
    filas_ceros = []
    for i, fila in enumerate(matriz):
        if all(elemento == 0 for elemento in fila):
            filas_ceros.append(i)
    return filas_ceros