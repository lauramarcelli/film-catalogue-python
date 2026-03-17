import os

def control(catalog):
    if os.path.exists(f"{catalog}.txt"):
        with open(f"{catalogo}.txt", 'r') as archivo:
            print(f"El catalogo '{catalogo}' ya existe.")
    else:
        print("El catalogo no existe.")
    return catalog            