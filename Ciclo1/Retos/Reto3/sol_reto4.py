""" solución al reto 4 encriptar cesar Ferney Berrio Zuleta"""

#COMPLETA LAS SIGUIENTES CUATRO (4) FUNCIONES
lista =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']

def encriptar_caracter(caracter, b): 
    return Cesar(caracter, b, "+")
  
def encriptar(mensaje, b):
    return Cesar(mensaje, b, "+")   
 
def desencriptar_caracter(caracter_encriptado, b):
    return Cesar(caracter_encriptado, b, "-")


def desencriptar(mensaje_encriptado, b):
    return Cesar(mensaje_encriptado, b, "-")

# función que unifica las 4 ateriores 
def Cesar(msm, b,sig):  # mensaje, cclave desifrado, "+" = cifra, "-" =descifra
    msm_ = ""
    for letra in msm:                    #recorro el string
        if letra in lista:               #letra esta en la lista
            a = lista.index(letra)       #posición de esa letra enla lista
            if sig == "+":               #
                ocesar = (a+b)%27        # encripta
            else: 
                ocesar = (a-b)%27        # desencripta
            msm_ += lista[ocesar]        #adiciono a la lista de salida la letra cifrada/descifrada
        else:                            #aqui es donde evaluo los espacios, o cualquier otro caracte no sea un letra del abecedario
            msm_ += letra                # adiciono el valor q no esta en la lista(espacios, caract especiales etc)
    return msm_

# # """
# # ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE!
# # NO AÑADIR CÓDIGO FUERA DE LAS FUNCIONES ESPECIFICADAS EN EL ENUNCIADO
# # """