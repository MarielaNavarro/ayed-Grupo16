import csv                  # Módulo para leer archivos CSV
from pathlib import Path    # Manejo de rutas del sistema operativo
from dominio.cancion import Cancion  # Clase de dominio Cancion

def cargar_biblioteca_desde_csv(ruta_archivo: Path) -> list:
    """Abre el archivo CSV y carga las canciones en una lista."""
    biblioteca = []

    if not ruta_archivo.exists():
        print(f"Error: No se encontró el archivo en {ruta_archivo}")
        return biblioteca

    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            cancion = Cancion(
                id=int(fila["id"]),
                titulo=fila["titulo"],
                artista=fila["artista"],
                album=fila["album"],
                genero=fila["genero"],
                anio=int(fila["anio"]),
                duracion_seg=int(fila["duracion_seg"])
            )
            biblioteca.append(cancion)

    return biblioteca

def listar_catalogo(biblioteca: list) -> None:
    """Imprime el catálogo completo en formato de tabla."""
    if not biblioteca:
        print("\nLa biblioteca está vacía.")
        return

    print("\n" + "=" * 70)
    print(f"{'N°':<4} {'Título':<22} {'Artista':<18} {'Género':<12} {'Duración':<8}")
    print("=" * 70)

    for tema in biblioteca:
        print(f"{tema.id:<4} {tema.titulo:<22} {tema.artista:<18} {tema.genero:<12} {tema.formatear_duracion():<8}")

    print("=" * 70)

def ver_detalle_cancion(biblioteca: list) -> None:
    """Busca una canción por N° de ID o Título."""
    busqueda = input("\nIngrese el N° o Título de la canción a consultar: ").strip()

    if not busqueda:
        print("Búsqueda cancelada: entrada vacía.")
        return

    encontrada = None

    for tema in biblioteca:
        if busqueda.isdigit() and tema.id == int(busqueda):
            encontrada = tema
            break
        elif tema.titulo.lower() == busqueda.lower():
            encontrada = tema
            break

    if encontrada:
        print("\n" + encontrada.mostrar_ficha_detalle())
    else:
        print(f"No se encontró ninguna canción con el criterio: '{busqueda}'.")

def mostrar_menu() -> None:
    print("\n╔══════════════════════════════════════════╗")
    print("║     BIBLIOTECA MUSICAL - CLI (E1)        ║")
    print("╠══════════════════════════════════════════╣")
    print("║ 1. Listar canciones del catálogo         ║")
    print("║ 2. Ver detalle de una canción            ║")
    print("║ 3. Salir                                 ║")
    print("╚══════════════════════════════════════════╝")

def main() -> None:
    directorio_actual = Path(__file__).parent
    ruta_csv = directorio_actual.parent / "data" / "canciones.csv"

    biblioteca_musical = cargar_biblioteca_desde_csv(ruta_csv)
    print(f"Sistema iniciado. Se cargaron {len(biblioteca_musical)} canciones.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            listar_catalogo(biblioteca_musical)
        elif opcion == "2":
            ver_detalle_cancion(biblioteca_musical)
        elif opcion == "3":
            print("\n¡Gracias por utilizar la Biblioteca Musical!")
            break
        else:
            print("\nOpción inválida. Ingrese un número del 1 al 3.")

if __name__ == "__main__":
    main()
