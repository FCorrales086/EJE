#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejemplo de relaciones entre clases: Biblioteca, Libro y Autor

class Autor:
    """
    Clase que representa a un autor de libros.
    """
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []  # Lista de libros escritos por este autor
    
    def escribir_libro(self, titulo, anio):
        """Crea un nuevo libro escrito por este autor"""
        nuevo_libro = Libro(titulo, self, anio)
        self.libros.append(nuevo_libro)
        return nuevo_libro
    
    def mostrar_info(self):
        """Muestra información del autor"""
        print(f"Autor: {self.nombre} ({self.nacionalidad})")
        print(f"Ha escrito {len(self.libros)} libros:")
        for libro in self.libros:
            print(f"  - {libro.titulo} ({libro.anio})")


class Libro:
    """
    Clase que representa un libro.
    Esta clase tiene una relación con la clase Autor.
    """
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor  # Relación: un libro tiene un autor
        self.anio = anio
        self.prestado = False
    
    def mostrar_info(self):
        """Muestra la información del libro"""
        estado = "Prestado" if self.prestado else "Disponible"
        print(f"Libro: {self.titulo}")
        print(f"Autor: {self.autor.nombre}")
        print(f"Año: {self.anio}")
        print(f"Estado: {estado}")
    
    def prestar(self):
        """Presta el libro si está disponible"""
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
    def devolver(self):
        """Devuelve el libro a la biblioteca"""
        if self.prestado:
            self.prestado = False
            return True
        return False


class Biblioteca:
    """
    Clase que representa una biblioteca.
    Esta clase tiene una relación con la clase Libro.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []  # Lista de libros en la biblioteca
    
    def agregar_libro(self, libro):
        """Agrega un libro al catálogo de la biblioteca"""
        self.catalogo.append(libro)
    
    def buscar_por_titulo(self, titulo):
        """Busca libros por título"""
        return [libro for libro in self.catalogo if titulo.lower() in libro.titulo.lower()]
    
    def buscar_por_autor(self, nombre_autor):
        """Busca libros por nombre de autor"""
        return [libro for libro in self.catalogo if nombre_autor.lower() in libro.autor.nombre.lower()]
    
    def mostrar_catalogo(self):
        """Muestra el catálogo completo de la biblioteca"""
        print(f"Catálogo de la biblioteca {self.nombre}:")
        print(f"Total de libros: {len(self.catalogo)}")
        for libro in self.catalogo:
            print(f"- {libro.titulo} de {libro.autor.nombre} ({libro.anio})")


# Ejemplo de uso
if __name__ == "__main__":
    # Creamos algunos autores
    autor1 = Autor("Gabriel García Márquez", "Colombiano")
    autor2 = Autor("Isabel Allende", "Chilena")
    
    # Los autores escriben libros
    libro1 = autor1.escribir_libro("Cien años de soledad", 1967)
    libro2 = autor1.escribir_libro("El amor en los tiempos del cólera", 1985)
    libro3 = autor2.escribir_libro("La casa de los espíritus", 1982)
    
    # Creamos una biblioteca
    biblioteca = Biblioteca("Biblioteca Municipal")
    
    # Agregamos los libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    
    # Mostramos información
    print("\n" + "=" * 50)
    biblioteca.mostrar_catalogo()
    
    print("\n" + "=" * 50)
    autor1.mostrar_info()
    
    print("\n" + "=" * 50)
    libro1.mostrar_info()
    
    # Prestamos un libro
    print("\n" + "=" * 50)
    print(f"Intentando prestar '{libro1.titulo}'...")
    if libro1.prestar():
        print("¡Libro prestado con éxito!")
    else:
        print("El libro ya está prestado.")
    
    # Mostramos el estado actualizado
    print("\n" + "=" * 50)
    libro1.mostrar_info()
    
    # Buscamos libros
    print("\n" + "=" * 50)
    print("Búsqueda por título 'amor':")
    for libro in biblioteca.buscar_por_titulo("amor"):
        print(f"- {libro.titulo} de {libro.autor.nombre}")
        print(f"- {libro.titulo} de {libro.autor.nombre}")


