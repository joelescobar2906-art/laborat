class Sensor:
    tipo: str = "Genérico"

    def __init__(self, id_sensor: str):
        self.id = id_sensor
        self.encendido = False

    def activar(self):
        self.encendido = True
        print(f"Sensor [{self.id}] activado.")

    def desactivar(self):
        self.encendido = False
        print(f"Sensor [{self.id}] desactivado.")


class Camara(Sensor):
    tipo: str = "Cámara"

    def __init__(self, id_sensor: str, resolucion: str):
        Sensor.__init__(self, id_sensor)
        self.resolucion = resolucion


class SensorLuzLaser(Sensor):
    tipo: str = "Luz Laser"

    def __init__(self, id_sensor: str, alcance: int):
        Sensor.__init__(self, id_sensor)
        self.alcance = alcance


class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo: str = "Vehículo Autónomo"

    def __init__(self, id_sensor: str, resolucion: str, alcance: int):
        # Inicializamos ambas ramas explícitamente sin conflictos
        Sensor.__init__(self, id_sensor)
        self.resolucion = resolucion
        self.alcance = alcance

    def mostrar_estado(self):
        print(f"--- ESTADO DEL {self.tipo.upper()} ---")
        print(f"ID: {self.id}")
        print(f"Resolución de Cámara: {self.resolucion}")
        print(f"Alcance de Luz Láser: {self.alcance} metros")
        print(f"Encendido: {self.encendido}")


if __name__ == "__main__":
    print("--- EJECUTANDO SISTEMA DE VEHÍCULO AUTÓNOMO ---")
    mi_vehiculo = VehiculoAutonomo("AUT-01", "4K", 150)
    mi_vehiculo.activar()
    mi_vehiculo.mostrar_estado()