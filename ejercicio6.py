class Estudiante:
    def __init__(self, nombre, edad, carrera):
        "Inicializa las propiedades del estudiante"
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []  

    def obtener_nombre(self):
        "Devuelve el nombre del estudiante"
        return self.nombre

    def establecer_nombre(self, nombre):
        "Establece un nuevo nombre para el estudiante"
        self.nombre = nombre

    def obtener_edad(self):
        "Devuelve la edad del estudiante"
        return self.edad

    def establecer_edad(self, edad):
        "Establece una nueva edad para el estudiante"
        self.edad = edad

    def obtener_carrera(self):
        "Devuelve la carrera del estudiante"
        return self.carrera

    def establecer_carrera(self, carrera):
        "Establece una nueva carrera para el estudiante"
        self.carrera = carrera

    def agregar_nota(self, nota):
        "Agrega una nota a la lista de exámenes"
        self.notas.append(nota)

    def calcular_nota_media(self):
        "Calcula y devuelve la nota media de los exámenes"
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)



if __name__ == "__main__":
    
    estudiante1 = Estudiante("Ana", 20, "Ingeniería")

   
    print(f"Nombre: {estudiante1.obtener_nombre()}")
    print(f"Edad: {estudiante1.obtener_edad()}")
    print(f"Carrera: {estudiante1.obtener_carrera()}")

    estudiante1.agregar_nota(8)
    estudiante1.agregar_nota(7.5)
    estudiante1.agregar_nota(9)

    
    print(f"Nota media: {estudiante1.calcular_nota_media():.2f}")

    estudiante1.establecer_nombre("Ana María")
    estudiante1.establecer_edad(21)
    estudiante1.establecer_carrera("Matemáticas")

    
    print("\nDespués de actualizar:")
    print(f"Nombre: {estudiante1.obtener_nombre()}")
    print(f"Edad: {estudiante1.obtener_edad()}")
    print(f"Carrera: {estudiante1.obtener_carrera()}")
