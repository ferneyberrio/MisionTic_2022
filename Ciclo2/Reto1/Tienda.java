public class Solution{
    //ESTA CLASE NO TIENE MAIN
    
    
    public static int [] reporte(int [] compra){
        //EN ESTE ESPACIO PONER SU LÓGICA
        
        int participantes[] = compra;
        
      int num_personas = 0, firstPuesto = 10000, lastPuesto = 0;     // datos requeridos
        int resultados[] = {num_personas, firstPuesto, lastPuesto};   // declaración e instanciación de array

        num_personas = participantes.length ;   // obtener numero de participantes
        int suma = 0;
        for( int i : participantes ){
            if( i > lastPuesto  ){
            lastPuesto =   i;  
            }//fin if

            if( i < firstPuesto  ){
            firstPuesto =   i;  
            }//fin if
            suma += i;

        }// fin for
        
    
        resultados = new int[] { suma, firstPuesto, lastPuesto};
        return resultados ;  
        
        
        
    }
}
