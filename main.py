""" El objetivo consiste en desarrollar un programa que permita llevar un registro de
películas aplicando conceptos de programación orientada a objetos.
El funcionamiento esperado es el siguiente:
• Al ejecutar el programa se solicita ingresar el nombre del catálogo de películas:
• Si el catálogo de películas no existe se creará uno nuevo. Este catálogo se va a
guardar en un archivo txt donde posteriormente se guardarán las películas. Si el
catálogo existe se podrá seguir modificando el archivo.
• Se debe mostrar un menú de opciones, que permita realizar las siguientes
operaciones:
1. Agregar Película
2. Modificar Pelicula
3. Listar Películas
4. Buscar Pelicula          
5. Eliminar Pelicula    
6. Eliminar Catálogo Películas
7. Salir
"""

import os
import sys

class MovieCatalog:
    def __init__(self, name):
        self.__name = name
        self.__path_file = f"movies/{name}.txt"
        self.movies = []

        def add_movies(self, movie):
            self.movies.append(movie)
            with open(self.__path_file, 'a') as file:
                file.write(f"{movie}\n")
                print(f"Pelicula {movie} agregada correctamente") 
        
        def list(self):
            with open(self.__path_file, 'r') as file:
                movies = file.readlines()
                for movie in movies:
                    print(movie.strip())


        def search(self, movie_name):
            for movie in self.movies:
                if movie.name == movie_name:
                    return movie
                else:
                    print(f"Pelicula {movie_name} no encontrada")

        def modify_movie(self, movie_name):
        for i, movie in enumerate(self.movies):
            if movie_name.lower() in movie.lower():
                print(f"Película encontrada: {movie}")
                new_name = input("Ingrese el nuevo nombre: ")
                self.movies[i] = self.movies[i].replace(movie.split(" | ")[0], new_name)
                self.__save_to_file()
                print(f"Película modificada correctamente.")
                return
        print(f"Película '{movie_name}' no encontrada.")

        def delete_movie(self, movie_name):
        for movie in self.movies:
            if movie_name.lower() in movie.lower():
                self.movies.remove(movie)
                self.__save_to_file()
                print(f"Película '{movie_name}' eliminada correctamente.")
                return
        print(f"Película '{movie_name}' no encontrada.")

        def delete(self):
            if os.path.exists(self.__path_file):
                os.remove(self.__path_file)
                print(f"Catálogo {self.__name} de películas eliminado correctamente")
            else:
                print(f"Catálogo {self.__name} de películas no encontrado")

        def exit(self):
            print("Saliendo del programa, gracias, hasta luego!")
            sys.exit(0)


     

class Movie(MovieCatalog):
    def __init__(self, movie_name, cast, description, director, duration, genre, year):
        super().__init__(movie_name)
        self.__description = description
        self.__director = director
        self.__cast = cast
        self.__duration = duration
        self.genre = genre
        self.__year = year

     def __str__(self):   
        return f"{self.__movie_name} - {self.__cast} - {self.__description} - {self.__director} - {self.__duration} minutos - {self.genre} - {self.__year}"


# ------------------------------
#       FUNCION MAIN
# ------------------------------

def main():
    name_catalog = input("Ingrese el nombre del catálogo de películas: ")

    catalog = MovieCatalog(name_catalog)

    if os.path.exists(f"movies/{name_catalog}.txt"):
        with open(f"{name_catalog}.txt", "r") as file:
        print(f"Catálogo '{name_catalog}' cargado exitosamente. Se abrirá para modificarlo.")
    else:
        with open (f"{name_catalog}.txt", 'w') as file:
        print(f"Catálogo '{name_catalog}' creado exitosamente.")

    while True:
        print("\n---MENÚ ---") 
        print("1. Agregar Película")
        print("2. Modificar Película")
        print("3. Listar Películas")
        print("4. Buscar Película")
        print("5. Eliminar Película")
        print("6. Eliminar Catálogo")
        print("7. Salir")

        option = input("Seleccione una opción: ").strip()

        if option == "1":
            name = input("Nombre: ")
            cast = input("Elenco: ")
            description = input("Descripción: ")
            director = input("Director/a: ")
            duration = input("Duracion (min): ")
            genre = input("Genero: ")
            year = input("Año: ")
            movie = Movie(name, cast, description, director, duration, genre, year)
            catalog,add_movie(movie)
        
        elif option == "2":
            name = input ("Ingrese el nombre de la pelicula a modificar: ")
            catalog.modify_movie(name)

        elif option == "3":
            catalog.list_movies()

        elif option == "4":
            name = input("Ingrese el nombre de la pelicula a eliminar: ")
            catalog.delete_movie(name)

        elif option == "6":
            confirm = input("¿Está seguro que desea eliminar el catalogo (S/N):  ")
            if confirm == "S"
            catalog.delete_catalog()
            break    

        elif option == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            sys.exit(0)
   
   if __name__ == "__main__":
        main()