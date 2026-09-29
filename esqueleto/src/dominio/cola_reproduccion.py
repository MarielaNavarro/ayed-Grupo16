from src.tads.cola import Cola

class ColaReproduccion:
    """Cola de espera de canciones por sonar (FIFO)."""
    def __init__(self):
        self._cola = Cola()

    def agregar_a_la_cola(self, cancion):
        self._cola.encolar(cancion)

    def reproducir_siguiente(self):
        return self._cola.desencolar()
