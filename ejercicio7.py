class Banco:
    def __init__(self, nombre, tasa_interes):
        "Inicializa el banco con nombre y tasa de interés anual en porcentaje"
        self.nombre = nombre
        self.tasa_interes = tasa_interes  

    def obtener_nombre(self):
        "Devuelve el nombre del banco"
        return self.nombre

    def establecer_nombre(self, nombre):
        "Establece un nuevo nombre para el banco"
        self.nombre = nombre

    def obtener_tasa_interes(self):
        "Devuelve la tasa de interés anual"
        return self.tasa_interes

    def establecer_tasa_interes(self, tasa):
        "Establece una nueva tasa de interés anual"
        self.tasa_interes = tasa

    def calcular_interes(self, capital, años):
        
        interes = capital * (self.tasa_interes / 100) * años
        return interes

    def tiempo_para_duplicar(self):
        
        if self.tasa_interes == 0:
            return float('inf')  
        return 72 / self.tasa_interes



if __name__ == "__main__":
    banco1 = Banco("Banco Central", 6)  

    print(f"Banco: {banco1.obtener_nombre()}")
    print(f"Tasa de interés: {banco1.obtener_tasa_interes()}% anual")

    capital = 10000
    años = 3

    interes_ganado = banco1.calcular_interes(capital, años)
    tiempo_duplicar = banco1.tiempo_para_duplicar()

    print(f"Interés ganado por ${capital} en {años} años: ${interes_ganado:.2f}")
    print(f"Tiempo estimado para duplicar el capital: {tiempo_duplicar:.2f} años")

    # Cambiar datos
    banco1.establecer_tasa_interes(8)
    print("\nDespués de actualizar tasa de interés:")
    print(f"Tasa de interés: {banco1.obtener_tasa_interes()}% anual")
    print(f"Nuevo tiempo para duplicar capital: {banco1.tiempo_para_duplicar():.2f} años")
