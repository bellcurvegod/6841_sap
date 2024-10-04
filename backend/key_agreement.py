# This file implements the X3DH (Extended Triple Diffie-Hellman) Protocol using the x3dh library in Python

# from cryptography import X
import x3dh
import requests
import json
import os
import base64
from cryptography.hazmat.primitives.asymmetric import x25519, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import time

import x3dh.identity_key_pair

# Initialise subclass that's inherited from x3dh.state.State
class Custom_State(x3dh.state.State):
    def __init__(self):
        super(Custom_State, self).__init__()

    # Override _publish_bundle() methods
    def _publish_bundle(self, bundle: x3dh.Bundle) -> None:
        bundle_data = {
            'identity_key': bundle.identity_key.decode('utf-8'),
            'signed_pre_key': bundle.signed_pre_key.decode('utf-8'),
            'signed_pre_key_sig': bundle.signed_pre_key_sig.decode('utf-8'),
            'pre_keys': [key.decode('utf-8') for key in bundle.pre_keys]
        }

        # Post bundle to Flask server 
        response = requests.post('http://127.0.0.1:5000/publish_bundle', json=bundle_data)

        if response.status_code == 200:
            print('Successfully published bundle to server')
        else:
            print(f'Failed to publish bundle: {response.json()}')
    
    # Override _encode_public_key() methods
    def _encode_public_key(self, key_format, pub: bytes) -> bytes:
        if key_format == x3dh.IdentityKeyFormat.CURVE_25519:
            return base64.b64encode(pub)
        elif key_format == x3dh.IdentityKeyFormat.ED_25519:
            return base64.b64encode(pub)
        else:
            raise ValueError(f"Unsupported key format: {key_format}")


# Generates an identity key pair 
# def generate_identity_key()

# Generates a signed prekey pair that will be changed periodically
def generate_signed_prekey(identity_private_key):
    # Generate new X25519 private key for the signed prekey pair
    signed_prekey_priv = x25519.X25519PrivateKey.generate()
    signed_prekey_public = signed_prekey_priv.public_key()

    # Encode public key to bytes 
    public_bytes = signed_prekey_public.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )

    # Sign public key using the identity private key
    signature = identity_private_key.sign(
        public_bytes,
        padding=padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        algorithm=hashes.SHA256()
    )

    # Get current timestamp
    timestamp = int(time.time())

    # Return signed prekey pair
    return signed_prekey_priv, signature, public_bytes, timestamp

# Generates a one-time prekey pair used in a single X3DH run
def generate_otp():
    private_key = x25519.X25519PrivateKey.generate()
    public_key = private_key.public_key()

    return private_key, public_key

# Checks the validity of the signed prekey against the identity public key 
def verify_signed_prekey(identity_public_key, signed_prekey_public_bytes, signature):
    try:
        identity_public_key.verify(
            signature, 
            signed_prekey_public_bytes, 
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        algorithm=hashes.SHA256()
        
        # Return true if signature is valid
        return True
    except Exception:
        print(f"Verification failed: {Exception}")
        return False 

# Main execution of x3dh protocol
if __name__ == '__main__':

    # Generate random 32-byte seed 
    random_seed = os.urandom(32)

    # Create Bob's Identity Key Pair using the random seed
    b_identity_key_pair = x3dh.identity_key_pair.IdentityKeyPairSeed(seed=random_seed)

    # Access Bob's public and private keys 
    b_private_key = b_identity_key_pair.secret
    b_public_key = b_identity_key_pair.as_priv().priv





    # Create Bob's signed prekey 




# print(b_private_key, b_public_key)
# key_format = x3dh.IdentityKeyFormat.ED_25519
# public_key = b'111111111'  
# custom_state = Custom_State()
# encoded_key = custom_state._encode_public_key(key_format, public_key)
# 
# custom_state._publish_bundle(b_bundle)


# Step 1: Bob publishes keys (uploads bundle of keys, IKB, signed prekey, set of OTPs to server)
# Step 2: Alice fetches Bob's prekey bundle, verifies prekey signature, sends init message to Bob
# Step 3: Bob retrieves Alice's keys, repeats DH calculations, decrypts init ciphertext
