import random

# Function to calculate gcd (Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    for x in range(1, phi):
        if (e * x) % phi == 1:
            return x
    return None

# Function to generate a random prime number
def generate_prime(min_value, max_value):
    while True:
        num = random.randint(min_value, max_value)
        if is_prime(num):
            return num

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# RSA Key Generation
def generate_rsa_keys():
    # Step 1: Choose two large prime numbers
    p = generate_prime(100, 300)
    q = generate_prime(100, 300)
    while q == p:
        q = generate_prime(100, 300)
    
    # Step 2: Compute n and phi
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Step 3: Choose public key exponent e
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    # Step 4: Compute private key d
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)  # Public key, Private key

# RSA Encryption
def encrypt_rsa(plaintext, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

# RSA Decryption
def decrypt_rsa(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Example Usage
public_key, private_key = generate_rsa_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

# Encrypt a message
plaintext = "Hello RSA!"
print("Plaintext:", plaintext)
ciphertext = encrypt_rsa(plaintext, public_key)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_text = decrypt_rsa(ciphertext, private_key)
print("Decrypted Text:", decrypted_text)
