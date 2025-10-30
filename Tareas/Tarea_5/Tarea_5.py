


alfabeto ="abcdefghijklmnñopqrstuvwxyz ,."
def descifrado_Cesar(mensaje_cifrado):
    """descifrado_Cesar
    Función que realiza el descifrado de un mensaje previamente cifrado
    :param mensaje_cifrado: mensaje ya cifrado
    :return: mensaje descifrado
    """
    longitud = len(alfabeto)
    print("Probando todas las claves posibles")
    for clave in range(longitud):
        texto_descifrado=""
        for caracter in mensaje_cifrado:
            if caracter in alfabeto:
                posicion_actual = alfabeto.find(caracter)
                nueva_posicion = (posicion_actual-clave)%longitud
                texto_descifrado += alfabeto[nueva_posicion]
        else:
            texto_descifrado += caracter

        print(f"Clave {clave}: {texto_descifrado}")

mensaje = "l.ziu,mf .fzmk,wzilwgfqw mfai kwukmsw flw,wfifsif.upamz plilflmf .fik,.isfm k.lwfmufmsfk.isfmsfiñ.psiftmcpkiuifdfmsfkwulwzfiulpuwgfk.isfiamfjpkmnisigfxzw,mñmufmsflm xspmñ.mflmsftixiflmfitmzpkifsi,puigflm lmfsifnzwu,mzifuwz,mflmftmcpkwfoi ,ifmsfkijwflmfowzuw gfxsi tiulwfsif.upnpkikpwuflmfsw fpjmzwitmzpkiuw gfu.m ,zwfkwu,pumu,mfu.mawfdfiu,pñ.wgfxzmlm ,puilwfifkwu,mumzf.uifzieify.pu,igfsifzieifkw tpkigfmufsifk.isf mfn.ulpziufsi flp xmz i fdf mfkwu .tizifsif.uplilh"
descifrado_Cesar(mensaje)

def producto_list(lista: list):
    """ producto_list
    Función que prueba el producto de todos los números de la lista y encuentra el producto mayor
    :param lista: lista con números
    :return: producto mayor
    """
    if len(lista)<2:
        print("La lista debe contener al menos dos números")
    prod_max = float("-inf")
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            producto = lista[i]*lista[j]
            if producto > prod_max:
                prod_max = producto
    return prod_max

def ex5(n):
    count = 0
    for i in range (n):
        for j in range (n+1):
            count += 1
    return count

numero = 10
print(ex5(numero))
