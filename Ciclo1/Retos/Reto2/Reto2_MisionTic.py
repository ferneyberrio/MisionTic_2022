estudiante1 = {
    "cédula":'00014301503',
    "nombre":'Pepito',
    "nota_fundamentos":4.3
              }

estudiante2 = {
    "cédula":'1037678471',
    "nombre": 'Fulanito',
    "nota_fundamentos":3.2
              }

estudiante3 = {
    "cédula": '71023567',
    "nombre":'Pacho',
    "nota_fundamentos":5
              }

estudiante4 = {
    "cédula":'32276123',
    "nombre":'Rita',
    "nota_fundamentos":4.7
              }

estudiante5 = {
    "cédula":'1036765245',
    "nombre":'Anita',
    "nota_fundamentos":4.7
              }

estudiante6 = {
    "cédula":'89122456',
    "nombre":'Pedrito',
    "nota_fundamentos":4.7
              }

estudiante7 = {
    "cédula":'289765345',
    "nombre":'Mat',
    "nota_fundamentos":4.8
              }  

estudiante8 = {
    "cédula":'4576890',
    "nombre":'Dan',
    "nota_fundamentos":4.8
              }
estudiante9 = {
    "cédula":'4576890',
    "nombre":'Dan',
    "nota_fundamentos":4.8
              }              

mi_grupo = [ estudiante1, estudiante2, estudiante3, estudiante4,
            estudiante5, estudiante6, estudiante7, estudiante8,estudiante9] 

for mi_val in mi_grupo:  
    print(mi_val)

def calcular_promedio_y_cuadro_honor(grupo) :
    
    import numpy as np                    # importar librería
    import math
    cuadro_honor = { 1:[], 2:[], 3:[] }   #diccionario cuadro de Honor                       
    notas=[]                              #lista vacia

    for i in grupo:                         # separar datos
        notas.append(i['nota_fundamentos']) # almacena todas las notas

    #tratamiento notas
    promedio = np.mean(np.array(notas))    #promedio grupo
    notas=list(set(notas))                 #eliminar duplicados
    notas_ord= np.sort(notas )[::-1]       # ordenar en orden descendente

    #cuadro de Honor
    for m in range(0,3):                   #posiciones podio
        for estu in grupo  :                  # recorrer lista            
            if estu['nota_fundamentos']== notas_ord[m]:  #si nota = posic podio
                cuadro_honor[m+1].append(estu['cédula']) #almacenar en posic podio



    return promedio, cuadro_honor

print(calcular_promedio_y_cuadro_honor(mi_grupo) )   # llamdo de la función
    