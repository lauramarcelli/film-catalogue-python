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

from back import control, select_catalog
from models import Movie, MovieCatalog
import os
import sys


# ------------------------------
#       FUNCION MAIN
# ------------------------------

def main():
    print("\n" + "=" * 60)
    print("   Bienvenida al Gestor de Catálogos de Películas")
    print("=" * 60)

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar Catálogo")
        print("2. Agregar Película")
        print("3. Modificar Película")
        print("4. Listar Películas")
        print("5. Buscar Película")
        print("6. Eliminar Película")
        print("7. Eliminar Catálogo")
        print("8. Salir")

        option = input("Seleccione una opción: ").strip()

        if option == "1":
            new_catalog_name = input("Ingrese el nombre del nuevo catálogo: ").strip()
            if os.path.exists(f"{new_catalog_name}.txt"):
                print(f"El catálogo '{new_catalog_name}' ya existe.")
            else:
                open(f"{new_catalog_name}.txt", "w").close()
                print(f"Catálogo '{new_catalog_name}' creado exitosamente.")

        elif option == "2":
            catalog = select_catalog("agregar la película")
            if not catalog:
                continue
            control(catalog._MovieCatalog__name)
            name = input("Ingrese el nombre de la película: ")
            cast = input("Ingrese el elenco: ")
            description = input("Ingrese descripción de la película: ")
            director = input("Ingrese el Director/a: ")
            duration = input("Ingrese la duración (min): ")
            genre = input("Ingrese el género: ")
            year = input("Ingrese el año: ")
            movie = Movie(name, cast, description, director, duration, genre, year)
            catalog.add_movie(movie)

        elif option == "3":
            catalog = select_catalog("modificar la película")
            if not catalog:
                continue
            name = input("Ingrese el nombre de la película a modificar: ")
            catalog.modify_movie(name)

        elif option == "4":
            catalog = select_catalog("listar")
            if not catalog:
                continue
            catalog.list()

        elif option == "5":
            name = input("Ingrese el nombre de la película a buscar: ")
            all_catalogs = [f.replace(".txt", "") for f in os.listdir(".") if f.endswith(".txt")]
            found = False
            for cat_name in all_catalogs:
                catalog = MovieCatalog(cat_name)
                result = catalog.search(name)
                if result:
                    found = True
                    print(f"  → Encontrada en el catálogo: '{cat_name}'")
            if not found:
                print(f"Película '{name}' no encontrada en ningún catálogo.")

        elif option == "6":
            catalog = select_catalog("eliminar la película")
            if not catalog:
                continue
            name = input("Ingrese el nombre de la película a eliminar: ")
            catalog.delete_movie(name)

        elif option == "7":
            catalog = select_catalog("eliminar")
            if not catalog:
                continue
            confirm = input("¿Está seguro que desea eliminar este catálogo? (S/N): ").strip().upper()
            if confirm == "S":
                catalog.delete()

        elif option == "8":
            print("Saliendo del programa. ¡Hasta luego!")
            sys.exit(0)

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()