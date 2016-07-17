import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def load_key(key_file, passphrase):
    return RSA.importKey(key_file, passphrase)


def gen_key():
    random = Random.new().read
    return RSA.generate(2048, random)


def encrypt(public_key, message):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message.encode('utf-8'))
    return base64.encodebytes(encrypted)


def decrypt(private_key, encrypted_message):
    cipher = PKCS1_OAEP.new(private_key)
    decoded = base64.decodebytes(encrypted_message)
    clear_bytes = cipher.decrypt(decoded)
    return clear_bytes.decode('utf-8')
