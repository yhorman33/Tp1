class Empleado:
    def __init__(self, nombre, edad, salario, cargo):
        "Inicializa las propiedades del empleado"
        self.nombre = nombre
        self.edad = edad
        self.salario = salario  
        self.cargo = cargo

    def obtener_nombre(self):
        "Devuelve el nombre del empleado"
        return self.nombre

    def establecer_nombre(self, nombre):
        "Establece un nuevo nombre para el empleado"
        self.nombre = nombre

    def obtener_edad(self):
        "Devuelve la edad del empleado"
        return self.edad

    def establecer_edad(self, edad):
        "Establece una nueva edad para el empleado"
        self.edad = edad

    def obtener_salario(self):
        "Devuelve el salario mensual del empleado"
        return self.salario

    def establecer_salario(self, salario):
        "Establece un nuevo salario mensual para el empleado"
        self.salario = salario

    def obtener_cargo(self):
        "Devuelve el cargo del empleado"
        return self.cargo

    def establecer_cargo(self, cargo):
        "Establece un nuevo cargo para el empleado"
        self.cargo = cargo

    def calcular_salario_anual(self):
        "Calcula y devuelve el salario anual"
        return self.salario * 12



if __name__ == "__main__":
    empleado1 = Empleado("Lucía", 28, 3500, "Analista")

   
    print(f"Nombre: {empleado1.obtener_nombre()}")
    print(f"Edad: {empleado1.obtener_edad()}")
    print(f"Salario mensual: ${empleado1.obtener_salario():.2f}")
    print(f"Cargo: {empleado1.obtener_cargo()}")
    print(f"Salario anual: ${empleado1.calcular_salario_anual():.2f}")

    
    empleado1.establecer_nombre("Lucía Gómez")
    empleado1.establecer_edad(29)
    empleado1.establecer_salario(4000)
    empleado1.establecer_cargo("Senior Analyst")

    print("\nDespués de actualizar:")
    print(f"Nombre: {empleado1.obtener_nombre()}")
    print(f"Edad: {empleado1.obtener_edad()}")
    print(f"Salario mensual: ${empleado1.obtener_salario():.2f}")
    print(f"Cargo: {empleado1.obtener_cargo()}")
    print(f"Salario anual: ${empleado1.calcular_salario_anual():.2f}")
