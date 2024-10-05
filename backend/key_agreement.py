# This file implements the X3DH (Extended Triple Diffie-Hellman) Protocol using the x3dh library in Python
import x3dh
import requests
import json
import os
import base64
from cryptography.hazmat.primitives.asymmetric import ed25519, x25519, padding
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
            'identity_key': base64.b64encode(bundle.identity_key).decode('utf-8'),
            'signed_pre_key': base64.b64encode(bundle.signed_pre_key).decode('utf-8'),
            'signed_pre_key_sig': base64.b64encode(bundle.signed_pre_key_sig).decode('utf-8'),
            'pre_keys': [base64.b64encode(key).decode('utf-8') for key in bundle.pre_keys]
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
def generate_identity_key():
    # Generate a new Ed25519 private key for the identity key
    identity_private_key = ed25519.Ed25519PrivateKey.generate()
    identity_public_key = identity_private_key.public_key()

    return identity_private_key, identity_public_key  # Keep it as the public key object


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
    signature = identity_private_key.sign(public_bytes)

    # Get current timestamp
    timestamp = int(time.time())

    # Return signed prekey pair
    return signed_prekey_priv, signature, public_bytes, timestamp

# Generates set of one-time prekeys 
def generate_otp(num_keys):
    prekeys = []
    for i in range(num_keys):
        pair = x25519.X25519PrivateKey.generate()
        private_key = pair.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key = pair.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        prekeys.append((private_key, public_key))
    return prekeys

# Checks the validity of the signed prekey against the identity public key 
def verify_signed_prekey(identity_public_key, signed_prekey_public_bytes, signature):
    try:
        identity_public_key.verify(
            signature,
            signed_prekey_public_bytes
        )
        
        # Return true if signature is valid
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False 

if __name__ == '__main__':
    # Generate identity key pair 
    b_identity_private, b_identity_public = generate_identity_key()

    # Generate signed prekey 
    b_signed_prekey_priv, b_signed_prekey_sig, b_signed_prekey_pub, timestamp = generate_signed_prekey(b_identity_private)

    # Verify signature of signed prekey
    if verify_signed_prekey(b_identity_public, b_signed_prekey_pub, b_signed_prekey_sig):
        # Generate one-time prekeys
        b_one_time_prekeys = generate_otp(num_keys=5)

        # Create bundle 
        custom_state = Custom_State()
        bundle = x3dh.Bundle(
            identity_key=custom_state._encode_public_key(x3dh.IdentityKeyFormat.ED_25519, b_identity_public.public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw
            )),
            signed_pre_key=b_signed_prekey_pub,
            signed_pre_key_sig=b_signed_prekey_sig,
            pre_keys=[key[1] for key in b_one_time_prekeys]
        )
        custom_state._publish_bundle(bundle)
        print('meow')
    else:
        exit(1)
