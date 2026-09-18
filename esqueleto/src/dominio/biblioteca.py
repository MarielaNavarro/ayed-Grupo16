import csv                  # Módulo integrado de Python para leer y escribir archivos CSV.
from pathlib import Path    # Módulo para el manejo seguro y multiplataforma de rutas de archivos.
from src.dominio.cancion import Cancion  # Importamos la clase del dominio 'Cancion' desde su módulo correspondiente.

class Biblioteca:
    """
    Clase del dominio que encapsula la colección de canciones y la lógica de negocio
    asociada (carga desde CSV, listado y búsquedas). Esto evita que main.py concentre la lógica.
    """
    def cargar_versiones_desde_csv(self, ruta_archivo: Path) -> None:
        """
        Lee el archivo de versiones (versiones.csv) y construye un diccionario interno
        donde la clave es el ID de la canción original y el valor es una lista 
        con los IDs de sus versiones directas.
        """
        self.diccionario_versiones = {}  # Inicializamos el diccionario como atributo de la clase.

        if not ruta_archivo.exists():
            print(f"Error: No se encontró el archivo de versiones en {ruta_archivo}")
            return

        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                id_version = int(fila["cancion_id"])
                id_original = int(fila["version_de_id"])
                
                # Agrupamos en el diccionario: a la canción original le sumamos su versión derivada.
                if id_original not in self.diccionario_versiones:
                    self.diccionario_versiones[id_original] = []
                self.diccionario_versiones[id_original].append(id_version)

    def versiones_directas(self, id_cancion: int) -> list:
        """
        Retorna una lista con los IDs de las versiones directas (covers/lives) de una canción.
        """
        # Si el diccionario no fue creado aún, retornamos vacío.
        if not hasattr(self, 'diccionario_versiones'):
            return []
            
        # Retorna la lista de versiones si la canción existe como clave, sino una lista vacía.
        return self.diccionario_versiones.get(id_cancion, [])

    def listar_todas_las_versiones(self, id_cancion: int) -> list:
        """
        FUNCIÓN RECURSIVA DEL DOMINIO (Ítem 2 de la E2):
        Busca todas las versiones derivadas de una canción, y las versiones de esas versiones.
        """
        directas = self.versiones_directas(id_cancion)
        
        # CASO BASE: Si la canción no tiene versiones directas, cortamos la recursión devolviendo una lista vacía.
        if not directas:
            return []
            
        # CASO RECURSIVO: Si tiene versiones, copiamos la lista actual y buscamos recursivamente por cada una.
        resultado = list(directas)
        for version in directas:
            resultado += self.listar_todas_las_versiones(version)
            
        return resultado
    def __init__(self):
        """Constructor de la clase: inicializa una lista vacía para almacenar las canciones."""
        self.canciones = []  # Lista interna que contendrá objetos de la clase Cancion.

    def cargar_desde_csv(self, ruta_archivo: Path) -> None:
        """
        Abre el archivo CSV especificado y mapea cada fila a un objeto de la clase Cancion,
        agregándolo a la lista de la biblioteca.
        """
        # Verificamos si el archivo físico realmente existe antes de intentar abrirlo.
        if not ruta_archivo.exists():
            print(f"Error: No se encontró el archivo en {ruta_archivo}")
            return  # Salimos de la función si el archivo no está presente.

        # Abrimos el archivo en modo lectura ('r') con codificación UTF-8 para evitar problemas con tildes o eñes.
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            # Creamos un lector de diccionarios que toma la primera fila del CSV como nombres de claves.
            lector = csv.DictReader(archivo)

            # Iteramos fila por fila dentro del archivo CSV.
            for fila in lector:
                # Instanciamos un objeto de la clase Cancion convirtiendo los tipos de datos necesarios.
                cancion = Cancion(
                    id=int(fila["id"]),
                    titulo=fila["titulo"],
                    artista=fila["artista"],
                    album=fila["album"],
                    genero=fila["genero"],
                    anio=int(fila["anio"]),
                    duracion_seg=int(fila["duracion_seg"]),
                    cancion_original=int(fila.get("cancion_original", 0))  # Valor por defecto 0 si no existe la columna.
                )
                # Agregamos la canción ya creada a nuestra lista interna del dominio.
                self.canciones.append(cancion)

    def listar(self) -> list:
        """Retorna la lista completa de objetos Cancion almacenados en la biblioteca."""
        return self.canciones

    def buscar_por_id_o_titulo(self, busqueda: str):
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
