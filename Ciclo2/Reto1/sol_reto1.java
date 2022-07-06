
package retos1_ciclo2;

import java.util.Arrays;
import java.util.Scanner;

/**
 *
 * @author Ferney
 */
public class sol_reto1 {
// public int[] participantes = new int[] {26, 17, 23, 16, 24, 21, 18, 25, 22, 20, 19} ;
// public int[] res = new int[] {0, 0, 0} ;
    Scanner captura = new Scanner(System.in);   //creo objeto para solicitar a usuario
    private String msm1="dato";
    private String msm2="dato";
    private String msm3="dato";
    private int[] participantes = new int[] {26, 17, 23, 16, 24, 21, 18, 25, 22, 20, 19} ;
    private double[] notas = new double[] {4.1, 4.8, 1.5, 0.1, 0.9, 1.4, 1.5, 3.0} ;
    private int[] resEsperada = new int[3]  ;
    private double[] resEsperadaD = new double[3]  ;
    
    private int[] res = new int[3]  ;
    private double[] resD = new double[3]  ;
      
    

    public static void main(String[] args) {
        // TODO code application logic here
        sol_reto1 reto;    // objeto para mostrar resultado
        reto = new sol_reto1();    // instanciar objeto
        
        /* pedir datos a usuario */
        System.out.println("Que reto desea solucinar : \n"+"1. Reto Tienda\n"+
                "2. Reto Notas\n"+"3. Reto Carrera \n");    // salida por pantalla
        int seleccion = reto.captura.nextInt();    // capturamos ingreso del usuario
        
        /* LLEVAR AL CASE CORRECPONDIENTE */   
        reto.tipoReto(seleccion);

//        Retos1_ciclo2 objeto  ;    //creo objeto carrera de la clase Retos1_ciclo
//        objeto = new  Retos1_ciclo2()  ;   // instancio
            
    }// fin public static void main
 
    /* método para mostrar resultados*/
    public void respuesta(String A, String B, String C, int[] arreglo){
        String texto[] = {A, B ,C};
        sol_reto1 reto;    // objeto para mostrar resultado
        reto = new sol_reto1();    // instanciar objeto
        float calif=0.0f;
        
        System.out.println( "para el arreglo : " + Arrays.toString(reto.participantes) ) ;
        
        for(int i = 0 ; i < 3; i++  ){            
            System.out.println( "\nPara El "+ texto[i] ) ;
            System.out.print("se esperaba : " + resEsperada[i]) ;
            System.out.print("  /  Su respuesta fue : " + arreglo[i]) ;

            if( resEsperada[i] == arreglo[i] ){            
                calif += (5.0/3);
                System.out.println("  ! correcto !");                         
            }// fin if
            else{System.out.println("  ! INCORRECTO !"); }
        }//fin for
        System.out.printf("%n su calificación es : %.2f / 5  %n" , calif ) ;

    }// fin método respuesta

    /* método para evaluar el reto seleccionado*/    
    public void tipoReto(int seleccion){
        sol_reto1 reto;    // objeto para mostrar resultado
        reto = new sol_reto1();    // instanciar objeto
        
        Retos1_ciclo2 objeto  ;    //creo objeto carrera de la clase Retos1_ciclo
        objeto = new  Retos1_ciclo2()  ;   // instancio
        
        int arr =participantes.length;
        int tam = arr;
        int Lista[] = new int[tam];
        Lista = reto.participantes;
        
        // para variante en double
        int arrD =notas.length;
        int tamD = arrD;
        double ListaD[] = new double[tamD];
        ListaD = this.notas;
        
        Arrays.sort(Lista);  // ordenar lista
        Arrays.sort(ListaD);  // ordenar lista
        switch(seleccion){
            case 1:   // reto tienda
            res = objeto.reporte(participantes);
            
            msm1 = "Costo total :"; msm2 = "Producto más barato : "; msm3 = "Producto más caro";   
            reto.resEsperada = new int[]{Arrays.stream(Lista).sum() ,Lista[0],Lista[tam-1]} ;
            reto.respuesta( msm1 ,msm2,msm3,  res );
            break;
            
            case 2: // reto notas
            resD = objeto.reporte(notas);
            
            msm1 = "Promedio de lista de notas :"; msm2 = "Nota más baja : "; msm3 = "Nota más alta";   
            resEsperadaD = new double[]{Arrays.stream(notas).sum() /  tamD ,ListaD[0],ListaD[tamD-1]} ;
            System.out.println( "la respuesta correcta es : " + Arrays.toString(resEsperadaD) ) ;
            System.out.println( "su respuesta es : " + Arrays.toString(resD) ) ;
            if( resD[0]==resEsperadaD[0] && resD[1]==resEsperadaD[1] && resD[2]==resEsperadaD[2] ){
                System.out.println(" su resultado es ! Correcto ¡");  
            }// fin if
            else{System.out.println("su resultado es ! INCORRECTO ¡");}// fin else

            break;
            
            case 3:// reto carrera
            res = objeto.reporte(participantes);
            
            msm1 = "número participantes :"; msm2 = "primer puesto : "; msm3 = "Ultimo puesto : ";   
            reto.resEsperada = new int[]{tam ,Lista[0],Lista[tam-1]} ;
            reto.respuesta( msm1 ,msm2,msm3,  res );
            break;         
            
            default:
                
        }// fin switch case
        
    }// finmétodo tipo reto

}// fin class
