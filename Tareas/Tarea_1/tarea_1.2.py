
encontrado = False
diccionario = {}
arreglo = [2, 4, 5, 6, 7, 9, 10, 15]
K= int(input("Ingrese el valor de K: "))

for num in arreglo:
    complemento = K - num
    if complemento in diccionario:
        print(f"Encontrado: {complemento} + {num} = {K}")
        encontrado = True
        break

    diccionario[num] = True

if not encontrado:
    print("No existe ninguna combinación")
