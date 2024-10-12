from flask import Flask, request, jsonify
import json
import os
from auth import create_conn, create_users_table
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

app = Flask(__name__)

# AES-256 encryption setup
def generate_aes_key():
    return os.urandom(32)  # 32 bytes = 256 bits

def encrypt_data(key, plaintext):
    iv = os.urandom(16)  # 16 bytes for AES block size
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the plaintext to be a multiple of the block size (16 bytes)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Return IV + ciphertext as base64 to store it securely
    return base64.b64encode(iv + ciphertext).decode()

def decrypt_data(key, encrypted_data):
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()

@app.route('/publish_bundle', methods=['POST'])
def publish_bundle():
    data = request.get_json()

    if data:
        # Extract the keys from the received JSON
        identity_key = data.get('identity_key')
        signed_pre_key = data.get('signed_pre_key')
        signed_pre_key_sig = data.get('signed_pre_key_sig')
        pre_keys = data.get('pre_keys')

        # Bundle the data (you can use your x3dh library)
        bundle = {
            'identity_key': identity_key,
            'signed_pre_key': signed_pre_key,
            'signed_pre_key_sig': signed_pre_key_sig,
            'pre_keys': pre_keys
        }

        # Encrypt the bundle using AES-256 before saving it
        aes_key = generate_aes_key()
        encrypted_bundle = encrypt_data(aes_key, json.dumps(bundle))

        # Save the encrypted bundle to a file (you can store the AES key securely elsewhere)
        file_path = '../data/keys.json'
        with open(file_path, 'a') as f:
            f.write(encrypted_bundle + '\n')

        return jsonify({"message": "Bundle received and encrypted successfully!"}), 200
    else:
        return jsonify({"error": "Invalid data!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
