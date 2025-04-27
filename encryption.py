from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.backends import default_backend
import os
import base64

def password_key(password: str, salt: bytes) -> bytes:
    gen = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return gen.derive(password.encode())

def encrypt(data: str, password: str) -> str:
    iv = os.urandom(16)
    salt = os.urandom(16)
    key = password_key(password, salt)
    
    pad = padding.PKCS7(128).padder()
    padded_data = pad.update(data.encode()) + pad.finalize()
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encrypt = cipher.encryptor()
    cipher_text = encrypt.update(padded_data) + encrypt.finalize()
    
    final_result = base64.b64encode(salt + iv + cipher_text).decode()
    return final_result

def decrypt(encoded_data: str, password: str) -> str:
    try:
        encoded_raw = base64.b64decode(encoded_data.encode())
        salt = encoded_raw[:16]
        iv = encoded_raw[16:32]
        ciphertext = encoded_raw[32:]
        key = password_key(password, salt)

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decrypt = cipher.decryptor()
        plaintext_with_pad = decrypt.update(ciphertext) + decrypt.finalize()

        unpad = padding.PKCS7(128).unpadder()
        plaintext = unpad.update(plaintext_with_pad) + unpad.finalize()
        return plaintext.decode()
    except Exception as error :
        return f"[Password is incorrect, Try enter it again]"
    


# if __name__ == "__main__":
    # password = input("Enter the Password: ")
    # test_msg = "hello world!!"
    # 
    # enc_msg = encrypt(test_msg, password)
    # print(f"Encrypted message: {enc_msg}")
    # 
    # dec_msg = decrypt(enc_msg, password)
    # print(f"Decrypted message: {dec_msg}")