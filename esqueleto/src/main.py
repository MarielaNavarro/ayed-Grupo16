import csv                  # Módulo para leer archivos CSV
from pathlib import Path    # Manejo de rutas del sistema operativo
from dominio.cancion import Cancion  # Clase de dominio Cancion
from dominio.biblioteca import Biblioteca #Clase de dominio Biblioteca
def listar_catalogo(biblioteca: Biblioteca) -> None:
    """
    Función de interfaz de usuario: solicita el catálogo a la biblioteca
    y lo imprime formateado en forma de tabla por la consola.
    """
    # Obtenemos la lista de canciones desde el objeto del dominio Biblioteca.
    canciones = biblioteca.listar()
    
    # Validamos si la lista está vacía para informar al usuario de forma amigable.
    if not canciones:
        print("\nLa biblioteca está vacía.")
        return

    # Imprimimos los bordes y encabezados de la tabla con alineación de texto.
    print("\n" + "=" * 70)
    print(f"{'N°':<4} {'Título':<22} {'Artista':<18} {'Género':<12} {'Duración':<8}")
    print("=" * 70)

    # Recorremos cada canción e imprimimos sus propiedades formateadas.
    for tema in canciones:
        print(f"{tema.id:<4} {tema.titulo:<22} {tema.artista:<18} {tema.genero:<12} {tema.formatear_duracion():<8}")

    # Cerramos la tabla visualmente.
    print("=" * 70)

def ver_detalle_cancion(biblioteca: Biblioteca) -> None:
    """
    Función de interfaz de usuario: captura el input del usuario para buscar 
    una canción específica y muestra su ficha detallada por pantalla.
    """
    # Solicitamos al usuario que ingrese el ID o Título de la canción a consultar, limpiando espacios sobrantes.
    busqueda = input("\nIngrese el N° o Título de la canción a consultar: ").strip()

    # Validamos que el usuario no haya presionado Enter sin escribir nada.
    if not busqueda:
        print("Búsqueda cancelada: entrada vacía.")
        return

    # Delegamos la búsqueda de la canción a un método de la clase del dominio Biblioteca.
    encontrada = biblioteca.buscar_por_id_o_titulo(busqueda)

    # Si se encontró la canción, mostramos su ficha detallada; de lo contrario, avisamos del error.
    if encontrada:
        print("\n" + encontrada.mostrar_ficha_detalle())
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
    Cumple estrictamente con la regla de la E2: solo inicializa componentes,
    muestra el menú en bucle y despacha las opciones elegidas. No contiene lógica de negocio.
    """
  # Determinamos la ruta del directorio actual donde se encuentra este script.
    directorio_actual = Path(__file__).parent
    
    # Construimos de forma segura las rutas hacia los archivos CSV en la carpeta 'data/'.
    ruta_canciones_csv = directorio_actual.parent / "data" / "canciones.csv"
    ruta_versiones_csv = directorio_actual.parent / "data" / "versiones.csv" # <--- NUEVO

    # Cargamos el listado invocando a los métodos de la Biblioteca.
    biblioteca_musical = Biblioteca()
    biblioteca_musical.cargar_desde_csv(ruta_canciones_csv)
    biblioteca_musical.cargar_versiones_desde_csv(ruta_versiones_csv) # <--- NUEVO
    
    print(f"Sistema iniciado. Se cargaron {len(biblioteca_musical.listar())} canciones.")
    # ... (el resto del while True queda exactamente igual)

    # Bucle infinito para mantener la aplicación ejecutándose hasta que el usuario elija salir.
    while True:
        # Mostramos las opciones del menú en cada iteración.
        mostrar_menu()
        # Capturamos la opción elegida por el usuario y eliminamos espacios en blanco.
        opcion = input("Seleccione una opción (1-3): ").strip()

        # Despachamos la acción correspondiente según la opción seleccionada.
        if opcion == "1":
            listar_catalogo(biblioteca)
        elif opcion == "2":
            ver_detalle_cancion(biblioteca)
        elif opcion == "3":
            print("\n¡Gracias por utilizar la Biblioteca Musical!")
            break  # Rompemos el bucle while para finalizar la ejecución del programa.
        else:
            # Mensaje en caso de que el usuario ingrese un valor no contemplado en el menú.
            print("\nOpción inválida. Ingrese un número del 1 al 3.")

# Condicional estándar de Python para asegurar que main() se ejecute solo al iniciar el script directamente.
if __name__ == "__main__":
    main()
