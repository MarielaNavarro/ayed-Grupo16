from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError


class Pila:
    """TAD Pila (LIFO) encapsulado sobre una ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()

    def esta_vacia(self):
        """Devuelve True si la pila no contiene elementos."""
        return self._items.esta_vacia()

    def __len__(self):
        """Devuelve la cantidad de elementos en la pila."""
        return len(self._items)

    def apilar(self, dato):
        """Agrega un elemento al tope de la pila en O(1)."""
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        """Remueve y devuelve el elemento del tope en O(1). Lanza PilaVaciaError si está vacía."""
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar de una pila vacía.")

        tope = self._items._cabeza.dato
        self._items.eliminar(tope)
        return tope

    def ver_tope(self):
        """Devuelve el elemento del tope sin removerlo. Lanza PilaVaciaError si está vacía."""
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self._items._cabeza.dato
