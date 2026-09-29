from src.tads.nodo import Nodo

class ListaEnlazada:
    """
    Estructura de datos lineal implementada desde cero con Nodos[cite: 1].
    REGLA: No utiliza listas de Python (`list`) por debajo[cite: 1].
    """
    def __init__(self):
        # Referencia al primer nodo de la lista[cite: 1]
        self._cabeza = None
        # Contador para mantener el tamaño en O(1)[cite: 1]
        self._tamanio = 0

    def esta_vacia(self):
        """Devuelve True si la lista no contiene nodos, False en caso contrario[cite: 1]."""
        return self._cabeza is None

    def tamanio(self):
        """Devuelve la cantidad total de elementos almacenados en la lista[cite: 1]."""
        return self._tamanio

    def insertar_al_inicio(self, dato):
        """
        Agrega un nuevo elemento al inicio de la lista en O(1)[cite: 1].
        
        Pasos:
        1. Crea un nuevo nodo que apunta al nodo que actualmente era la cabeza[cite: 1].
        2. Actualiza la cabeza para que apunte al nuevo nodo[cite: 1].
        3. Incrementa el contador de tamaño[cite: 1].
        """
        nuevo_nodo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo_nodo
        self._tamanio += 1

    def insertar_al_final(self, dato):
        """
        Agrega un nuevo elemento al final de la lista en O(n)[cite: 1].
        
        Pasos:
        1. Crea el nuevo nodo sin siguiente (siguiente=None)[cite: 1].
        2. Si está vacía, pasa a ser la cabeza[cite: 1].
        3. Si no, recorre hasta el último nodo y enlaza el nuevo[cite: 1].
        """
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo_nodo
        else:
            actual = self._cabeza
            # Recorre la lista mientras exista un siguiente nodo[cite: 1]
            while actual.siguiente is not None:
                actual = actual.siguiente
            # Conecta el último nodo actual con el nuevo nodo[cite: 1]
            actual.siguiente = nuevo_nodo
        self._tamanio += 1

    def eliminar(self, dato):
        """
        Busca y remueve la primera aparición del dato indicado[cite: 1].
        Maneja los 3 casos principales: vacía, eliminar cabeza o nodo del medio/final[cite: 1].
        """
        # Caso 0: La lista está vacía, no hay nada que eliminar[cite: 1]
        if self.esta_vacia():
            return

        # Caso 1: El elemento a eliminar está en la cabeza de la lista[cite: 1]
        if self._cabeza.dato == dato:
            self._cabeza = self._cabeza.siguiente
            self._tamanio -= 1
            return

        # Caso 2: Buscar el elemento en el resto de los nodos de la lista[cite: 1]
        actual = self._cabeza
        while actual.siguiente is not None:
            # Si el nodo siguiente contiene el dato buscado, omitimos ese nodo[cite: 1]
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                self._tamanio -= 1
                return
            actual = actual.siguiente

    def buscar(self, dato):
        """
        Recorre la lista buscando un nodo con el dato especificado[cite: 1].
        Devuelve el Nodo si lo encuentra, o None si no existe en la lista[cite: 1].
        """
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                return actual  # Retorna la referencia al nodo encontrado[cite: 1]
            actual = actual.siguiente
        return None  # No se encontró el elemento en la lista[cite: 1]

    def __iter__(self):
        """
        Implementación del iterador usando la palabra clave `yield`[cite: 1].
        Permite recorrer la lista con bucles `for elemento in lista:`[cite: 1].
        """
        actual = self._cabeza
        while actual is not None:
            yield actual.dato  # Devuelve el valor actual y congela la ejecución[cite: 1]
            actual = actual.siguiente  # Avanza al siguiente nodo para la próxima iteración[cite: 1]
