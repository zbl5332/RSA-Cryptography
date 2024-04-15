# -----------------------------------------------------------------------
# RSA Implementation
# -----------------------------------------------------------------------

from typing import Tuple

# Type defs
Key = Tuple[int, int]



def isprime(p: int) -> bool:
    '''
    Description: Checks if the input is a valid prime number
    Args: p (input integer)
    Returns: Bool
    '''
    if not isinstance(p, int):
        raise TypeError("Input must be an integer.")
    if p <= 1:
        return False
    i = 2
    while i * i <= p:
        if p % i == 0:
            return False
        i += 1
    return True
    #raise NotImplementedError()


def generate_keypair(p: int, q: int) -> Tuple[Key, Key]:
    '''
    Description: Generates the public and private key pair
    if p and q are distinct primes. Otherwise, raise a value error
    
    Args: p, q (input integers)

    Returns: Keypair in the form of (Pub Key, Private Key)
    PubKey = (n,e) and Private Key = (n,d)
    '''
    if not all(isinstance(i, int) for i in [p, q]):
        raise TypeError("Inputs must be integers.")
    if not (isprime(p) and isprime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("Numbers cannot be the same.")

    n = p * q
    k = (p - 1) * (q - 1)

    e = generate_public_exponent(k)
    d = modular_inverse(e, k)

    return ((n, e), (n, d))
    #raise NotImplementedError()


def generate_public_exponent(k: int) -> int:
    '''
    Description: Helper function that generates the SMALLEST
    public exponent for a given k value.

    Args: k (integer)

    Returns: e (public exponent)
    '''
    if not isinstance(k, int):
        raise TypeError("Input must be an integer.")
    e = 2
    while gcd(e, k) != 1:
        e += 1
    return e
    #raise NotImplementedError()


def gcd(x: int, y: int) -> int:
    '''
    Description: Helper function to compute gcd of two integers
    Args: x and y 
    Returns: gcd(x,y)
    '''
    if not all(isinstance(i, int) for i in [x, y]):
        raise TypeError("Both inputs must be integers.")
    while y:
        x, y = y, x % y
    return x
    #raise NotImplementedError()


def modular_inverse(a: int, n: int) -> int:
    '''
    Description: Helper function to compute the modular inverse
    of a with respect to n
    Args: a (integer), n (modulus)
    Returns: a^(-1)modn

    Examples:
    modular_inverse(3,10) = 7
    modular_inverse(2,5) = 3
    '''
    if not all(isinstance(i, int) for i in [a, n]):
        raise TypeError("Both inputs must be integers.")
    n0, x0, x1 = n, 0, 1
    if n == 1:
        return 0
    while a > 1:
        q = a // n
        n, a = a % n, n
        x0, x1 = x1 - q * x0, x0
    return x1 + n0 if x1 < 0 else x1
    #raise NotImplementedError()


def mod_exp(base: int, exp: int, mod: int) -> int:
    '''
    Description: Helper function for modular exponentiation
    Args: base (integer), exp (exponent), mod (modulus)
    Return: v (result of mod exponentiation)
    '''
    if not all(isinstance(i, int) for i in [base, exp, mod]):
        raise TypeError("Base, expoment, and mod must be integers.")
    v = 1
    base = base % mod
    while exp > 0:
        if exp % 2:
            v = (v * base) % mod
        exp //= 2
        base = (base * base) % mod
    return v
    #raise NotImplementedError()


def rsa_encrypt(m: int, pub_key: Key) -> int:
    '''
    Description: Encrypts the message with the given public
    key using the RSA algorithm.

    Args: m (positive integer input)

    Returns: c (encrypted cipher)
    '''
    if not isinstance(m, int):
        raise TypeError("Input must be an integer.")
    (n, e) = pub_key
    c = mod_exp(m, e, n)
    return c
    #raise NotImplementedError()


def rsa_decrypt(c: int, priv_key: Key) -> int:
    '''
    Description: Decrypts the ciphertext using the private key
    according to RSA algorithm

    Args: c (encrypted cipher)

    Returns: m (decrypted message, an integer)
    '''
    if not isinstance(c, int):
        raise TypeError("Ciphertext must be an integer.")
    (n, d) = priv_key
    m = mod_exp(c, d, n)
    return m
    #raise NotImplementedError()



if __name__ == '__main__':
    pass