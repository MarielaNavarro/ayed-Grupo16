import csv
from pathlib import Path
from src.dominio.cancion import Cancion
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ArchivoInvalidoError, ElementoNoEncontradoError


class Biblioteca:
    """
    Clase del dominio que encapsula la colección de canciones y la lógica de negocio
    asociada, utilizando la estructura propia ListaEnlazada.
    """

    def __init__(self):
        """Inicializa las colecciones internas utilizando ListaEnlazada."""
        self.canciones = ListaEnlazada()
        self.diccionario_versiones = {}

    def cargar_desde_csv(self, ruta_archivo: Path) -> None:
        """
        Lee el archivo CSV e inserta cada canción en la ListaEnlazada.
        Lanza ArchivoInvalidoError si el archivo no existe.
        """
        if not ruta_archivo.exists():
            raise ArchivoInvalidoError(f"No se encontró el archivo de canciones en {ruta_archivo}")

        try:
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
                        duracion_seg=int(fila["duracion_seg"]),
                        cancion_original=int(fila.get("cancion_original", 0))
                    )
                    # Insertamos al final de nuestra ListaEnlazada
                    self.canciones.insertar_al_final(cancion)
        except (KeyError, ValueError) as e:
            raise ArchivoInvalidoError(f"El archivo CSV tiene un formato inválido: {e}")

    def cargar_versiones_desde_csv(self, ruta_archivo: Path) -> None:
        """
        Lee el archivo de versiones y agrupa los IDs utilizando ListaEnlazada para cada original.
        Lanza ArchivoInvalidoError si el archivo no existe.
        """
        if not ruta_archivo.exists():
            raise ArchivoInvalidoError(f"No se encontró el archivo de versiones en {ruta_archivo}")

        try:
            with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    id_version = int(fila["cancion_id"])
                    id_original = int(fila["version_de_id"])

                    if id_original not in self.diccionario_versiones:
                        self.diccionario_versiones[id_original] = ListaEnlazada()
                    
                    self.diccionario_versiones[id_original].insertar_al_final(id_version)
        except (KeyError, ValueError) as e:
            raise ArchivoInvalidoError(f"El archivo de versiones tiene un formato inválido: {e}")

    def versiones_directas(self, id_cancion: int) -> ListaEnlazada:
        """Retorna la ListaEnlazada de IDs de las versiones directas."""
        return self.diccionario_versiones.get(id_cancion, ListaEnlazada())

    def listar_todas_las_versiones(self, id_cancion: int) -> ListaEnlazada:
        """
        Busca recursivamente todas las versiones derivadas y las almacena en una ListaEnlazada.
        """
        resultado = ListaEnlazada()
        directas = self.versiones_directas(id_cancion)

        if directas.esta_vacia():
            return resultado

        for version in directas:
            resultado.insertar_al_final(version)
            sub_versiones = self.listar_todas_las_versiones(version)
            for sub in sub_versiones:
                resultado.insertar_al_final(sub)

        return resultado

    def listar( me ) -> ListaEnlazada:
        """Retorna la ListaEnlazada completa de objetos Cancion."""
        return self.canciones

    def buscar_por_id_o_titulo(self, busqueda: str) -> Cancion:
        """
        Busca una canción dentro de la ListaEnlazada.
        Lanza ElementoNoEncontradoError si no se encuentra.
        """
        es_numero = busqueda.isdigit()
        id_buscado = int(busqueda) if es_numero else None
        busqueda_lower = busqueda.lower()

        # Usamos el método buscar de nuestra ListaEnlazada pasando un criterio lambda
        cancion = self.canciones.buscar(
            lambda tema: (es_numero and tema.id == id_buscado) or (tema.titulo.lower() == busqueda_lower)
        )

        if cancion is None:
            raise ElementoNoEncontradoError(f"No se encontró ninguna canción con el criterio '{busqueda}'.")

        return cancion

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
