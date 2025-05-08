import hashlib
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import base64
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.backends import default_backend
from config import ENV_FILE_PATH

load_dotenv(ENV_FILE_PATH)

class crypto:
    @staticmethod
    def __get_aes_key():
        key = os.getenv("Encryption_Key")
        if key:
            return base64.b64decode(key.encode())
        return None

    @staticmethod
    def hash_pass(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def encrypt(message: str) -> str:
        try:
            key = crypto.__get_aes_key()
            iv = os.urandom(16)
            
            pad = padding.PKCS7(128).padder()
            padded_data = pad.update(message.encode()) + pad.finalize()
            
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encrypt = cipher.encryptor()
            cipher_text = encrypt.update(padded_data) + encrypt.finalize()
            
            final_result = base64.b64encode(iv + cipher_text).decode()
            
            return final_result
        except:
            return None

    @staticmethod
    def decrypt(encoded_message: str):
        try:
            encoded_raw = base64.b64decode(encoded_message.encode())
            iv = encoded_raw[:16]
            ciphertext = encoded_raw[16:]
            
            key = crypto.__get_aes_key()
            
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decrypt = cipher.decryptor()
            plaintext_with_pad = decrypt.update(ciphertext) + decrypt.finalize()

            unpad = padding.PKCS7(128).unpadder()
            plaintext = unpad.update(plaintext_with_pad) + unpad.finalize()
            return plaintext.decode()
        except Exception:
            return None
    