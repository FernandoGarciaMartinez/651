import time

class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.felicidad = 50
        self.energia = 100
        self.sed = 0  # Nuevo atributo para la sed
        self.vivo = True

    def alimentar(self):
        if self.hambre > 0:
            self.hambre -= 20
            self.felicidad += 10
            self.energia -= 5
            if self.hambre < 0:
                self.hambre = 0  # Evita valores negativos
            print(f"{self.nombre} ha sido alimentado.")
        else:
            print(f"{self.nombre} no tiene hambre en este momento.")

    def jugar(self):
        if self.energia >= 20:
            self.felicidad += 15
            self.energia -= 20
            if self.energia < 0:
                self.energia = 0  # Evita valores negativos
            print(f"{self.nombre} está jugando contigo.")
        else:
            print(f"{self.nombre} está demasiado cansado para jugar.")

    def dormir(self):
        self.energia = 100
        print(f"{self.nombre} ha dormido bien.")

    def beber_agua(self):
        if self.energia > 10:
            self.felicidad += 5
            self.energia -= 10
            self.sed = 0  # Restaura la sed
            if self.energia < 0:
                self.energia = 0  # Evita valores negativos
            print(f"{self.nombre} ha tomado agua y se siente mejor.")
        else:
            print(f"{self.nombre} está demasiado cansado para tomar agua en este momento.")

    def estado(self):
        print(f"{self.nombre} - Hambre: {self.hambre}, Felicidad: {self.felicidad}, Energía: {self.energia}, Sed: {self.sed}")

    def vivir(self):
        while self.vivo:
            self.hambre += 10
            self.felicidad -= 5
            self.energia -= 10
            self.sed += 5  # Incrementa la sed con el tiempo
            if self.hambre >= 100:
                self.hambre = 100  # Evita que el hambre supere 100
            if self.felicidad <= 0 or self.energia <= 0:
                self.vivo = False
                print(f"{self.nombre} ha fallecido.")
            else:
                self.estado()
                accion = input("¿Qué deseas hacer? (alimentar/jugar/dormir/beber/salir): ").lower()
                if accion == "alimentar":
                    self.alimentar()
                elif accion == "jugar":
                    self.jugar()
                elif accion == "dormir":
                    self.dormir()
                elif accion == "beber":
                    self.beber_agua()
                elif accion == "salir":
                    self.vivo = False
                    print(f"{self.nombre} se ha ido.")
                else:
                    print("Acción no válida.")

if __name__ == "__main__":
    nombre = input("Elige un nombre para tu Tamagotchi: ")
    mi_tamagotchi = Tamagotchi(nombre)
    mi_tamagotchi.vivir()
