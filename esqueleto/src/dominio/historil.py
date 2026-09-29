from src.tads.pila import Pila

class HistorialReproduccion:
    """Historial de canciones escuchadas (LIFO)."""
    def __init__(self):
        self._pila = Pila()

    def registrar_reproduccion(self, cancion):
        self._pila.apilar(cancion)

    def deshacer(self):
        return self._pila.desapilar()
