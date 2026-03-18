# 🎬 Gestor de Catálogos de Películas

Programa desarrollado en Python que permite crear y gestionar catálogos de películas, con interfaz gráfica construida con CustomTkinter.

---

## 📋 Descripción

Este proyecto permite al usuario crear múltiples catálogos de películas, agregar películas con sus datos completos, modificarlas, buscarlas, listarlas y eliminarlas. Cada catálogo se guarda como un archivo `.txt` en el directorio del proyecto.

---

## 🗂️ Estructura del proyecto

```
python-film-catalog/
├── app.py        → Interfaz gráfica (CustomTkinter)
├── main.py       → Versión de consola
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

- **`app.py`** — Interfaz gráfica con CustomTkinter. Muestra el menú con botones y cada pantalla se construye con funciones simples.

- **`main.py`** — Versión de consola del programa. Muestra el menú en terminal y llama a las funciones correspondientes.

---

## ⚙️ Requisitos

- Python 3.x
- CustomTkinter

```bash
pip install customtkinter
```

---

## 🚀 Instalación y ejecución

1. Cloná o descargá el repositorio:

```bash
git clone https://github.com/lauramarcelli/film-catalogue-python.git
cd film-catalogue-python
```

2. Instalá la dependencia:

```bash
pip install customtkinter
```

3. Ejecutá el programa con interfaz gráfica:

```bash
python app.py
```

O en versión consola:

```bash
python main.py
```

---

## 📌 Uso

Al ejecutar `app.py` se abre una ventana con el menú principal:

```
🎬 Gestor de Películas
¿Qué querés hacer hoy?

➕ Agregar Catálogo
🎬 Agregar Película
✏️ Modificar Película
📋 Listar Películas
🔍 Buscar Película
🗑️ Eliminar Película
❌ Eliminar Catálogo
```

Cada opción abre una pantalla con los campos necesarios y un botón **← Volver al menú** para navegar hacia atrás.

### Opciones del menú

| Opción | Descripción |
|--------|-------------|
| ➕ Agregar Catálogo | Crea un nuevo catálogo (archivo `.txt`) en el proyecto |
| 🎬 Agregar Película | Agrega una película a un catálogo existente |
| ✏️ Modificar Película | Modifica un atributo específico de una película |
| 📋 Listar Películas | Lista todas las películas de un catálogo |
| 🔍 Buscar Película | Busca por nombre en **todos los catálogos** automáticamente |
| 🗑️ Eliminar Película | Elimina una película de un catálogo |
| ❌ Eliminar Catálogo | Elimina un catálogo completo |

---

## 🎥 Atributos de una película

Cada película almacena los siguientes datos:

| Atributo | Descripción |
|----------|-------------|
| Título | Nombre de la película |
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
➕ Agregar Catálogo
  Nombre del catálogo: Accion
  ✅ Catálogo 'Accion' creado exitosamente.

🎬 Agregar Película
  Nombre del catálogo: Accion
  Título: Matrix
  Elenco: Keanu Reeves
  Descripción: Hacker descubre la verdad sobre su realidad
  Director/a: Wachowski
  Duración (min): 136
  Género: Ciencia ficción
  Año: 1999
  ✅ Película 'Matrix' agregada correctamente.

🔍 Buscar Película
  Nombre de la película: Matrix
  ✅ Matrix — catálogo: Accion
     🎭 Elenco:      Keanu Reeves
     📝 Descripción: Hacker descubre la verdad sobre su realidad
     🎬 Director:    Wachowski
     ⏱️ Duración:    136 min
     🎞️ Género:      Ciencia ficción
     📅 Año:         1999
```

---

## 🛠️ Conceptos aplicados

- Programación Orientada a Objetos (POO)
- Clases y métodos
- Atributos privados con name mangling (`__atributo`)
- Properties (`@property`)
- Manejo de archivos `.txt` (lectura, escritura, eliminación)
- Modularización en múltiples archivos
- Interfaz gráfica con CustomTkinter
- Funciones como ciudadanos de primera clase (callbacks en botones)

---

## ✍️ Autora Laura Marcelli

Desarrollado como proyecto práctico del curso de Python — ADA ITW.
