import os


class MovieCatalog:
    def __init__(self, name):
        self.__name = name
        self.__path_file = f"{name}.txt"
        self.movies = []

        if os.path.exists(self.__path_file):
            with open(self.__path_file, "r", encoding="utf-8") as file:
                for line in file:
                    stripped = line.strip()
                    if stripped:
                        self.movies.append(stripped)

    def add_movie(self, movie):
        self.movies.append(str(movie))
        with open(self.__path_file, "a", encoding="utf-8") as file:
            file.write(f"{movie}\n")
        print(f"Película '{movie}' agregada correctamente.")

    def list(self):
        if not self.movies:
            print("El catálogo está vacío.")
            return
    
        print("\n" + "=" * 60)
        print(f"  CATÁLOGO: {self.__name.upper()}")
        print("=" * 60)
    
        for i, movie in enumerate(self.movies, 1):
            parts = movie.split(" | ")
            print(f"\n  #{i}")
            print(f"  Título:      {parts[0]}")
            print(f"  Elenco:      {parts[1]}")
            print(f"  Descripción: {parts[2]}")
            print(f"  Director:    {parts[3]}")
            print(f"  Duración:    {parts[4]}")
            print(f"  Género:      {parts[5]}")
            print(f"  Año:         {parts[6]}")
            print("  " + "-" * 58)
    
        print(f"\n  Total: {len(self.movies)} película/s")
        print("=" * 60)

    def search(self, movie_name):
        for movie in self.movies:
            if movie_name.lower() in movie.lower():
                print(f"Encontrada: {movie}")
                return movie
        print(f"Película '{movie_name}' no encontrada.")
        return None

    def modify_movie(self, movie_name):
        for i, movie in enumerate(self.movies):
            if movie_name.lower() in movie.lower():
                print(f"\nPelícula encontrada: {movie}")
                parts = movie.split(" | ")

                print("\n¿Qué atributo desea modificar?")
                print("1. Nombre")
                print("2. Elenco")
                print("3. Descripción")
                print("4. Director")
                print("5. Duración")
                print("6. Género")
                print("7. Año")

                attr_option = input("Seleccione una opción: ").strip()

                if attr_option == "1":
                    parts[0] = input("Ingrese el nuevo nombre: ")
                elif attr_option == "2":
                    parts[1] = input("Ingrese el nuevo elenco: ")
                elif attr_option == "3":
                    parts[2] = input("Ingrese la nueva descripción: ")
                elif attr_option == "4":
                    parts[3] = input("Ingrese el nuevo director: ")
                elif attr_option == "5":
                    parts[4] = input("Ingrese la nueva duración (min): ")
                elif attr_option == "6":
                    parts[5] = input("Ingrese el nuevo género: ")
                elif attr_option == "7":
                    parts[6] = input("Ingrese el nuevo año: ")
                else:
                    print("Opción inválida.")
                    return

                self.movies[i] = " | ".join(parts)
                self.__save_to_file()
                print("Película modificada correctamente.")
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
            print(f"Catálogo '{self.__name}' eliminado correctamente.")
        else:
            print(f"Catálogo '{self.__name}' no encontrado.")

    def __save_to_file(self):
        with open(self.__path_file, "w", encoding="utf-8") as file:
            for movie in self.movies:
                file.write(f"{movie}\n")


class Movie:
    def __init__(self, movie_name, cast, description, director, duration, genre, year):
        self.__movie_name = movie_name
        self.__cast = cast
        self.__description = description
        self.__director = director
        self.__duration = duration
        self.genre = genre
        self.__year = year

    @property
    def name(self):
        return self.__movie_name

    def __str__(self):
        return (f"{self.__movie_name} | {self.__cast} | {self.__description} | "
                f"{self.__director} | {self.__duration} min | {self.genre} | {self.__year}")