
package funciones;

public class funcionesGenerales {
    
    public String removerAcentos(String palabraOrigen){
            String palabraRetorno = palabraOrigen.toLowerCase();
            String conAcentos = "áéíóú";
            String sinAcentos = "aeiou";
            
            int ejemplares = conAcentos.length();
            for (int i=0; i < ejemplares; i ++ ){
                palabraRetorno = palabraRetorno.replace(conAcentos.charAt(i), sinAcentos.charAt(i));
            }
                
            
            return palabraRetorno;
        }
}

