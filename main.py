import numpy as np
from Funciones import Funciones_matrices

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

# Ejemplo de uso
estado_inicial = "1000"  # Puede ser cualquier longitud
sistema_candidatos = "ABC"  # Puede incluir cualquier letra del estado inicial
profundidad_inicial = len(estado_inicial)  # Nivel de profundidad

combinaciones_t1 = Funciones_matrices.generar_combinaciones_exponenciales_t1(profundidad_inicial)
combinaciones_t = Funciones_matrices.generar_combinaciones_exponenciales_t(profundidad_inicial)
resultado, letras_restantes, trans_matrix_filtrada = Funciones_matrices.background(combinaciones_t, estado_inicial, sistema_candidatos, trans_matrix)

matriz_resultado = Funciones_matrices.marginalizar_columna(estado_inicial, sistema_candidatos, trans_matrix_filtrada)
profundidad = len(sistema_candidatos)
print("Matriz marginalizada: ") 
print(matriz_resultado)

sistema_candidatos_margi = "AB"
matriz_resultado_fila = Funciones_matrices.marginalizar_fila(sistema_candidatos, sistema_candidatos_margi, matriz_resultado)
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

matriz_produto = Funciones_matrices.producto_tensorial_matrices(matrices_resultantes)
# Imprimir la matriz de resultados con combinaciones
print("Matriz de resultados:")
print(matriz_produto)
