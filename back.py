import os
from models import MovieCatalog


def control(catalog):
    if os.path.exists(f"{catalog}.txt"):
        print(f"El catálogo '{catalog}' se abrirá para modificarlo.")
    else:
        print("El catálogo no existe.")
    return catalog


def select_catalog(action):
    catalog_name = input(f"Ingrese el nombre del catálogo donde desea {action}: ").strip()
    if not os.path.exists(f"{catalog_name}.txt"):
        print(f"El catálogo '{catalog_name}' no existe. Cree uno primero.")
        return None
    return MovieCatalog(catalog_name)