class Producto:
    def __init__(self, nombre, precio, stock):
        "Inicializa las propiedades del producto"
        self.nombre = nombre    
        self.precio = precio   
        self.stock = stock     

    def obtener_nombre(self):
        "Devuelve el nombre del producto"
        return self.nombre

    def establecer_nombre(self, nombre):
        "Establece un nuevo nombre para el producto"
        self.nombre = nombre

    def obtener_precio(self):
        "Devuelve el precio del producto"
        return self.precio

    def establecer_precio(self, precio):
        "Establece un nuevo precio para el producto"
        self.precio = precio

    def obtener_stock(self):
        "Devuelve el stock disponible del producto"
        return self.stock

    def establecer_stock(self, stock):
        "Establece un nuevo stock para el producto."
        self.stock = stock

    def aumentar_stock(self, cantidad):
        "Aumenta el stock del producto en la cantidad indicada"
        self.stock += cantidad

    def disminuir_stock(self, cantidad):
        "Disminuye el stock del producto si hay suficiente cantidad disponible"
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("No hay suficiente stock disponible para realizar esta operación.")



if __name__ == "__main__":
   
    producto1 = Producto("Lápiz", 0.50, 100)

  
    print(f"Nombre: {producto1.obtener_nombre()}")
    print(f"Precio: ${producto1.obtener_precio():.2f}")
    print(f"Stock disponible: {producto1.obtener_stock()} unidades")

  
    producto1.aumentar_stock(20)
    producto1.disminuir_stock(50)

   
    print("\nDespués de actualizar el stock:")
    print(f"Stock disponible: {producto1.obtener_stock()} unidades")

    #
    producto1.disminuir_stock(100) 
