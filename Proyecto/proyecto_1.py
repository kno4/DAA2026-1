import sys
# Problema 1 - Ejercicio 1 - Pregunta 1
#Tarea 1: Determinar si existe un camino (implementación óptima)
def existe_camino_robot(n, m):
    """""Determina si existe un camino desde (0,0) hasta (n-1,m-1) usando backtracking
    con memoización para optimizar la búsqueda. (programación dinámica).

    :param : n: número de filas de la cuadrícula
    :param : m: número de columnas de la cuadrícula
    :return: True si existe un camino, False en caso contrario.

    Nota: Un camino solo puede existir si el destino (n-1,m-1) se puede expresar como
    (0 + 2a, 0 + 3b) para enteros no negativos a y b.
    """
    target = (n - 1, m - 1)

    #memo almacena los resultados ya calculados
    # None = no visitado, True = camino existe, False = no se puede
    memo = {}

    def buscar(r, c):
        #1. Caso base: éxito
        if r == target[0] and c == target[1]:
            return True
        #2. Caso base: fuera de límites
        if r >= n or c >= m:
            return False
        #3. Revisar memoización
        if (r, c) in memo:
            return memo[(r, c)]
        #4. Paso recursivo: explorar las dos opciones

        # Opción 1: moverse hacia abajo
        encontrado_abajo = buscar(r + 2, c)

        # Opción 2: moverse hacia la derecha
        #(podemos ahorrarnos la llamada si la de 'encontrado_abajo' es True)
        encontrado_derecha = False
        if not encontrado_abajo:
            encontrado_derecha = buscar(r, c + 3)

        #5. Guardar en memoización
        memo[(r, c)] = encontrado_abajo or encontrado_derecha
        return memo[(r, c)]
    return buscar(0, 0)
# --- Ejemplo de uso ---
n = 5
m = 7
if existe_camino_robot(n, m):
    print(f"Existe un camino desde (0,0) hasta ({n-1},{m-1})")
else:
    print(f"No existe un camino desde (0,0) hasta ({n-1},{m-1})")

print(f"Para una cuadricula de 5x6: {'Sí existe' if existe_camino_robot(5, 6) else 'No existe'} un camino.")

# Problema 1 - Ejercicio 1 - Pregunta 2
#Tarea 2: Determinar todos los caminos posibles

def todos_caminos_robot(n, m):
    """
    Encuentra todos los caminos posibles desde (0,0) hasta (n-1, m-1) usando backtracking.
    :param n: Número de filas de la cuadrícula
    :param m: número de columnas de la cuadrícula
    :return: Lista de listas, donde cada lista interna representa un camino como una secuencia
             de coordenadas (tuples) desde el inicio hasta el destino.
    """
    target = (n - 1, m - 1)
    soluciones = []

    def buscar(r, c, actual_path):
        #1. Caso base: Fracaso(fuera de límites)
        if r >= n or c >= m:
            return # Esta rama no lleva a una solución

        #2. Añadir la casilla actual al camino que estamos explorando
        actual_path = actual_path + [(r, c)]

        #3. Caso base: Éxito
        if r == target[0] and c == target[1]:
            soluciones.append(actual_path) #Se encontró el camino
            return #Termina esta rama

        #4. Paso recursivo: explorar las dos opciones

        # Opción 1: moverse hacia abajo
        buscar(r + 2, c, actual_path)

        # Opción 2: moverse hacia la derecha
        buscar(r, c + 3, actual_path)

    buscar(0, 0, [])
    return soluciones
# --- Ejemplo de uso ---
n = 5
m = 7
caminos = todos_caminos_robot(n, m)
print(f"Todos los caminos desde (0,0) hasta ({n-1},{m-1}):")
for camino in caminos:
    print(camino)

