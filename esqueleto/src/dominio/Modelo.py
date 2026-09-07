from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Cancion:
    id: int
    titulo: str
    artista: str
    album: str
    genero: str
    duracion_segundos: int
    anio: int
    # Lista de IDs de canciones que son versiones (covers, remixes, live) de esta
    versiones: List[int] = field(default_factory=list)

    def mostrar_resumen(self) -> str:
        """Devuelve una línea de texto resumida para mostrar en el catálogo."""
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"#{self.id:03d} | {self.titulo} - {self.artista} [{self.genero}] ({minutos}:{segundos:02d}) - {self.anio}"

    def formato_csv(self) -> str:
        """Convierte los datos a una línea de texto CSV para guardar en archivo."""
        versiones_str = ";".join(map(str, self.versiones))
        return f"{self.id},{self.titulo},{self.artista},{self.album},{self.genero},{self.duracion_segundos},{self.anio},{versiones_str}"
