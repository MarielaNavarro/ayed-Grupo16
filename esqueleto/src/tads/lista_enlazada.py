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
        
    def eliminar(self, dato):
            """Busca y elimina la primera ocurrencia de dato en la lista."""
            if self.esta_vacia():
                return False

                # Caso 1: El elemento a eliminar está en la cabeza
            if self._cabeza.dato == dato:
                self._cabeza = self._cabeza.siguiente
                self._cant -= 1
                return True

        # Caso 2: El elemento está en el resto de la lista
            actual = self._cabeza
            while actual.siguiente is not None:
                if actual.siguiente.dato == dato:
                    actual.siguiente = actual.siguiente.siguiente
                    self._cant -= 1
                    return True
                actual = actual.siguiente

            return False  # No se encontró el dato
    def buscar(self, criterio_o_dato):
        """
        Busca un elemento en la lista.
        Puede recibir un dato para comparar por igualdad o una función/criterio.
        """
        actual = self._cabeza
        while actual is not None:
            if callable(criterio_o_dato):
                if criterio_o_dato(actual.dato):
                    return actual.dato
            elif actual.dato == criterio_o_dato:
                return actual.dato
            actual = actual.siguiente
        return None
    def __iter__(self):
        """Permite iterar sobre la lista con un bucle for."""
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
