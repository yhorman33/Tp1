import math

class Circulo:
    def __init__(self, radio):
        "Inicializa las propiedades del círculo"
        self.radio = radio              
        self.diametro = 2 * radio      

    def obtener_radio(self):
        "Devuelve el radio del círculo"
        return self.radio

    def establecer_radio(self, radio):
        "Establece un nuevo radio y actualiza el diámetro"
        self.radio = radio
        self.diametro = 2 * radio

    def obtener_diametro(self):
        "Devuelve el diámetro del círculo"
        return self.diametro

    def establecer_diametro(self, diametro):
        "Establece un nuevo diámetro y actualiza el radio"
        self.diametro = diametro
        self.radio = diametro / 2

    def calcular_area(self):
        "Calcula y devuelve el área del círculo"
        return math.pi * (self.radio ** 2)

    def calcular_circunferencia(self):
        "Calcula y devuelve la circunferencia del círculo"
        return 2 * math.pi * self.radio



if __name__ == "__main__":
   
    circulo1 = Circulo(5)

    
    print(f"Radio: {circulo1.obtener_radio()} unidades")
    print(f"Diámetro: {circulo1.obtener_diametro()} unidades")

    
    print(f"Área: {circulo1.calcular_area():.2f} unidades cuadradas")
    print(f"Circunferencia: {circulo1.calcular_circunferencia():.2f} unidades")

   
    circulo1.establecer_radio(7)
    print("\nDespués de actualizar el radio:")
    print(f"Radio: {circulo1.obtener_radio()} unidades")
    print(f"Diámetro: {circulo1.obtener_diametro()} unidades")
    print(f"Área: {circulo1.calcular_area():.2f} unidades cuadradas")
    print(f"Circunferencia: {circulo1.calcular_circunferencia():.2f} unidades")

   
    circulo1.establecer_diametro(20)
    print("\nDespués de actualizar el diámetro:")
    print(f"Radio: {circulo1.obtener_radio()} unidades")
    print(f"Diámetro: {circulo1.obtener_diametro()} unidades")
    print(f"Área: {circulo1.calcular_area():.2f} unidades cuadradas")
    print(f"Circunferencia: {circulo1.calcular_circunferencia():.2f} unidades")
