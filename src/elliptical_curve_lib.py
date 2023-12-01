"""
This is a self-made library for anything involving eliptical curves
"""

from modular_arithmetic_lib import pow_reimplemented


def add_points(P: (int, int), Q: (int, int), a: int, modulo: int = None) -> (int, int):
    """
    This function implements adding two points together on an eliptic curve.
    None is used to represent the point at infinity
    """
    if P == None:
        return Q
    elif Q == None:
        return P

    if (P[0] == Q[0]) and ((P[1] == -Q[1]) or (P[1] != Q[1])):
        return None

    m = 1

    if modulo == None:
        if P[0] != Q[0]:
            m = (Q[1] - P[1]) / (Q[0] - P[0])
        elif P[1] == Q[1]:
            m = (3 * (P[0] ** 2) + a) / (2 * P[1])
    else:
        # If in a field, we can't just divide normally
        if P[0] != Q[0]:
            m = ((Q[1] - P[1]) * pow_reimplemented(Q[0] - P[0], -1, modulo)) % modulo
        elif P[1] == Q[1]:
            m = (
                (3 * (P[0] ** 2) + a) * pow_reimplemented((2 * P[1]), -1, modulo)
            ) % modulo

    x_3 = m**2 - P[0] - Q[0]
    y_3 = m * (P[0] - x_3) - P[1]

    if modulo == None:
        return (x_3, y_3)
    else:
        return (x_3 % modulo, y_3 % modulo)
