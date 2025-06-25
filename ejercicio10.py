class Libro:
    def __init__(self, titulo, autor, genero, num_paginas):
        "Inicializa las propiedades del libro"
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.num_paginas = num_paginas

    def obtener_titulo(self):
        "Devuelve el título del libro"
        return self.titulo

    def establecer_titulo(self, titulo):
        "Establece un nuevo título para el libro"
        self.titulo = titulo

    def obtener_autor(self):
        "Devuelve el autor del libro"
        return self.autor

    def establecer_autor(self, autor):
        "Establece un nuevo autor para el libro"
        self.autor = autor

    def obtener_genero(self):
        "Devuelve el género del libro"
        return self.genero

    def establecer_genero(self, genero):
        "Establece un nuevo género para el libro"
        self.genero = genero

    def obtener_num_paginas(self):
        "Devuelve el número de páginas del libro"
        return self.num_paginas

    def establecer_num_paginas(self, num_paginas):
        "Establece un nuevo número de páginas para el libro"
        self.num_paginas = num_paginas

    def es_ficcion(self):
        
        generos_ficcion = [
            "ciencia ficción",
            "fantasía",
            "terror",
            "novela",
            "ficción histórica",
            "ficción",
            "aventura"
        ]
        return self.genero.lower() in generos_ficcion



if __name__ == "__main__":
    libro1 = Libro("1984", "George Orwell", "Ciencia ficción", 328)

   
    print(f"Título: {libro1.obtener_titulo()}")
    print(f"Autor: {libro1.obtener_autor()}")
    print(f"Género: {libro1.obtener_genero()}")
    print(f"Número de páginas: {libro1.obtener_num_paginas()}")

    
    if libro1.es_ficcion():
        print("El libro es de ficción.")
    else:
        print("El libro no es de ficción.")

    
    libro1.establecer_genero("Ensayo")
    libro1.establecer_num_paginas(400)

    print("\nDespués de actualizar:")
    print(f"Género: {libro1.obtener_genero()}")
    print(f"Número de páginas: {libro1.obtener_num_paginas()}")

    
    if libro1.es_ficcion():
        print("El libro es de ficción.")
    else:
        print("El libro no es de ficción.")
