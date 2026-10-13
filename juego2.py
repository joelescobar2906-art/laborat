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
class JuegoAdivinaNumeroExtendio(Juego):
    def __init__(self, vidas: int):
        super().__init__(vidas)
        self.numero_a_adivinar = 0
    def valida_numero(self, numero: int) -> bool:
        return 0 <= numero <= 10
    def generar_numero_secreto(self):
        self.numero_a_adivinar = random.randint(0, 10)
    def juega(self):
        self.reinicia_partida()
        self.generar_numero_secreto()
        while True:
            try:
                numero_ingresado = int(input("Adivina un número entre el 0 y el 10: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue
            if not self.valida_numero(numero_ingresado):
                print("Error: El número debe estar entre 0 y 10.")
                continue
            if numero_ingresado == self.numero_a_adivinar:
                print("¡Acertaste!!")
                self.actualiza_record()
                break
            else:
                if not self.quita_vida():
                    print(f"¡Te quedaste sin vidas! El número era: {self.numero_a_adivinar}")
                    break
                else:
                    if numero_ingresado < self.numero_a_adivinar:
                        print("El número es mayor.")
                    else:
                        print("El número es menor.")
class JuegoAdivinaPar(JuegoAdivinaNumeroExtendio):
    def valida_numero(self, numero: int) -> bool:
        if super().valida_numero(numero):
            if numero % 2 == 0:
                return True
            else:
                print("Error: El número ingresado no es PAR.")
                return False
        print("Error: El número está fuera del rango (0-10).")
        return False
    def generar_numero_secreto(self):
        pares = [0, 2, 4, 6, 8, 10]
        self.numero_a_adivinar = random.choice(pares)
class JuegoAdivinaImpar(JuegoAdivinaNumeroExtendio):
    def valida_numero(self, numero: int) -> bool:
        if super().valida_numero(numero):
            if numero % 2 != 0:
                return True
            else:
                print("Error: El número ingresado no es IMPAR.")
                return False
        print("Error: El número está fuera del rango (0-10).")
        return False
    def generar_numero_secreto(self):
        impares = [1, 3, 5, 7, 9]
        self.numero_a_adivinar = random.choice(impares)
if __name__ == "__main__":
    print("--- EJECUTANDO JUEGO 2 (Los tres juegos obligatorios) ---")
    print("\n--- 1. Juego Adivina Número (Normal) ---")
    juego_normal = JuegoAdivinaNumeroExtendio(3)
    juego_normal.juega()
    print("\n--- 2. Juego Adivina Número Par ---")
    juego_par = JuegoAdivinaPar(3)
    juego_par.juega()
    print("\n--- 3. Juego Adivina Número Impar ---")
    juego_impar = JuegoAdivinaImpar(3)
    juego_impar.juega()