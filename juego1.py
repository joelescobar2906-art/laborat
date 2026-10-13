import random

class Juego:
    def __init__(self, vidas_iniciales: int):
        self.numero_de_vidas = vidas_iniciales
        self.record = 0

    def reinicia_partida(self):
        self.numero_de_vidas = 3

    def actualiza_record(self):
        print("¡Récord actualizado!")

    def quita_vida(self) -> bool:
        self.numero_de_vidas -= 1
        return self.numero_de_vidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas: int):
        super().__init__(vidas)
        self.numero_a_adivinar = 0

    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = random.randint(0, 10)
        
        while True:
            try:
                numero_ingresado = int(input("Adivina un número entre el 0 y el 10: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue
            
            if numero_ingresado == self.numero_a_adivinar:
                print("¡Acertaste!!")
                self.actualiza_record()
                break
            else:
                quedan_vidas = self.quita_vida()
                if quedan_vidas:
                    if numero_ingresado < self.numero_a_adivinar:
                        print("El número a adivinar es MAYOR. Inténtalo de nuevo.")
                    else:
                        print("El número a adivinar es MENOR. Inténtalo de nuevo.")
                else:
                    print(f"Te has quedado sin vidas. Fin del juego. El número era: {self.numero_a_adivinar}")
                    break

if __name__ == "__main__":
    print("--- EJECUTANDO JUEGO 1 ---")
    juego = JuegoAdivinaNumero(3)
    juego.juega()