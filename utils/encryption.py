# utils/encryption.py
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.asymmetric import x25519
import os

class SecureComms:
    def __init__(self):
        pass
    
    def encrypt_message(self, message: bytes, key: bytes) -> bytes:
        """Cifra mensaje con ChaCha20-Poly1305"""
        pass
