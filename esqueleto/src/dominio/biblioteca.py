import csv
from pathlib import Path
from src.dominio.cancion import Cancion

class Biblioteca:
    def __init__(self):
        self.canciones: list[Cancion] = []
        # Estructura: id_original -> lista de tuplas (id_derivada, tipo)
        self.versiones_map: dict[int, list[tuple[int, str]]] = {}

    def cargar_desde_csv(self, ruta_csv: Path) -> None:
        if not ruta_csv.exists():
            return
        with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                self.canciones.append(
                    Cancion(
                        id=int(fila["id"]),
                        titulo=fila["titulo"],
                        artista=fila["artista"],
                        album=fila["album"],
                        genero=fila["genero"],
                        anio=int(fila["anio"]),
                        duracion_seg=int(fila["duracion_seg"])
                    )
                )

    def cargar_versiones(self, ruta_csv: Path) -> None:
        """Carga el archivo de versiones leyendo cancion_id, version_de_id, tipo."""
        if not ruta_csv.exists():
            return
        with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                derivada = int(fila["cancion_id"])
                original = int(fila["version_de_id"])
                tipo = fila["tipo"].strip()

                if original not in self.versiones_map:
                    self.versiones_map[original] = []
                self.versiones_map[original].append((derivada, tipo))

    def buscar_por_id(self, id_cancion: int) -> Cancion | None:
        for c in self.canciones:
            if c.id == id_cancion:
                return c
        return None

    def buscar_por_criterio(self, criterio: str) -> Cancion | None:
        if criterio.isdigit():
            return self.buscar_por_id(int(criterio))
        for c in self.canciones:
            if c.titulo.lower() == criterio.lower():
                return c
        return None

    def obtener_versiones_derivadas(self, id_cancion: int) -> list[tuple[int, str]]:
        """
        Algoritmo recursivo del dominio (Ítem 2 de E2).
        Devuelve una lista de tuplas (id_derivado, tipo_version).
        """
        directas = self.versiones_map.get(id_cancion, [])

        # CASO BASE: Si no tiene canciones derivadas, retorna lista vacía
        if not directas:
            return []

        # CASO RECURSIVO: Agrega las derivadas directas y busca iterativamente sus sub-derivadas
        resultado = list(directas)
        for id_derivado, _ in directas:
            resultado += self.obtener_versiones_derivadas(id_derivado)

        return resultado
