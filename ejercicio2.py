from datetime import datetime

class Coche:
    def __init__(self, marca, modelo, anio_fabricacion):
        "Inicializa las propiedades del coche"
        self.marca = marca  
        self.modelo = modelo  
        self.anio_fabricacion = anio_fabricacion  

    def obtener_marca(self):
        """Devuelve la marca del coche."""
        return self.marca

    def establecer_marca(self, marca):
        "Establece una nueva marca para el coche."
        self.marca = marca

    def obtener_modelo(self):
        "Devuelve el modelo del coche"
        return self.modelo

    def establecer_modelo(self, modelo):
        "Establece un nuevo modelo para el coche"
        self.modelo = modelo

    def obtener_anio_fabricacion(self):
        "Devuelve el año de fabricación del coche"
        return self.anio_fabricacion

    def establecer_anio_fabricacion(self, anio):
        "Establece un nuevo año de fabricación para el coche"
        self.anio_fabricacion = anio

    def obtener_antiguedad(self):
        "Devuelve los años que han pasado desde que se fabricó el coche"
        anio_actual = datetime.now().year
        return anio_actual - self.anio_fabricacion



if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", 2015)


    print(f"Marca: {coche1.obtener_marca()}")
    print(f"Modelo: {coche1.obtener_modelo()}")
    print(f"Año de fabricación: {coche1.obtener_anio_fabricacion()}")
    print(f"Años de antigüedad: {coche1.obtener_antiguedad()}")


    coche1.establecer_marca("Honda")
    coche1.establecer_modelo("Civic")
    coche1.establecer_anio_fabricacion(2018)

    print("\nDespués de actualizar:")
    print(f"Marca: {coche1.obtener_marca()}")
    print(f"Modelo: {coche1.obtener_modelo()}")
    print(f"Año de fabricación: {coche1.obtener_anio_fabricacion()}")
    print(f"Años de antigüedad: {coche1.obtener_antiguedad()}")
