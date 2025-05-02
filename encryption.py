import hashlib
import os
import base64
from dotenv import load_dotenv, set_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.backends import default_backend


load_dotenv()


def get_create_aes_key() -> bytes:
    key = os.getenv("Encryption_Key")
    if key:
        return base64.b64decode(key.encode())
    
    new_key = os.urandom(32)
    set_key(".env", "Encryption_Key", base64.b64encode(new_key).decode())
    return new_key

def hash_pass(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def encrypt(data: str, password: str) -> str:
    key = get_create_aes_key()
    iv = os.urandom(16)
    
    pad = padding.PKCS7(128).padder()
    padded_data = pad.update(data.encode()) + pad.finalize()
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encrypt = cipher.encryptor()
    cipher_text = encrypt.update(padded_data) + encrypt.finalize()
    
    final_result = base64.b64encode(iv + cipher_text).decode()
    
    pass_hash = hash_pass(password)
    return pass_hash + final_result

def decrypt(encoded_data: str, password: str) -> str:
    try:
        input_pass = hash_pass(password)
        embedded_hash = encoded_data[:64]
        encrypted = encoded_data[64:]
        
        if input_pass != embedded_hash:
            return "[Access denied: invalid credentials or corrupted data]"

        encoded_raw = base64.b64decode(encrypted.encode())
        iv = encoded_raw[:16]
        ciphertext = encoded_raw[16:]
        
        key = get_create_aes_key()
        
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decrypt = cipher.decryptor()
        plaintext_with_pad = decrypt.update(ciphertext) + decrypt.finalize()

        unpad = padding.PKCS7(128).unpadder()
        plaintext = unpad.update(plaintext_with_pad) + unpad.finalize()
        return plaintext.decode()
    except Exception:
        return "[Decryption failed — corrupted data or wrong key]"
    

#test
if __name__ == "__main__":
    test_msg = input("Enter the message:")
    password = input("Enter the Password: ")
    
    enc_msg = encrypt(test_msg, password)
    print(f"Encrypted message: {enc_msg}")
    
    print("#"*50)
    
    print("Decryption process....")
    input_pass = input("Enter the Password: ")
    dec_msg = decrypt(enc_msg, input_pass)
    print(f"Decrypted message: {dec_msg}")
