public class Solution{
    //ESTA CLASE NO TIENE MAIN
    
    
    public static double[] reporte(double[] listaNotas) {
        //EN ESTE ESPACIO PONER SU LÓGICA
    double num_personas = 0.0, firstPuesto = 5.0, lastPuesto = 0.0;     // datos requeridos
        double resultados[] = {num_personas, firstPuesto, lastPuesto};   // declaración e instanciación de array
        double suma = 0.0;    // sumar elementos del arreglo

        num_personas = listaNotas.length ;   // obtener numero de participantes
        
        
        
        for( int i=0; i < num_personas; i++ ){
            if( listaNotas[i] > lastPuesto  ){
            lastPuesto =   listaNotas[i];            
            }//fin if

            if( listaNotas[i] < firstPuesto  ){
            firstPuesto =   listaNotas[i];  
            }//fin if
            
            suma += listaNotas[i];    // suma cada elemento

        }// fin for
        double promedio = suma/num_personas;
    
    
        resultados = new double[] { promedio, firstPuesto, lastPuesto};
        return resultados ;    
        
        
        
        
    }
}
