
def fn_buscar(arreglo, k):
    for num in range(len(arreglo)):
        if arreglo[num] == k:
            return num
    return -1
#En el peor de los casos, se recorren todos los valores del arreglo T(n)
arreglo = [10, 12, 30 , 14, 15, 18, 22, 19, 22, 28]
K= 18
#En espacio, se ocupa solo dos espacios de memoria S(c)
res = fn_buscar(arreglo, K)
if res == -1:
    print(f"Valor {K} no encontrado")
else:
    print(f"Valor {K} encontrado en el índice: {res}")