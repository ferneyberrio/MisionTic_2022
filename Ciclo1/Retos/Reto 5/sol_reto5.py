#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para el funcionamiento de las librería csv y json respectivamente
import csv, json
from operator import index
def solucion():
    import numpy as np
    import pandas as pd

    data = pd.read_csv('JandJ.csv')
    # print(data[1:5] )  #de la columna Open imprimir filas 0 a la 2
    # print( data["Open"][0:3])  #de la columna Open imprimir filas 0 a la 2
    # print( data["Open"][0]-data["Close"][0])  #de la columna Open imprimir filas 0 a la 2

    tam = len(data)
    archivo2 = open('analisis_archivo.csv','a')   # abrir y si no existe crear
    archivo2.write("Fecha analizada\tComportamiento de la accion\tabs Diferencia Close-Open\n")
    absol=[]   # lista vacia para almacenar el valor absoluto
    for i in range(tam ):
        absol.append (data["Close"][i] - data["Open"][i]  )
        if absol[i] > 0 :
            difer= "SUBE"
        elif absol[i] < 0 :
            difer = "BAJA"         
        else: 
            difer = "ESTABLE"                       
        
        archivo2.write('%s\t' % data["Date"][i])
        archivo2.write('%s\t' % difer)
        archivo2.write('%s\n' % abs( absol[i] ) )  
    archivo2.close()

    diccionario={}      # crear diccionario vacio
    lowest=min(data["Volume"]); highest=max(data["Volume"]); mean= np.mean(data["Volume"]);greatest=max(absol)
    comp= [ lowest, highest, greatest ]
    datos=[data["Volume"], data["Volume"], absol ]
    claves=['date_lowest_volume','lowest_volume','date_highest_volume','highest_volume','date_greatest_difference','greatest_difference']

    cont=0
    for i in comp:
        for j in range(tam):
            pos=comp.index(i)
            if datos[pos][j] == i:
                diccionario[claves[cont] ] = data["Date"][j]
                diccionario[claves[cont+1] ] = i
        cont += 2

    diccionario['mean_volume'] = mean

    with open('detalles.json','w') as archivo:
        json.dump(diccionario,archivo)
