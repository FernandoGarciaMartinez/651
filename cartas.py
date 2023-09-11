class Carta:

    def __init_(self, numero, palo):
        self.palo = palo
        self.numero = numero

    def imprimir(self):
        print(self.numero, "de", self.palo)

carta1 = Carta(7, "Espadas")
carta2 = Carta(8, "Diamantes")
carta1.imprimir()
carta2.imprimir()