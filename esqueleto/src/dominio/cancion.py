from dataclasses import dataclass

@dataclass
class Cancion:
    id: int
    titulo: str
    artista: str
    album: str
    genero: str
    anio: int
    duracion_seg: int

    def formatear_duracion(self) -> str:
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}:{segundos:02d}"

    def mostrar_ficha_detalle(self) -> str:
        duracion_fmt = self.formatear_duracion()
        return (
            f"┌────────────────────────────────────────┐\n"
            f"│  N° {self.id:<3} - {self.titulo:<26} │\n"
            f"├────────────────────────────────────────┤\n"
            f"│  Artista  : {self.artista:<26} │\n"
            f"│  Álbum    : {self.album:<26} │\n"
            f"│  Género   : {self.genero:<26} │\n"
            f"│  Año      : {self.anio:<26} │\n"
            f"│  Duración : {duracion_fmt + ' min':<26} │\n"
            f"└────────────────────────────────────────┘"
        )        )
