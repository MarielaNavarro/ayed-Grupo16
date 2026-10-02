from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError


class Cola:
    """TAD Cola (FIFO) encapsulado sobre una ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()

    def esta_vacia(self):
        """Devuelve True si la cola no contiene elementos."""
        return self._items.esta_vacia()

    def __len__(self):
        """Devuelve la cantidad de elementos en la cola."""
        return len(self._items)

    def encolar(self, dato):
        """Agrega un elemento al final de la cola en O(n)."""
        self._items.insertar_al_final(dato)

    def desencolar(self):
        """Remueve y devuelve el primer elemento en O(1). Lanza ColaVaciaError si está vacía."""
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar de una cola vacía.")

        frente = self._items._cabeza.dato
        self._items.eliminar(frente)
        return frente

    def ver_frente(self):
        """Devuelve el primer elemento sin removerlo. Lanza ColaVaciaError si está vacía."""
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._items._cabeza.dato
