class Rectangulo:
    def __init__(self, longitud, anchura):
        "Inicializa las propiedades del rectángulo"
        self.longitud = longitud  
        self.anchura = anchura    

    def obtener_longitud(self):
        "Devuelve la longitud del rectángulo."
        return self.longitud

    def establecer_longitud(self, longitud):
        "Establece una nueva longitud para el rectángulo"
        self.longitud = longitud

    def obtener_anchura(self):
        "Devuelve la anchura del rectángulo"
        return self.anchura

    def establecer_anchura(self, anchura):
        "Establece una nueva anchura para el rectángulo"
        self.anchura = anchura

    def calcular_area(self):
        "Calcula y devuelve el área del rectángulo"
        return self.longitud * self.anchura

    def calcular_perimetro(self):
        "Calcula y devuelve el perímetro del rectángulo"
        return 2 * (self.longitud + self.anchura)



if __name__ == "__main__":
    
    rectangulo1 = Rectangulo(5, 3)

   
    print(f"Longitud: {rectangulo1.obtener_longitud()} unidades")
    print(f"Anchura: {rectangulo1.obtener_anchura()} unidades")

    
    print(f"Área: {rectangulo1.calcular_area()} unidades cuadradas")
    print(f"Perímetro: {rectangulo1.calcular_perimetro()} unidades")

    
    rectangulo1.establecer_longitud(10)
    rectangulo1.establecer_anchura(4)

    
    print("\nDespués de actualizar:")
    print(f"Longitud: {rectangulo1.obtener_longitud()} unidades")
    print(f"Anchura: {rectangulo1.obtener_anchura()} unidades")
    print(f"Área: {rectangulo1.calcular_area()} unidades cuadradas")
    print(f"Perímetro: {rectangulo1.calcular_perimetro()} unidades")
