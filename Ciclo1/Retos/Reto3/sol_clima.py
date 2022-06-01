# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN.
# NO ELIMINAR LAS IMPORTACIONES A CONTINUACIÓN. SU SOLUCIÓN
# DEBE BASARSE EN EL USO DE ELLAS. SE RECOMIENDA ENSAYAR POR
# APARTE SU PROPUESTA DE SOLUCIÓN USANDO LOS DATOS DE APOYO

import numpy as np

def clima(datos):
    
    #ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA HALLAR LAS
    #FECHAS DE LOS EVENTOS DEL TIEMPO MENCIONADOS EN EL ENUNCIADO.
    #ATÉNGASE AL USO DE LOS RETORNOS PUESTOS AL FINAL DE ESTA FUNCIÓN
    import numpy as np

    arreglo_datos = np.array(datos, dtype='object')
    
    # print(arreglo_datos)
    
    fechas_temp_min =[]
    fechas_temp_max =[]
    fechas_precip_min =[]
    fechas_precip_max =[]
    fechas_max_dias_sol =[]
    salida=[fechas_temp_min, fechas_temp_max, fechas_precip_min, fechas_precip_max, fechas_max_dias_sol]
    
    datos2 = arreglo_datos.reshape(-1,7)
    tam = len(datos2)
    dat=datos2[0:tam,0:7]
    arreglo = []
    fechas_dato= datos2[:,0:1]
    temp_min= datos2[:,1:2]   #columna temperaturas min
    temp_max= datos2[:,2:3]   #columna temperaturas max
    precipit= datos2[:,3:4]   #columna precipitaciones
    dias_sol= datos2[:,6:7]   #columna precipitaciones
    arreglo = [temp_min, temp_max, precipit,precipit, dias_sol ]
    eval= [np.min(temp_min), np.max(temp_max), np.min(precipit), np.max(precipit ), np.max(dias_sol)  ]
    # print(arreglo)
    # print( np.max(dat,axis=0 ) )   #acceder a [ini_fila:fin_fila, ini_col:fin_col]
    cont = 0
    for fechas in arreglo:
        for i in range(0,tam) :
            if fechas[i] == eval[cont] :
                salida[cont].append(fechas_dato[i])
        # print(salida[cont])
        cont += 1

    return fechas_temp_min, fechas_temp_max, fechas_precip_min, fechas_precip_max, fechas_max_dias_sol
