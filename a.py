from sympy import randprime
from math import gcd
from sympy import mod_inverse

# RSA Algorithm
def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = 2
    while gcd(e, phi) != 1:
        e += 1

    # Use Extended Euclid's Algorithm to generate the private key
    d = mod_inverse(e, phi)

    # Return public and private keypair
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    # Unpack the key into it's components
    e, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** e) % n for char in plaintext]
    # Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    # Unpack the key into its components
    d, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** d) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)

def main():
    p = randprime(1, 100)
    q = randprime(1, 100)
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public ," and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public ," . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))

if __name__ == '__main__':
    main()
