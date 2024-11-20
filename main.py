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
sistema_candidatos = "ABCD"  # Puede incluir cualquier letra del estado inicial
profundidad_inicial = len(estado_inicial)  # Nivel de profundidad

combinaciones_t1 = Funciones_matrices.generar_combinaciones_exponenciales_t1(profundidad_inicial)
combinaciones_t = Funciones_matrices.generar_combinaciones_exponenciales_t(profundidad_inicial)
resultado, letras_restantes, trans_matrix_filtrada = Funciones_matrices.filtrar_combinaciones(combinaciones_t, estado_inicial, sistema_candidatos, trans_matrix)

# Imprimir resultado
print("Sistema candidato:")
print(" ".join(letras_restantes))
print("\nCombinaciones filtradas:")
for fila in resultado:
    print(" ".join(map(str, fila)))

# Imprimir resultado
print("Matriz de transición filtrada:")
print(trans_matrix_filtrada)

matriz_resultado = Funciones_matrices.filtrar_y_marginalizar(estado_inicial, sistema_candidatos, trans_matrix_filtrada)
profundidad = len(sistema_candidatos)
print("Matriz marginalizada: ") 
print(matriz_resultado)


# Nivel de profundidad
combinaciones = Funciones_matrices.generar_combinaciones_exponenciales(profundidad)

# Ejemplo de uso
resultadoA = Funciones_matrices.independicia_condicional(matriz_resultado, combinaciones[0])
resultadoB = Funciones_matrices.independicia_condicional(matriz_resultado, combinaciones[1])
resultadoC = Funciones_matrices.independicia_condicional(matriz_resultado, combinaciones[2])
matriz_condicional = [resultadoA, resultadoB, resultadoC]
Funciones_matrices.imprimir_tablas_transicion(matriz_condicional)



# Ejemplo de uso Producto tensorial
resultado_tensorial = Funciones_matrices.producto_tensorial([resultadoA, resultadoB, resultadoC])
print(resultado_tensorial)
