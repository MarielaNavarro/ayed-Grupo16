import csv            # Módulo para leer archivos CSV
from pathlib import Path    # Manejo de rutas del sistema operativo
from src.dominio.cancion import Cancion  # Clase de dominio Cancion
from src.dominio.biblioteca import Biblioteca

def listar_catalogo(biblioteca: Biblioteca) -> None:
    """
    Función de interfaz de usuario: solicita el catálogo a la biblioteca
    y lo imprime formateado en forma de tabla por la consola.
    """
    canciones = biblioteca.listar()
    
    if not canciones:
        print("\nLa biblioteca está vacía.")
        return

    print("\n" + "=" * 70)
    print(f"{'N°':<4} {'Título':<22} {'Artista':<18} {'Género':<12} {'Duración':<8}")
    print("=" * 70)

    for tema in canciones:
        print(f"{tema.id:<4} {tema.titulo:<22} {tema.artista:<18} {tema.genero:<12} {tema.formatear_duracion():<8}")

    print("=" * 70)

def ver_detalle_cancion(biblioteca: Biblioteca) -> None:
    """
    Función de interfaz de usuario: captura el input del usuario para buscar 
    una canción específica y muestra su ficha detallada por pantalla junto con sus versiones.
    """
    busqueda = input("\nIngrese el N° o Título de la canción a consultar: ").strip()

    if not busqueda:
        print("Búsqueda cancelada: entrada vacía.")
        return

    encontrada = biblioteca.buscar_por_id_o_titulo(busqueda)

    if encontrada:
        print("\n" + encontrada.mostrar_ficha_detalle())
        
        # --- NUEVO: Invocamos la función recursiva del dominio para las versiones ---
        versiones_ids = biblioteca.listar_todas_las_versiones(encontrada.id)
        if versiones_ids:
            print(f"-> Versiones derivadas (IDs): {versiones_ids}")
        else:
            print("-> No registra versiones derivadas (Caso base alcanzado).")
    else:
        print(f"No se encontró ninguna canción con el criterio: '{busqueda}'.")

def mostrar_menu() -> None:
    """Imprime por consola las opciones disponibles del menú principal del sistema."""
    print("\n╔══════════════════════════════════════════╗")
    print("║     BIBLIOTECA MUSICAL - CLI (E2)        ║")
    print("╠══════════════════════════════════════════╣")
    print("║ 1. Listar canciones del catálogo         ║")
    print("║ 2. Ver detalle de una canción            ║")
    print("║ 3. Salir                                 ║")
    print("╚══════════════════════════════════════════╝")

def main() -> None:
    """
    Punto de entrada principal de la aplicación. 
    """
    directorio_actual = Path(__file__).parent
    
    # Rutas hacia los archivos CSV en la carpeta data/
    ruta_csv = directorio_actual.parent / "data" / "canciones.csv"
    ruta_versiones_csv = directorio_actual.parent / "data" / "versiones.csv"  # <--- NUEVO

    biblioteca = Biblioteca()
    biblioteca.cargar_desde_csv(ruta_csv)
    biblioteca.cargar_versiones_desde_csv(ruta_versiones_csv)                  # <--- NUEVO
    
    print(f"Sistema iniciado. Se cargaron {len(biblioteca.listar())} canciones.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            listar_catalogo(biblioteca)
        elif opcion == "2":
            ver_detalle_cancion(biblioteca)
        elif opcion == "3":
            print("\n¡Gracias por utilizar la Biblioteca Musical!")
            break 
        else:
            print("\nOpción inválida. Ingrese un número del 1 al 3.")

if __name__ == "__main__":
    main()
