import random
from sympy import isprime

# Function to generate prime numbers (for simplicity)
def generate_prime(bits=8):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

# RSA Key Generation
def generate_keys(bits=8):
    # Generate two distinct primes p and q
    p = generate_prime(bits)
    q = generate_prime(bits)
    
    n = p * q  # Modulus for public and private keys
    phi_n = (p - 1) * (q - 1)  # Euler's Totient function
    
    # Choose a public exponent e such that 1 < e < phi_n and gcd(e, phi_n) = 1
    e = 65537  # Common choice for e (prime number)
    d = modinv(e, phi_n)  # Compute private exponent d

    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

# Function to calculate modular inverse (used for finding d)
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Encryption function (using public key)
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]  # M^e mod n
    return encrypted_message

# Decryption function (using private key)
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])  # C^d mod n
    return decrypted_message

# Example usage:
public_key, private_key = generate_keys(bits=8)
message = "Hello RSA!"

# Encrypt the message using the public key
encrypted_message = encrypt(message, public_key)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message using the private key
decrypted_message = decrypt(encrypted_message, private_key)
print(f"Decrypted message: {decrypted_message}")
