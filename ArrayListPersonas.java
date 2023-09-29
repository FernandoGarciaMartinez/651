package arraylistpersonas;
import java.util.ArrayList;
public class ArrayListPersonas {


    public static void main(String[] args) {
        ArrayList<Persona> listaPersonas = new ArrayList<>();
        listaPersonas.add (new Persona (1,"Benito",15));
        listaPersonas.add (new Persona (2,"Ana",17));
        listaPersonas.add (new Persona (3,"Juan",25));
        
//System.out.println(listaPersonas); 
System.out.println("-----FOR-----");
for (int i = 0; i < listaPersonas.size(); i++){
    System.out.println("Contenido: "+ listaPersonas.get(i).getNombre());
}
        System.out.println("----FOR EACH-----");
        for(Persona pepol: listaPersonas){
            System.out.println("Contenido:" + pepol.getNombre());
        }
    }
    
}
