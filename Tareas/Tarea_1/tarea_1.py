
encontrado = False

arreglo = [2, 4, 5, 6, 7, 9, 10, 15]

K= int(input("Ingrese el valor de k: "))

for i in range(len(arreglo)):
    for j in range(len(arreglo)):
        if arreglo[i] + arreglo[j] == K:
            print(f"Encontrado: {arreglo[i]} + {arreglo[j]} = {K}")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print("No se encontró ninguna combinación")