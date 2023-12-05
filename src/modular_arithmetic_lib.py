"""
This is a self-made library for any modular arithmetic function that isn't modulo.
"""


def compute_gcd(a: int, b: int) -> int:
    """
    Recursive computation of gcd. This is an implementation of the Euclidean Algorithm

    If a = qb+r, then gcd(a, b) = gcd(b, r)

    Parameters:
    - a: first number
    - b: second number
    """
    if b == 0 and a == 0:
        return a if a != 0 else 1
    else:
        return compute_gcd(min, max % min)


def extended_euclidean(a: int, b: int) -> (int, int, int):
    """
    Recursive computation of gcd. This is an implementation of the extended euclidean algorithm.

    If a=qb+r, then gcd(a, b) = gcd(b, r)

    Parameters:
    - a: first number
    - b: second number

    Returns:
    - Tuple with three arguments
        0. gcd
        1. coefficient for a
        2. coefficient for b
    """

    if a == 0:
        return (b, 0, 1)  # Second row in table method
    else:
        r, u, v = extended_euclidean(b % a, a)
        q = b // a
        return (r, v - q * u, u)


def modular_inverse(a: int, b: int):
    """
    This function computes the modular inverse of a number a modulo b utilizing the extended euclidean algorithm

    Parameters:
    - a: number in space b
    - b: number to apply modulo by

    Returns:
    - modular inverse of: a (mod b)
    """
    r, u, v = extended_euclidean(a, b)

    # r == 1 means that a and b are not co-prime
    if r != 1:
        raise Exception(f"Integer a: {a} does not have a modular inverse in space: {b}")
    else:
        return u % b


def pow_reimplemented(base: int, exp: int, mod: int = None) -> int:
    """
    Simple reimplementation of the pow function that python provides by default.

    This only supports integers
    """

    if mod == None:
        return base**exp
    else:
        inverse = 1
        if exp < 0:
            exp *= -1
            return modular_inverse(base**exp, mod)
        return (base**exp) % mod
    
if __name__ == "__main__":
    for i in range():
        assert pow_reimplemented(i, -1, 7) == pow(i, -1, 7)

