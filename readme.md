# 🎬 Gestor de Catálogos de Películas

Programa de consola desarrollado en Python que permite crear y gestionar catálogos de películas, aplicando conceptos de Programación Orientada a Objetos.

---

## 📋 Descripción

Este proyecto permite al usuario crear múltiples catálogos de películas, agregar películas con sus datos completos, modificarlas, buscarlas, listarlas y eliminarlas. Cada catálogo se guarda como un archivo `.txt` en el directorio del proyecto.

---

## 🗂️ Estructura del proyecto

```
python-film-catalog/
├── main.py       → Menú principal y lógica de navegación
├── models.py     → Clases Movie y MovieCatalog
├── back.py       → Funciones auxiliares (control, select_catalog)
└── README.md
```

### Descripción de cada archivo

- **`models.py`** — Contiene las clases principales:
  - `MovieCatalog`: maneja la creación, lectura y escritura del archivo `.txt`, y todas las operaciones sobre las películas.
  - `Movie`: representa una película con sus atributos y define cómo se guarda en el archivo.

- **`back.py`** — Contiene funciones de soporte:
  - `control()`: verifica si un catálogo existe e informa al usuario.
  - `select_catalog()`: solicita el nombre del catálogo, valida que exista y lo retorna cargado.

- **`main.py`** — Punto de entrada del programa. Muestra el menú y llama a las funciones y métodos correspondientes según la opción elegida.

---

## ⚙️ Requisitos

- Python 3.x
- No requiere librerías externas

---

## 🚀 Instalación y ejecución

1. Cloná o descargá el repositorio:

```bash
git clone https://github.com/lauramarcelli/film-catalogue-python.git
cd film-catalogue-python
```

2. Ejecutá el programa:

```bash
python main.py
```

---

## 📌 Uso

Al ejecutar el programa se muestra el menú principal:

```
============================================================
   Bienvenido al Gestor de Catálogos de Películas
============================================================

--- MENÚ ---
1. Agregar Catálogo
2. Agregar Película
3. Modificar Película
4. Listar Películas
5. Buscar Película
6. Eliminar Película
7. Eliminar Catálogo
8. Salir
```

### Opciones del menú

| Opción | Descripción |
|--------|-------------|
| 1 | Crea un nuevo catálogo (archivo `.txt`) en el proyecto |
| 2 | Agrega una película a un catálogo existente |
| 3 | Modifica un atributo específico de una película |
| 4 | Lista todas las películas de un catálogo |
| 5 | Busca una película por nombre |
| 6 | Elimina una película de un catálogo |
| 7 | Elimina un catálogo completo |
| 8 | Sale del programa |

---

## 🎥 Atributos de una película

Cada película almacena los siguientes datos:

| Atributo | Descripción |
|----------|-------------|
| Nombre | Título de la película |
| Elenco | Actores principales |
| Descripción | Sinopsis breve |
| Director | Nombre del director/a |
| Duración | Duración en minutos |
| Género | Género cinematográfico |
| Año | Año de estreno |

---

## 💾 Formato de almacenamiento

Las películas se guardan en el archivo `.txt` del catálogo con el siguiente formato:

```
Matrix | Keanu Reeves | Hacker descubre la verdad | Wachowski | 136 min | Ciencia ficción | 1999
John Wick | Keanu Reeves | Ex asesino busca venganza | Chad Stahelski | 101 min | Acción | 2014
```

---

## 👩‍💻 Ejemplo de uso

```
Seleccione una opción: 1
Ingrese el nombre del nuevo catálogo: Accion
Catálogo 'Accion' creado exitosamente.

Seleccione una opción: 2
Ingrese el nombre del catálogo donde desea agregar la película: Accion
Ingrese el nombre de la película: Matrix
Ingrese el elenco: Keanu Reeves
Ingrese descripción de la película: Hacker descubre la verdad sobre su realidad
Ingrese el Director/a: Wachowski
Ingrese la duración (min): 136
Ingrese el género: Ciencia ficción
Ingrese el año: 1999
Película 'Matrix | Keanu Reeves | ...' agregada correctamente.

Seleccione una opción: 4
Ingrese el nombre del catálogo que desea listar: Accion

============================================================
  CATÁLOGO: ACCION
============================================================

  #1
  Título:      Matrix
  Elenco:      Keanu Reeves
  Descripción: Hacker descubre la verdad sobre su realidad
  Director:    Wachowski
  Duración:    136 min
  Género:      Ciencia ficción
  Año:         1999
  ----------------------------------------------------------

  Total: 1 película/s
============================================================
```

---

## 🛠️ Conceptos aplicados

- Programación Orientada a Objetos (POO)
- Clases y métodos
- Atributos privados con name mangling (`__atributo`)
- Properties (`@property`)
- Manejo de archivos `.txt` (lectura, escritura, eliminación)
- Modularización en múltiples archivos
- Manejo de flujo con `continue` y `return`

---

## ✍️ Autora: Laura Marcelli

Desarrollado como proyecto práctico del curso de Python — ADA ITW.