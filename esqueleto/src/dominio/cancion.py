class Cancion:
    def __init__(self, titulo, artista, genero):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.genero})"
