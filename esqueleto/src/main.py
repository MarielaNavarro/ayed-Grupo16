import csv                  # Módulo para leer archivos CSV
from pathlib import Path    # Manejo de rutas del sistema operativo
from src.dominio.cancion import Cancion  # Clase de dominio Cancion

class biblioteca
    """
    Clase del dominio que encapsula la colección de canciones y la lógica de negocio
    asociada (carga desde CSV, listado y búsquedas). Esto evita que main.py concentre la lógica.
    """
    
    def __init__(self):
        """Constructor de la clase: inicializa una lista vacía para almacenar las canciones."""
        self.canciones = []  # Lista interna que contendrá objetos de la clase Cancion.
        # Verificamos si el archivo físico realmente existe antes de intentar abrirlo.
    def cargar_biblioteca_desde_csv(ruta_archivo: Path) -> list:
            """Abre el archivo CSV y carga las canciones en una lista."""
            biblioteca = []

            if not ruta_archivo.exists():
                print(f"Error: No se encontró el archivo en {ruta_archivo}")
                return #Salimos de la función si el archivo no está presente.
# Abrimos el archivo en modo lectura ('r') con codificación UTF-8 para evitar problemas con tildes o eñes.
            with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
                # Creamos un lector de diccionarios que toma la primera fila del CSV como nombres de claves.
                lector = csv.DictReader(archivo)

                for fila in lector:
                    cancion = Cancion(
                        id=int(fila["id"]),
                        titulo=fila["titulo"],
                        artista=fila["artista"],
                        album=fila["album"],
                        genero=fila["genero"],
                        anio=int(fila["anio"]),
                        duracion_seg=int(fila["duracion_seg"]),
                        cancion_original=int(fila.get("cancion_original", 0))  #  Valor por defecto 0 si no existe la columna.
                )
                # Agregamos la canción ya creada a nuestra lista interna del dominio.
                        
                    self.canciones.append(cancion)

          
    def listar_catalogo(self) -> list:
        """Retorna la lista completa de objetos Cancion almacenados en la biblioteca."""
        return self.canciones
         

 

    def ver_detalle_cancion(self, busqueda: str):
        """
        Busca una canción dentro de la biblioteca comparando el parámetro de búsqueda 
        con el ID numérico o con la coincidencia exacta (sin distinción de mayúsculas) del título.
        Retorna el objeto Cancion si lo encuentra, o None en caso contrario.
        """
            for tema in self.canciones:
            # Si el texto ingresado es un número y coincide con el ID de la canción...
                if busqueda.isdigit() and tema.id == int(busqueda):
                    return tema
            # O si el título de la canción coincide exactamente con el texto de búsqueda (ignorando mayúsculas/minúsculas)...
                elif tema.titulo.lower() == busqueda.lower():
                    return tema
        
        # Si recorremos toda la lista y no hay coincidencias, retornamos None.
            return None



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
