import numpy as np
from Funciones import Funciones_matrices
import pandas as pd

# Configurar NumPy para mostrar matrices completas
np.set_printoptions(threshold=np.inf)
ruta = 'matriz 15x15 texto.txt'
matriz_cargada = Funciones_matrices.leer_matriz_desde_txt(ruta)
#print('Esta es la matriz cargada')
#print(matriz_cargada)

#matriz_producto = Funciones_matrices.producto_tensorial_matrices(matriz_cargada)
#print("Matriz de resultados:")
#print(matriz_producto)

# Ejemplo de uso
estado_inicial = {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0}
sistema_candidatos = "ABCDE"  # Puede incluir cualquier letra del estado inicial
subsistema = 'ABCDE|ABCDE'
profundidad_inicial = len(estado_inicial)  # Nivel de profundidad
print('esta es la profundidad: ', profundidad_inicial)
# Separar los elementos por el símbolo "|"
futuro, presente = subsistema.split("|")
# Crear un conjunto para guardar los pares
v = set()
# Agregar los elementos como un par (t+1, t)
v.add((futuro, presente))

combinaciones_t1 = Funciones_matrices.generar_combinaciones_exponenciales_t1(profundidad_inicial)
combinaciones_t = Funciones_matrices.generar_combinaciones_exponenciales_t(profundidad_inicial)
resultado, letras_restantes, trans_matrix_filtrada = Funciones_matrices.background(combinaciones_t, estado_inicial, sistema_candidatos, matriz_cargada)
print('esta es back',trans_matrix_filtrada)

matriz_resultado = Funciones_matrices.marginalizar_columna(estado_inicial, sistema_candidatos, trans_matrix_filtrada)
profundidad = len(sistema_candidatos)
print("Matriz marginalizada: ") 
print(matriz_resultado)

#sistema_candidatos_margi = "AB"
#matriz_resultado_fila = Funciones_matrices.marginalizar_fila(sistema_candidatos, sistema_candidatos_margi, matriz_resultado)
#print("Matriz marginalizada por fila: ") 
#print(matriz_resultado_fila)
# Nivel de profundidad
combinaciones = Funciones_matrices.generar_combinaciones_exponenciales(profundidad)

# Ejemplo de uso
matrices_resultantes = []
i=0
for i in range(profundidad):
    resultadoA = Funciones_matrices.independicia_condicional(matriz_resultado, combinaciones[i])
    matrices_resultantes.append(resultadoA)  # Guardar la matriz en la lista  
#print("matrices que entran:\n",matrices_resultantes)
#producto_t = Funciones_matrices.producto_tensorial_matrices(matrices_resultantes)
#print('producto tensorial: \n', producto_t)

particiones = Funciones_matrices.particiones_subco(v)
complemento = Funciones_matrices.complemento(futuro,presente,particiones)
# Imprimir las particiones y sus complementos

for ve in v:
    # Obtener los valores del estado inicial correspondientes a las claves en ve[1]
    valores = [estado_inicial[letra] for letra in ve[1] if letra in estado_inicial]
     # Convertir valores en una cadena binaria
    binary_combination = ''.join(str(valor) for valor in valores)
    print('esta es la combi: ', binary_combination)
    # Calcular el índice de la fila basado en la combinación binaria
    try:
        row_index = int(binary_combination, 2)
    except ValueError:
        print("Error al convertir la combinación binaria:", binary_combination)
        continue

    #print('Esto es dentro:', valores)

    # Sistema parte 0: Operar sobre columnas
    sistema_part0 = ve[0]
    #print('sistema 0: ', sistema_part0)
    matriz_resultado_part = Funciones_matrices.marginalizar_columna(binary_combination, sistema_part0, matriz_resultado)

    # Sistema parte 1: Operar sobre filas
    sistema_part1 = ve[1]
    #print('sistema 1: ', sistema_part1)
    matriz_resultado_fila_part = Funciones_matrices.marginalizar_fila(binary_combination, sistema_part1, matriz_resultado_part)

    # Validar el índice antes de acceder a la fila
    if 0 <= row_index < len(matriz_resultado_fila_part):
        row = matriz_resultado_fila_part[row_index]
        print("Fila seleccionada:", row)
    else:
        print("El índice calculado está fuera del rango de la matriz.")

print('esta es la particion',sistema_part0)
print('esta es la matriz mar col',matriz_resultado_part)
print('esta es la matriz mar fil',matriz_resultado_fila_part)
print('esta es la particion',sistema_part1)
print('este es el row: ',row)
print('estos son los valores: ', valores)


menor_res, mejor_particion, mejor_complemento = Funciones_matrices.procesar_particiones(particiones, estado_inicial, trans_matrix_filtrada, row, complemento, binary_combination, binary_combination)

print('----------ESTA ES LA RESPUESTA-------')
# Al finalizar el ciclo
print(f"El subsistema ingresado es: {subsistema}")
print(f"El menor resultado encontrado es: {menor_res}")
print(f"La mejor partición es: {mejor_particion}")
print(f"El mejor complemento es: {mejor_complemento}")


#---------------------------------Segunda parte--------------------------------
print('---------------------------------SEGUNDA PARTE--------------------------------')
# Generar conjunto A de aristas
conjunto_a = Funciones_matrices.generar_aristas_subsistema(subsistema)
print("Conjunto A de aristas:", conjunto_a)

