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

class MovieCatalog:
    def __init__(self, name):
        self.__name = name
        self.__path_file = f"movies/{name}.txt"
        self.movies = []

        def add_movies(self, movie):
            self.movies.append(movie)
            with opne(self.__path_file, 'a') as file:
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


        def modify(self, movie_name):
        for movie in self.movies:
            if movie.name == movie_name:
            new_name = input ("Ingrese el nuevo nombre de la pelicula: ")
            movie.name = new_name
            print (f"Pelicula (movie_name) modificada correctamente")
            break
            else:
                print(f"Pelicula {movie_name} no encontrada")
            return movie

        def deleteMovie(self, movie_name):
            for movie in self.movies:
                if movie.name ==movie_name:
                    self.movies.remove(movie)
                    print(f"Pelicual{movie_name} ha sido eliminada correctamente")
                    break
                else:
                print(f"Pelicula {movie_name} no encontrada")
                

        def delete(self)
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

     def__str__(self):   
        return f"{self.__movie_name} - {self.__cast} - {self.__description} - {self.__director} - {self.__duration} minutos - {self.genre} - {self.__year}"