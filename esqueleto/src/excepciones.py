class PilaVaciaError(Exception):
    """Excepción lanzada al intentar operar en una pila vacía."""
    pass

class ColaVaciaError(Exception):
    """Excepción lanzada al intentar operar en una cola vacía."""
    pass

class ColeccionLlenaError(Exception):
    """Excepción lanzada al intentar agregar un elemento a una colección con capacidad máxima."""
    pass

class ArchivoInvalidoError(Exception):
    """Excepción lanzada al encontrar errores de formato o lectura en archivos CSV/datos."""
    pass

class ElementoNoEncontradoError(Exception):
    """Excepción lanzada al buscar o eliminar un elemento que no existe."""
    pass
