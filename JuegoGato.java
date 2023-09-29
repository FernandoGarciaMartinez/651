
package juegogato;
import java.util.Scanner;

public class JuegoGato {

    static char[] tablero = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
    static String jugadorActual = "X";
    static String estadoActual = "jugando";
    static int turno = 1;

    public static void imprimirInstrucciones() {
        System.out.println("Vamos a jugar al gato");
        System.out.println("El tablero tiene la siguiente estructura");
        System.out.println(" 1 | 2 | 3 ");
        System.out.println("---+---+---");
        System.out.println(" 4 | 5 | 6 ");
        System.out.println("---+---+---");
        System.out.println(" 7 | 8 | 9 ");
    }

    public static void dibujarTablero(char[] tablero) {
        System.out.printf(" %c | %c | %c \n", tablero[0], tablero[1], tablero[2]);
        System.out.println("---+---+---");
        System.out.printf(" %c | %c | %c \n", tablero[3], tablero[4], tablero[5]);
        System.out.println("---+---+---");
        System.out.printf(" %c | %c | %c \n", tablero[6], tablero[7], tablero[8]);
    }

    public static String estadoJuego(char[] tablero) {
        // Revisar horizontales
        if (tablero[0] == tablero[1] && tablero[1] == tablero[2] && tablero[2] != ' ') {
            return "ganador";
        } else if (tablero[3] == tablero[4] && tablero[4] == tablero[5] && tablero[5] != ' ') {
            return "ganador";
        } else if (tablero[6] == tablero[7] && tablero[7] == tablero[8] && tablero[8] != ' ') {
            return "ganador";
        }

        // Revisar verticales
        else if (tablero[0] == tablero[3] && tablero[3] == tablero[6] && tablero[6] != ' ') {
            return "ganador";
        } else if (tablero[1] == tablero[4] && tablero[4] == tablero[7] && tablero[7] != ' ') {
            return "ganador";
        } else if (tablero[2] == tablero[5] && tablero[5] == tablero[8] && tablero[8] != ' ') {
            return "ganador";
        }

        // Revisar diagonales
        else if (tablero[0] == tablero[4] && tablero[4] == tablero[8] && tablero[8] != ' ') {
            return "ganador";
        } else if (tablero[6] == tablero[4] && tablero[4] == tablero[2] && tablero[2] != ' ') {
            return "ganador";
        } else {
            return "jugando";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        imprimirInstrucciones();

        while (true) {
            System.out.printf("El turno del jugador %s\n", jugadorActual);
            System.out.print("Elija la posición a jugar (1-9): ");
            int posicion = scanner.nextInt() - 1;

            if (posicion >= 0 && posicion <= 8) {
                if (tablero[posicion] != ' ') {
                    System.out.printf("La posición %d ya está ocupada, elija otra.\n", posicion + 1);
                    continue;
                } else {
                    tablero[posicion] = jugadorActual.charAt(0);
                    turno++;
                }
            } else {
                System.out.println("Posición no válida");
                continue;
            }

            dibujarTablero(tablero);
            estadoActual = estadoJuego(tablero);

            if (estadoActual.equals("jugando")) {
                // Cambiar de turno X o O
                jugadorActual = (jugadorActual.equals("X")) ? "O" : "X";
            } else if (estadoActual.equals("ganador")) {
                System.out.printf("El jugador %s es el GANADOR\n", jugadorActual);
                break;
            }

            // Salir si los turnos se acaban
            if (turno >= 9) {
                System.out.println("Ya no hay más casillas, juego empatado.");
                break;
            }
        }
    }
}