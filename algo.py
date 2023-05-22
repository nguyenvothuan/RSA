import sympy

# config variables
prime_length = 10

# utility functions
def string_to_ascii(string: str) -> int:
    # return a number represent the string's chracaters' ascii code
    return int.from_bytes(string.encode(), 'big')

def ascii_to_string(ascii: int)-> str:
    # return a string represent the ascii code
    return ascii.to_bytes((ascii.bit_length() + 7) // 8, 'big').decode()

def cook(no_digits: int=prime_length) -> tuple:
    # return 2 super large prime numbers
    if no_digits<1:
        raise ValueError("no_digits must be a positive integer")
    p = sympy.randprime(10**(no_digits-1), 10**no_digits-1)
    q = sympy.randprime(10**(no_digits-1), 10**no_digits-1)
    return p,q

def prepare()-> tuple:
    # return n, phi, e, d
    p,q = cook()
    n = p*q
    phi = (p-1)*(q-1)
    e = sympy.randprime(2, phi-1)
    d = sympy.mod_inverse(e, phi)
    return (n, e), (phi, d)

def encrypt(public_key: tuple, m: int) -> int:
    # return ciphertext
    n, e = public_key
    return pow(m, e, n)

def decrypt(public_key, private_key: tuple, c: int) -> int:
    # return plaintext
    _, d = private_key
    n, _ = public_key
    return pow(c, d, n)

def brute_force_decrypt(public_key: tuple, c: int)->int:
    # return plaintext
    n, e = public_key
    for i in range(1, n):
        if pow(i, e, n) == c:
            return i
    return -1
