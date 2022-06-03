pensum = [{ '0123': {'nombre': 'intro a la ing', 'créditos': 2},
           '4567': {'nombre': 'inglés', 'créditos': 1}},
            {},
            {}]
# print(pensum)            
# dicc={}
# dicc= dict( hola=25.3, dato=52 )
# pos =list (dicc.keys() )
# print(pos )
# print(dicc['hola'])
# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# NO MODIFICAR EL NOMBRE, PARÁMETROS O RETORNO DE LA FUNCIÓN
def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN modificar_materia (En este espacio debes 
    # poner el código necesario para implementar esta funcionalidad)
    #pensum = [{'0123': {'nombre': 'intro a la ing', 'créditos': 2},'4567': {'nombre': 'inglés', 'créditos': 1}},{}, {}]
    n=len(pensum)
    mensaje= "Ingrese un semestre válido"
    if semestre >=1 and semestre <=n:
        if pensum[semestre-1]!={}:
            semestre_pensum=pensum[semestre-1]
            if materia in semestre_pensum:
                semestre_pensum[materia]['nombre']=nombre
                semestre_pensum[materia]['créditos']=creditos
                mensaje="Modificada con éxito"
            else:
                mensaje="La materia no existe"     
        elif pensum[semestre-1]== {} :
            mensaje="El semestre no tiene materias"


    # ACÁ TERMINA LA FUNCIÓN modificar_materia
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    print(mensaje) 

    return mensaje

modificar_materia(pensum, 3, '0123', 'lecto escritura ', 3) 
