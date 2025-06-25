class Tienda:
    def __init__(self, nombre):
        "Inicializa el nombre de la tienda y la lista de productos"
        self.nombre = nombre
        self.productos = [] 

    def obtener_nombre(self):
        "Devuelve el nombre de la tienda"
        return self.nombre

    def establecer_nombre(self, nombre):
        "Establece un nuevo nombre para la tienda"
        self.nombre = nombre

    def agregar_producto(self, producto):
        " Agrega un producto a la lista El producto puede ser un objeto o simplemente un string con su nombre"
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        "Elimina un producto de la lista si existe"
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print("El producto no está en la lista.")

    def obtener_productos(self):
        "Devuelve la lista completa de productos disponibles"
        return self.productos



if __name__ == "__main__":
    tienda1 = Tienda("La Tiendita")

    
    print(f"Tienda: {tienda1.obtener_nombre()}")

    
    tienda1.agregar_producto("Manzanas")
    tienda1.agregar_producto("Pan")
    tienda1.agregar_producto("Leche")

    
    print("Productos disponibles:", tienda1.obtener_productos())

    
    tienda1.eliminar_producto("Pan")
    print("Después de eliminar 'Pan':", tienda1.obtener_productos())

    
    tienda1.eliminar_producto("Galletas")  

    
    tienda1.establecer_nombre("Supermercado Central")
    print("Nuevo nombre de la tienda:", tienda1.obtener_nombre())
