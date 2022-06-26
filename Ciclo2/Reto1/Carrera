public class Solution{
    //ESTA CLASE NO TIENE MAIN
    
    
    public static int [] reporte(int [] participantes){
        //EN ESTE ESPACIO PONER SU LÓGICA

    int num_personas = 0, firstPuesto = 10000, lastPuesto = 0;     // datos requeridos
    
//    int[] resultados = new int[3];   // declaración array
//    int[] resultados = new int[]{0,0,0};   // declaración e instanciación de array
    int resultados[] = {num_personas, firstPuesto, lastPuesto};   // declaración e instanciación de array
    
    num_personas = participantes.length ;   // obtener numero de participantes

    for( int i : participantes ){
        if( i > lastPuesto  ){
        lastPuesto =   i;  
        }//fin if
       
        if( i < firstPuesto  ){
        firstPuesto =   i;  
        }//fin if
        
    }// fin for
    
    
    resultados = new int[] { num_personas, firstPuesto, lastPuesto};
        return resultados ;
        
        
    }
}
