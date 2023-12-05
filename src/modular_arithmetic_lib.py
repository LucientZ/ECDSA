"""
This is a self-made library for any modular arithmetic function that isn't modulo.
"""

import random

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
    
def miller_rabin_witness(a: int, q: int, k: int, N: int) -> bool:
    """
    This function implements the miller-rabin test for given variables
    - a: number to be tested
    - q: q such that N-1 == (2^k)*q
    - k: k such that N-1 == (2^k)*q
    - N: Number being tested to be composite

    returns: whether or not a number is composite (a is a witness)
    """
    # This keeps me from shooting myself in the foot
    if (2**k) * q != N - 1:
        raise Exception(f"Invalid q and k values: 2^{k} * {q} != {N}-1")

    satisfies_first_condition: bool = False
    satisfies_second_condition: bool = True

    if pow(a, q, N) != 1:
        satisfies_first_condition = True

    for i in range(0, k):
        if pow(a, (2**i) * q, N) == -1 % N:
            satisfies_second_condition = False
            break

    if satisfies_first_condition and satisfies_second_condition:
        return True
    else:
        return False
    
def generate_random_large_prime() -> int:
    """
    Generates a very large number that is most likely prime
    """
    cryptogen = random.SystemRandom()

    while(True):
        potential_prime = cryptogen.randint(10000000000000,1000000000000000000000)
        is_likely_prime = True

        if potential_prime % 2 == 0:
            continue


        i = 0
        while(i < 100):
            possible_witness = cryptogen.randint(2, potential_prime-1)

            k = 0
            q = 0
            while ((potential_prime - 1) // (2**k)) % 2 == 0:
                k += 1
            q = (potential_prime - 1) // (2**k)

            if(miller_rabin_witness(possible_witness, q, k, potential_prime)):
                is_likely_prime = False
                break
            i += 1
        if is_likely_prime:
            return potential_prime

if __name__ == "__main__":
    print(generate_random_large_prime())

