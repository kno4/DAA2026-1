def suma_lista(lista: list):
    """suma_lista
    Función que realiza con
    recursividad la suma de los elementos de una lista
    :param lista: list : lista de enteros
    :return: int:  suma de los elementos de la lista
    """
    #Caso base: La lista está vacia
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])


#arr = [0, 0, 1, 2, 3, 5, 8, 13]
#print(suma_lista(arr))

def contar_digts(num):
    """"
    contar_digts
    Función que cuenta el número de dígitos que tiene un número entero usando recursividad
    :param: num El número entero
    :return: int el número de dígitos en el número

    """

    # Caso base: que el número tenga solo un dígito
    if abs(num) < 10:
        return 1
    else:
        return 1 + contar_digts(num // 10)

#numero = 45634
#print(contar_digts(numero))


"""
    valor_medio 
    Función que saca recursivamente el valor de enmedio de un Stack ADT 
    Clase Stack (Pila)
    :param: index El index que 
            pila un objeto de la clase pila del cual se desea eliminar el dato
    :return: string Confirmación de eliminado
    
"""
def valor_medio(index, pila):

    tamanio = pila.length()
    if tamanio == 0 or index < 0 or index >= tamanio:
        print("Error, el índice está fuera de rango")
    if index == 0:
        pila.pop()
        return


    temp = pila.pop()
    valor_medio(index - 1, pila)
    pila.push(temp)


class Stack:
    def __init__(self):
        self.dato = []

    def esta_vacia(self):
        return self.length() == 0

    def length(self):
        return len(self.dato)

    def pop(self):
        return self.dato.pop()

    def peek(self):
        return self.dato[-1]

    def push (self, dato):
        self.dato.append(dato)

    def __str__(self):
        info = "-----"
        for elem in self.dato[-1::-1]:
            print (" ",elem," ", "\n|---|")

"""
pila = Stack()
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.push(5)
valor_medio(2, pila)
print(pila.__str__())
"""

def es_palindromo(cadena: str):
    
    """es_palindromo
    Funcion que usando recursividad, revisa si una cadena es un palindromo
    :param cadena: cadena de entrada
    :return: True si es palindromo, False de lo contrario
    """
    def limpiar_cadena(cadena: str):
        """limpiar_cadena
        Funcion que limpia los caracteres no alfanumericos de una cadena
        :param cadena: cadena de entrada
        :return: cadena limpia
        """
        if cadena == None:
            return cadena

        cadena_limpia = cadena.lower()

        car_no_val = ['á','é','í','ó','ú','ñ','ü','¡','!','¿','?','.',',','(',')',':',';','-',' ']

        car_validos = {'á':'a','é':'e','í':'i','ó':'o','ú':'u','ñ':'n','ü':'u','¡':'','!':'','¿':'','?':'', '.':'', ',':'',
                    '(':'',')':'', ':':'',';':'','-':'', ' ':''}

        for caracter in cadena_limpia:
            if caracter in car_no_val:
                cadena_limpia = cadena_limpia.replace(caracter, car_validos[caracter])

        return cadena_limpia

    if len(cadena) <= 1:
        return True
    else:
        cadena = limpiar_cadena(cadena)
        if cadena [0] == cadena[-1]:
            return es_palindromo(cadena[1:-1])
        else:
            return False

cad = "anita lava la tina"
print(es_palindromo(cad))
