import sys
# Problema 2 - Ejercicio 4 - Pregunta 1
#Tarea 1: Implementar el algoritmo con Fuerza Bruta
def leer_postes(archivo_input):
    """
    Lee el archivo 'campo.in' y devuelve una lista de tuplas (x, y)
    :param archivo_input: el nombre del archivo con la lista de 500 postes acomodados en un área
    :return: postes
    """
    postes = []
    try:
        with open(archivo_input, 'r') as f:
            for linea in f:
                x_str, y_str = linea.strip().split()
                x, y = int(x_str), int(y_str)

                if x == -1 and y == -1:
                    break # Fin de la lista de postes
                postes .append((x, y))
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_input} no se encontró.")
        sys.exit(1)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        sys.exit(1)

    return postes

def calcular_doble_area(p1, p2, p3):
    """
    Calcula el doble del área del triángulo formado por los puntos p1, p2 y p3
    usando la fórmula del determinante (Fórmula de Shoelace).
    :param p1: Tupla (x1, y1)
    :param p2: Tupla (x2, y2)
    :param p3: Tupla (x3, y3)
    :return: Doble del área del triángulo
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    area = (x1 * (y2 - y3) +
            x2 * (y3 - y1) +
            x3 * (y1 - y2))
    return abs(area)

def escribir_salida(archivo_out, postes_max):
    """
    Escribe los postes que forman el triángulo de área máxima en el archivo de salida.
    :param archivo_out: Nombre del archivo de salida
    :param postes_max: Lista de tuplas (x, y) que forman el triángulo de área máxima
    """
    try:
        with open(archivo_out, 'w') as f:
            for poste in postes_max:
                f.write(f"{poste[0]} {poste[1]}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
        sys.exit(1)

def resolver_fuerza_bruta(postes):
    """
    Resuelve el problema de encontrar el triángulo de área máxima usando fuerza bruta.
    :param postes: Lista de tuplas (x, y) que representan los postes
    :return: Lista de tuplas (x, y) que forman el triángulo de área máxima
    """
    n = len(postes)
    if n < 3:
        print("No hay suficientes postes para formar un triángulo.")
        return None

    max_area_doble = 0
    postes_max = []

    #Tres bucles anidados para considerar todas las combinaciones de 3 postes
    for i in range (n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p1 = postes[i]
                p2 = postes[j]
                p3 = postes[k]

                area_actual_doble = calcular_doble_area(p1, p2, p3)

                if area_actual_doble > max_area_doble:
                    max_area_doble = area_actual_doble
                    postes_max = [p1, p2, p3]
    return postes_max
# Este programa no es óptimo para grandes conjuntos de datos debido a su complejidad O(n^3),
# pero es adecuado para el problema dado con 500 postes.
# Sin embargo, para conjuntos de datos más grandes, se recomendaría un enfoque más eficiente,
# como el de Graham Scan que calcula el área del polígono convexo máximo en O(n log n).
# Explicado y desarrollado a continuación;
def producto_cruz(o, a, b):
    """
    Calcula el producto cruzado de los vectores OA y OB
    :param o: Punto de origen (x, y)
    :param a: Punto A (x, y)
    :param b: Punto B (x, y)
    :return: Valor del producto cruzado
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(postes):
    """
    Algoritmo de Graham Scan para encontrar el casco convexo de un conjunto de puntos.
    Complejidad O(n log n)
    Retorna los puntos que forman el casco convexo en sentido antihorario.
    :param postes: Lista de tuplas (x, y) que representan todos los postes
    :return: Lista de tuplas (x, y) que forman el casco convexo
    """
    n = len(postes)
    if n < 3:
        return postes  # No se puede formar un casco convexo
    #Ordenar los puntos: primero en x, luego en y
    puntos_ordenados = sorted(set(postes))

    #Construir el hull* inferior
    # *Se refiere al casco convexo
    lower = []
    for p in puntos_ordenados:
        while len(lower) >= 2 and producto_cruz(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    #Construir el hull superior
    upper = []
    for p in reversed(puntos_ordenados):
        while len(upper) >= 2 and producto_cruz(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    #Eliminar el último punto de cada mitad porque es el punto de inicio del otro
    return lower[:-1] + upper[:-1]

def resolver_optimizado(postes):
    """
    Encuentra el triángulo de área máxima usando el casco convexo

    Algoritmos:
    1. Calcular el hull: O(n log n)
    2. Probar todas las combinaciones de 3 puntos que pertenezcan al hull: O(h^3), donde 'h' es el número de puntos en el hull

    Complejidad total: O(n log n + h^3) donde h <= n típicamente h << n para 500 puntos, 'h' puede ser,
    ~20-50 puntos -> mucho más rápido y eficiente que O(n^3)
    :param postes: Lista de tuplas (x, y) que representan los postes
    :return: Lista de tuplas (x, y) que forman el triángulo de área máxima
    """

    n = len(postes)
    if n < 3:
        print("No hay suficientes postes para formar un triángulo.")
        return None

    #Paso 1: Calcular el casco convexo
    hull = convex_hull(postes)
    h = len(hull)

    print(f"Puntos totales: {n}")
    print(f"Puntos en el hull convexo: {h}")
    print(f"Reducción: {n} -> {h} ({100 * h / n:.1f}%)")

    #Paso 2: Encontrar el triángulo de área máxima dentro del hull
    max_area_doble = 0
    postes_max = []
    for i in range(h):
        for j in range(i + 1, h):
            for k in range(j + 1, h):
                p1 = hull[i]
                p2 = hull[j]
                p3 = hull[k]

                area_actual_doble = calcular_doble_area(p1, p2, p3)

                if area_actual_doble > max_area_doble:
                    max_area_doble = area_actual_doble
                    postes_max = [p1, p2, p3]
    return postes_max

def main():
    archivo_input = 'campo.in'
    archivo_output = 'campo.out'

    postes = leer_postes(archivo_input)

    if not postes:
        print("No se encontraron postes en el archivo de entrada.")
        return
    usar_optimizado = True

    if usar_optimizado:
        print("========= Solución Optimizada (Convex Hull) ==========")
        resultado = resolver_optimizado(postes)
    else:
        print("========= Solución Fuerza Bruta ==========")
        resultado = resolver_fuerza_bruta(postes)
    if resultado:
        escribir_salida(archivo_output, resultado)
        print(f"Triángulo de área máximo encontrado.")
        for i, p in enumerate(resultado, 1):
            print(f"Punto {i}: ({p[0]}, {p[1]})")

        #Calcular y mostrar el área
        area_doble = calcular_doble_area(resultado[0], resultado[1], resultado[2])
        area_real = area_doble / 2.0
        print(f"Área del triángulo: {area_real:.2f}")
        print(f"Resultados guardados en {archivo_output}")

if __name__ == "__main__":
    main()

