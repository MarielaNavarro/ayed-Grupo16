from src.tads.nodo import Nodo

class ListaEnlazada:
    """Estructura de datos lineal implementada con nodos enlazados."""
    
    def __init__(self):
        self._cabeza = None
        self._cant = 0  # Mantener la cantidad nos permite len() en O(1)

    def esta_vacia(self):
        """Devuelve True si la lista no contiene elementos."""
        return self._cabeza is None

    def __len__(self):
        """Devuelve la cantidad de elementos en la lista en O(1)."""
        return self._cant

    def buscar(self, dato):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
