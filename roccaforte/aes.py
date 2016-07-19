import os
import base64
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto import Random


def otk():
    passphrase = os.urandom(512)
    salt = os.urandom(64)
    key = PBKDF2(passphrase, salt, dkLen=32, count=65536)
    return base64.b64encode(key)


def encrypt(key, payload):
    decoded_key = base64.b64decode(key)

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(decoded_key, AES.MODE_CBC, iv)

    payload = pad(payload)
    cipher_text = cipher.encrypt(payload)

    return base64.b64encode(iv), base64.b64encode(cipher_text)


def decrypt(key, iv, ciper_text):
    decoded_key = base64.b64decode(key)
    decoded_iv = base64.b64decode(iv)
    decoded_cipher_text = base64.b64decode(ciper_text)

    cipher = AES.new(decoded_key, AES.MODE_CBC, decoded_iv)

    clear_text = cipher.decrypt(decoded_cipher_text)
    clear_text = unpad(clear_text.decode())

    return clear_text


# PKCS#7
def pad(secret):
    return secret + (AES.block_size - len(secret) % AES.block_size) \
                    * chr(AES.block_size - len(secret) % AES.block_size)


def unpad(byte_string):
    return byte_string[:-ord(byte_string[-1])]
