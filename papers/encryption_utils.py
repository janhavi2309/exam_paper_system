from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

BLOCK_SIZE = 16  # AES block size

def pad(data):
    padding = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding]) * padding

def unpad(data):
    return data[:-data[-1]]

def encrypt_file(file_data):
    key = get_random_bytes(32)  # AES 256 key
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(file_data))
    return cipher.iv + ct_bytes, key

def decrypt_file(enc_data, key):
    iv = enc_data[:16]
    ct = enc_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct))
