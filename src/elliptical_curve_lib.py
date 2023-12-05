"""
This is a self-made library for anything involving eliptical curves
"""

from modular_arithmetic_lib import pow_reimplemented
from dataclasses import dataclass
from random import SystemRandom

@dataclass
class Point:
    x: int
    y: int


@dataclass
class Curve:
    a: int  # Coefficient of x^1
    b: int  # Coefficient of x^0
    modulo: int  # Modular space


def add_points(P: Point, Q: Point, curve: Curve) -> Point:
    """
    This function implements adding two points together on an eliptic curve.
    None is used to represent the point at infinity
    """
    if P == None:
        return Q
    elif Q == None:
        return P

    if (P.x == Q.x) and ((P.y == -Q.y) or (P.y != Q.y)):
        return None

    m = 1

    if curve.modulo == None:
        if P.x != Q.x:
            m = (Q.y - P.y) / (Q.x - P.x)
        elif P.y == Q.y:
            m = (3 * (P.x**2) + curve.a) / (2 * P.y)
    else:
        # If in a field, we can't just divide normally
        if P.x != Q.x:
            m = ((Q.y - P.y) * pow_reimplemented(Q.x - P.x, -1, curve.modulo)) % curve.modulo
        elif P.y == Q.y:
            m = ((3 * (P.x**2) + curve.a)* pow_reimplemented((2 * P.y), -1, curve.modulo)) % curve.modulo

    x_3 = m**2 - P.x - Q.x
    y_3 = m * (P.x - x_3) - P.y

    if curve.modulo == None:
        return Point(x_3, y_3)
    else:
        return Point(x_3 % curve.modulo, y_3 % curve.modulo)


def multiply_point(P: Point, n: int, curve: Curve) -> Point:
    """
    Multiplies an eliptical curve point by a scalar value n

    This is done by the double and add method
    """

    base = Point(P.x, P.y)
    copy = None

    while n > 0:
        if n % 2 == 0:
            base = add_points(base, base, curve)
            n = n // 2
        else:
            copy = add_points(base, copy, curve)
            n -= 1

    return copy

def create_random_curve(modulo):
    cryptogen = SystemRandom()
    a = cryptogen.randrange(100, 1000000)
    b = cryptogen.randrange(100, 1000000)
    return Curve(a, b, modulo)
    


if __name__ == "__main__":
    point1 = Point(2, 1)
    point2 = Point(6, 0)
    curve = Curve(2, 0, 7)

    result = add_points(point1, point2, curve)
    assert result != None
    assert result.x == 3
    assert result.y == 1

    result = multiply_point(point1, 2, curve)
    assert result.x == 3
    assert result.y == 6
