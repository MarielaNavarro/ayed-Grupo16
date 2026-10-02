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
# src/tads/lista_enlazada.py

from src.tads.nodo import Nodo

class ListaEnlazada:
    """Estructura de datos lineal implementada con nodos enlazados."""
    
    def __init__(self):
        self._cabeza = None
        self._cant = 0

    def esta_vacia(self):
        """Devuelve True si la lista no contiene elementos."""
        return self._cabeza is None

    def __len__(self):
        """Devuelve la cantidad de elementos en la lista."""
        return self._cant

    def insertar_al_inicio(self, dato):
        """Agrega un elemento al principio de la lista. Complejidad: O(1)."""
        nuevo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo
        self._cant += 1

    def insertar_al_final(self, dato):
        """Agrega un elemento al final de la lista. Complejidad: O(n)."""
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._cant += 1
