"""Reto 4 encryptar reto cesar """
# import sol_reto4
from sol_reto4 import encriptar_caracter
from sol_reto4 import encriptar
from sol_reto4 import desencriptar_caracter
from sol_reto4 import desencriptar
b= 7
palabra= "U DE A*"
caracter = "U"
print(palabra)
print(caracter)
print(encriptar_caracter(caracter, b) ) #"U"
print( encriptar(palabra, b) )
print( desencriptar_caracter(encriptar_caracter(caracter, b), b)  )
print( desencriptar(encriptar(palabra, b), b)  )
