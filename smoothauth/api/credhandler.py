from binascii import hexlify, unhexlify
from sys import stdin

from simplecrypt import encrypt, decrypt


def decryptCreds(salt, cipher):
    plaintext = decrypt(salt, unhexlify(cipher))
    return plaintext.decode('utf8')


def encryptCreds(salt, password):
    # encrypt the plaintext.  we explicitly convert to bytes first (optional)
    ciphertext = encrypt(salt, password.encode('utf8'))
    return hexlify(ciphertext).decode('utf8')
