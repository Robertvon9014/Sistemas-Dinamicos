import numpy as np

def dyn_generator(oper, state):
    """Genera la dinámica del sistema cuántico.

    Calcula la evolución temporal del sistema basado en el operador dado.

    Args:
        oper (np.ndarray): Operador cuántico O.
        state (np.ndarray): Estado actual del sistema y(t).

    Returns:
        (ndarray): Derivada temporal del estado.

    Examples:
        >>> oper = np.array([[1, 0], [0, -1]])
        >>> state = np.array([[0.5, 0], [0, 0.5]])
        >>> dyn_generator(oper, state)
        array([[ 0.+0.j,  0.+0.j],
               [ 0.+0.j,  0.+0.j]])
    """
    return -1.0j * (np.dot(oper, state) - np.dot(state, oper))


def rk4(func, oper, state, h):
    """Aplica el método RK4 para resolver la evolución temporal del sistema.

    Args:
        func (function): Función que genera la dinámica (e.g., `dyn_generator`).
        oper (np.ndarray): Operador cuántico O.
        state (np.ndarray): Estado inicial del sistema.
        h (float): Paso de tiempo.

    Returns:
        (ndarray): Estado actualizado después de un paso temporal.

    Examples:
        >>> oper = np.array([[1, 0], [0, -1]])
        >>> state = np.array([[0.5, 0], [0, 0.5]])
        >>> h = 0.01
        >>> rk4(dyn_generator, oper, state, h)
        array([[0.5+0.j, 0. +0.j],
               [0. +0.j, 0.5+0.j]])
    """
    k1 = h * func(oper, state)
    k2 = h * func(oper, state + (0.5 * k1))
    k3 = h * func(oper, state + (0.5 * k2))
    k4 = h * func(oper, state + k3)

    return state + (1/6)*(k1 + (2*k2) + (2*k3) + k4)



