import customtkinter as ctk
import os
from models import MovieCatalog, Movie


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("🎬 Gestor de Catálogos de Películas")
window.geometry("700x600")

main_frame = ctk.CTkScrollableFrame(window, fg_color="transparent")
main_frame.pack(fill="both", expand=True, padx=24, pady=24)



def clear():
    for widget in main_frame.winfo_children():
        widget.destroy()

def show_message(text, color="#2e7d32"):
    ctk.CTkLabel(main_frame, text=text, text_color=color).pack(pady=4)

def back_button():
    ctk.CTkButton(
        main_frame, text="← Volver al menú",
        command=show_menu,
        fg_color="transparent", text_color="#1565c0",
        hover_color="#e3f2fd", width=160
    ).pack(anchor="w", pady=(0, 12))

def show_title(text):
    ctk.CTkLabel(
        main_frame, text=text,
        font=ctk.CTkFont(size=22, weight="bold"),
        text_color="#1a237e"
    ).pack(anchor="w", pady=(0, 12))

def create_field(label):
    ctk.CTkLabel(main_frame, text=label, anchor="w").pack(fill="x")
    field = ctk.CTkEntry(main_frame, width=400)
    field.pack(pady=(0, 8))
    return field



def show_menu():
    clear()

    ctk.CTkLabel(
        main_frame, text="🎬 Gestor de Películas",
        font=ctk.CTkFont(size=28, weight="bold"), text_color="#1a237e"
    ).pack(pady=(0, 4))

    ctk.CTkLabel(main_frame, text="¿Qué querés hacer hoy?", text_color="#555").pack(pady=(0, 16))

    buttons = [
        ("➕  Agregar Catálogo",   show_add_catalog,    "#1565c0"),
        ("🎬  Agregar Película",   show_add_movie,      "#1565c0"),
        ("✏️  Modificar Película", show_modify_movie,   "#1565c0"),
        ("📋  Listar Películas",   show_list_movies,    "#1565c0"),
        ("🔍  Buscar Película",    show_search_movie,   "#1565c0"),
        ("🗑️  Eliminar Película",  show_delete_movie,   "#c62828"),
        ("❌  Eliminar Catálogo",  show_delete_catalog, "#c62828"),
    ]

    for label, command, color in buttons:
        ctk.CTkButton(
            main_frame, text=label, command=command,
            fg_color=color, hover_color="#0d47a1" if color == "#1565c0" else "#b71c1c",
            width=300, height=40,
            font=ctk.CTkFont(size=14)
        ).pack(pady=5)



def show_add_catalog():
    clear()
    show_title("Agregar Catálogo")
    back_button()

    name_field = create_field("Nombre del catálogo:")

    def create():
        name = name_field.get().strip()
        if not name:
            show_message("⚠️ Ingresá un nombre.", "#c62828")
            return
        if os.path.exists(f"{name}.txt"):
            show_message(f"⚠️ El catálogo '{name}' ya existe.", "#c62828")
        else:
            open(f"{name}.txt", "w").close()
            show_message(f"✅ Catálogo '{name}' creado exitosamente.")
        name_field.delete(0, "end")

    ctk.CTkButton(main_frame, text="Crear", command=create, width=200).pack(pady=8)



def show_add_movie():
    clear()
    show_title("Agregar Película")
    back_button()

    catalog_field = create_field("Nombre del catálogo:")
    ctk.CTkFrame(main_frame, height=1, fg_color="#ccc").pack(fill="x", pady=8)
    title_field    = create_field("Título:")
    cast_field     = create_field("Elenco:")
    desc_field     = create_field("Descripción:")
    director_field = create_field("Director/a:")
    duration_field = create_field("Duración (min):")
    genre_field    = create_field("Género:")
    year_field     = create_field("Año:")

    def add():
        cat_name = catalog_field.get().strip()
        if not cat_name:
            show_message("⚠️ Ingresá el nombre del catálogo.", "#c62828")
            return
        if not os.path.exists(f"{cat_name}.txt"):
            show_message(f"⚠️ El catálogo '{cat_name}' no existe.", "#c62828")
            return
        if not title_field.get().strip():
            show_message("⚠️ El título es obligatorio.", "#c62828")
            return

        catalog = MovieCatalog(cat_name)
        movie = Movie(
            title_field.get().strip(), cast_field.get().strip(),
            desc_field.get().strip(), director_field.get().strip(),
            duration_field.get().strip(), genre_field.get().strip(), year_field.get().strip()
        )
        catalog.add_movie(movie)
        show_message(f"✅ Película '{title_field.get().strip()}' agregada correctamente.")
        for field in [title_field, cast_field, desc_field, director_field, duration_field, genre_field, year_field]:
            field.delete(0, "end")

    ctk.CTkButton(main_frame, text="Agregar", command=add, width=200).pack(pady=8)



def show_list_movies():
    clear()
    show_title("Listar Películas")
    back_button()

    catalog_field = create_field("Nombre del catálogo:")
    results_frame = ctk.CTkScrollableFrame(main_frame, height=300)
    results_frame.pack(fill="both", expand=True, pady=8)

    def list_movies():
        for widget in results_frame.winfo_children():
            widget.destroy()

        cat_name = catalog_field.get().strip()
        if not os.path.exists(f"{cat_name}.txt"):
            ctk.CTkLabel(results_frame, text=f"⚠️ El catálogo '{cat_name}' no existe.", text_color="#c62828").pack()
            return

        catalog = MovieCatalog(cat_name)
        if not catalog.movies:
            ctk.CTkLabel(results_frame, text="El catálogo está vacío.", text_color="#c62828").pack()
            return

        for i, movie in enumerate(catalog.movies, 1):
            parts = movie.split(" | ")
            card = ctk.CTkFrame(results_frame, fg_color="white", corner_radius=10)
            card.pack(fill="x", pady=6, padx=4)

            ctk.CTkLabel(card, text=f"#{i}  {parts[0]}",
                        font=ctk.CTkFont(size=15, weight="bold"),
                        text_color="#1a237e").pack(anchor="w", padx=12, pady=(10, 2))

            for detail in [
                f"🎭 Elenco:      {parts[1]}",
                f"📝 Descripción: {parts[2]}",
                f"🎬 Director:    {parts[3]}",
                f"⏱️ Duración:    {parts[4]}",
                f"🎞️ Género:      {parts[5]}",
                f"📅 Año:         {parts[6]}",
            ]:
                ctk.CTkLabel(card, text=detail, anchor="w").pack(anchor="w", padx=12)
            ctk.CTkLabel(card, text="").pack(pady=2)

    ctk.CTkButton(main_frame, text="Listar", command=list_movies, width=200).pack(pady=8)



def show_search_movie():
    clear()
    show_title("Buscar Película")
    back_button()

    movie_field = create_field("Nombre de la película:")  
    results_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    results_frame.pack(fill="x", pady=8)

    def search():
        for widget in results_frame.winfo_children():
            widget.destroy()

        movie_name = movie_field.get().strip()
        if not movie_name:
            ctk.CTkLabel(results_frame, text="⚠️ Ingresá el nombre de la película.", text_color="#c62828").pack()
            return

        
        all_catalogs = [f.replace(".txt", "") for f in os.listdir(".") if f.endswith(".txt")]
        found = False

        for cat_name in all_catalogs:
            catalog = MovieCatalog(cat_name)
            result = catalog.search(movie_name)
            if result:
                found = True
                parts = result.split(" | ")
                card = ctk.CTkFrame(results_frame, fg_color="white", corner_radius=10)
                card.pack(fill="x", pady=6, padx=4)
                ctk.CTkLabel(card, text=f"✅  {parts[0]}  —  catálogo: {cat_name}",
                            font=ctk.CTkFont(size=15, weight="bold"),
                            text_color="#1a237e").pack(anchor="w", padx=12, pady=(10, 2))
                for detail in [
                    f"🎭 Elenco:      {parts[1]}",
                    f"📝 Descripción: {parts[2]}",
                    f"🎬 Director:    {parts[3]}",
                    f"⏱️ Duración:    {parts[4]}",
                    f"🎞️ Género:      {parts[5]}",
                    f"📅 Año:         {parts[6]}",
                ]:
                    ctk.CTkLabel(card, text=detail, anchor="w").pack(anchor="w", padx=12)
                ctk.CTkLabel(card, text="").pack(pady=2)

        if not found:
            ctk.CTkLabel(results_frame, text=f"⚠️ Película '{movie_name}' no encontrada en ningún catálogo.", text_color="#c62828").pack()

    ctk.CTkButton(main_frame, text="Buscar", command=search, width=200).pack(pady=8)



def show_modify_movie():
    clear()
    show_title("Modificar Película")
    back_button()

    catalog_field = create_field("Nombre del catálogo:")
    movie_field   = create_field("Nombre de la película a modificar:")

    ctk.CTkLabel(main_frame, text="Atributo a modificar:", anchor="w").pack(fill="x")
    attributes = ["Nombre", "Elenco", "Descripción", "Director", "Duración", "Género", "Año"]
    dropdown = ctk.CTkOptionMenu(main_frame, values=attributes, width=400)
    dropdown.pack(pady=(0, 8))

    new_value_field = create_field("Nuevo valor:")

    def modify():
        cat_name = catalog_field.get().strip()
        if not os.path.exists(f"{cat_name}.txt"):
            show_message(f"⚠️ El catálogo '{cat_name}' no existe.", "#c62828")
            return

        index = attributes.index(dropdown.get())
        catalog = MovieCatalog(cat_name)
        for i, movie in enumerate(catalog.movies):
            if movie_field.get().strip().lower() in movie.lower():
                parts = movie.split(" | ")
                parts[index] = new_value_field.get().strip()
                catalog.movies[i] = " | ".join(parts)
                catalog._MovieCatalog__save_to_file()
                show_message("✅ Película modificada correctamente.")
                return
        show_message("⚠️ Película no encontrada.", "#c62828")

    ctk.CTkButton(main_frame, text="Modificar", command=modify, width=200).pack(pady=8)


def show_delete_movie():
    clear()
    show_title("Eliminar Película")
    back_button()

    catalog_field = create_field("Nombre del catálogo:")
    movie_field   = create_field("Nombre de la película:")

    def delete():
        cat_name = catalog_field.get().strip()
        if not os.path.exists(f"{cat_name}.txt"):
            show_message(f"⚠️ El catálogo '{cat_name}' no existe.", "#c62828")
            return
        catalog = MovieCatalog(cat_name)
        catalog.delete_movie(movie_field.get().strip())
        show_message("✅ Película eliminada correctamente.")

    ctk.CTkButton(
        main_frame, text="Eliminar", command=delete,
        width=200, fg_color="#c62828", hover_color="#b71c1c"
    ).pack(pady=8)


def show_delete_catalog():
    clear()
    show_title("Eliminar Catálogo")
    back_button()

    catalog_field = create_field("Nombre del catálogo:")

    def delete():
        cat_name = catalog_field.get().strip()
        catalog = MovieCatalog(cat_name)
        catalog.delete()
        show_message(f"✅ Catálogo '{cat_name}' eliminado.")

    ctk.CTkButton(
        main_frame, text="Eliminar", command=delete,
        width=200, fg_color="#c62828", hover_color="#b71c1c"
    ).pack(pady=8)



show_menu()
window.mainloop()