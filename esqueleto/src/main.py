import os
import sys

# Permitir ejecuciones directas agregando el directorio raíz al PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.persistencia.manejador_csv import ManejadorCSV

# Ruta por defecto al archivo CSV de canciones
RUTA_DATASET = os.path.join("esqueleto", "data", "canciones.csv")


def mostrar_menu():
    print("\n" + "=" * 45)
    print("      BIBLIOTECA MUSICAL - MENÚ PRINCIPAL")
    print("=" * 45)
    print("1. Listar catálogo de canciones")
    print("2. Ver detalle de una canción")
    print("3. Salir")
    print("=" * 45)


def listar_catalogo(catalogo):
    if not catalogo:
        print("\n[!] El catálogo está vacío.")
        return

    print("\n--- CATÁLOGO DE CANCIONES ---")
    for cancion in catalogo:
        print(cancion.mostrar_resumen())


def ver_detalle(catalogo):
    if not catalogo:
        print("\n[!] El catálogo está vacío.")
        return

    try:
        id_buscar = int(input("\nIngrese el ID de la canción: "))
        encontrado = False

        for cancion in catalogo:
            if cancion.id == id_buscar:
                print("\n" + "-" * 35)
                print(f"ID:                 #{cancion.id:03d}")
                print(f"Título:             {cancion.titulo}")
                print(f"Artista:            {cancion.artista}")
                print(f"Álbum:              {cancion.album}")
                print(f"Género:             {cancion.genero}")
                print(
                    f"Duración:           {cancion.duracion_segundos // 60}:{cancion.duracion_segundos % 60:02d} min"
                )
                print(f"Año:                {cancion.anio}")
                print(f"IDs de versiones:   {cancion.versiones}")
                print("-" * 35)
                encontrado = True
                break

        if not encontrado:
            print(f"\n[!] No se encontró ninguna canción con el ID {id_buscar}.")

    except ValueError:
        print("\n[Error] Debe ingresar un número entero válido.")


def main():
    print("Cargando catálogo musical...")
    try:
        catalogo = ManejadorCSV.cargar_catalogo(RUTA_DATASET)
        print(f"¡Catálogo cargado con éxito! ({len(catalogo)} canciones)")
    except Exception as e:
        print(f"[Error al cargar CSV]: {e}")
        catalogo = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_catalogo(catalogo)
        elif opcion == "2":
            ver_detalle(catalogo)
        elif opcion == "3":
            print("\n¡Gracias por usar la Biblioteca Musical! Saliendo...")
            break
        else:
            print("\n[Opción inválida] Por favor, ingrese un número del 1 al 3.")


if __name__ == "__main__":
    main()
