from email.policy import default

#Creación de  la clase nodo para ser utilizada en el árbol
class Nodo:
    def __init__(self, valor, izq= None, der=None, cen = None):
        self.valor = valor
        self.izq = izq
        self.der = der
        self.cen = cen
#Construcción del árbol directamente con los nodos enlazados
head = Nodo(
    20,
    izq=Nodo(23, cen=Nodo(57)),
    cen=Nodo(19, cen=Nodo(67),der=Nodo(99)),
)
#Imprimimos los valores requeridos
print(head.izq.cen.valor) #Debe imprimir 57

print(head.cen.der.valor) #Debe imprimir 99