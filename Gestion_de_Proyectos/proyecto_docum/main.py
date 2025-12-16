# docstrings
def sumar(a: int, b: int) -> int:
    """Suma dos enteros.

    Parameters
    ----------
    a : int
        Primer sumando.
    b : int
        Segundo sumando.

    Returns
    -------
    int
        Resultado de la suma.

    Examples
    --------
    >>> sumar(2, 3)
    5
    """
    return a + b


def potencia(base: float, exponente: float) -> float:
    """Calcula la potencia de un número.

    Eleva la base al exponente indicado y devuelve el resultado.

    Args:
        base (float): Base de la potencia.
        exponente (float): Exponente al que se eleva la base.

    Returns:
        float: Resultado de la operación base**exponente.

    Raises:
        TypeError: Si alguno de los argumentos no es numérico.
    """
    return base**exponente


def main():
    sumar(12, 22)


if __name__ == '__main__':
    main()
