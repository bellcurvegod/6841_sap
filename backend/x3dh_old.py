# This file implements the X3DH (Extended Triple Diffie-Hellman) Protocol 

from cryptography.hazmat.primitives.asymmetric import ed25519, x25519
from cryptography.hazmat.primitives import serialization

class User(object):
    def __init__(self, name, max_opk_num=10):
        self.name = name

        # Define long-term identity key pair (IKs)
        self.IK_s = x25519.X25519PrivateKey.generate()  
        self.IK_p = self.IK_s.public_key()

        # Define signed prekey pair (SPKs)
        self.SPK_s = x25519.X25519PrivateKey.generate()  
        self.SPK_p = self.SPK_s.public_key()

        # Ed25519 key pair for signing
        self.ED_s = ed25519.Ed25519PrivateKey.generate()
        self.ED_p = self.ED_s.public_key()

        # Sign SPK public key
        self.SPK_sig = self.ED_s.sign(self.SPK_p.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        ))

        # Define one time prekeys (OPKs) 
        self.OPK_s = []
        self.OPK_p = []

        # Generate OPKs 
        for i in range(max_opk_num):
            sk = x25519.X25519PrivateKey.generate()
            pk = sk.public_key()
            self.OPK_p.append(pk)
            self.OPK_s.append((sk, pk))

            # Later steps
            self.key_bundles = {}
            self.dr_keys = {}

        # Define public keys for each user to store their key bundles 

    # Return user's key bundle (IK_p, SPK_p, SPK_sig, OPKs)
    def publish(self):
        return {
            'IK_p': self.IK_p,
            'SPK_p': self.SPK_p,
            'SPK_sig': self.SPK_sig,
            'OPKs_p': self.OPKs_p
        }

    def get_key_bundle(self, server, user_name):
        if user_name in self.key_bundles and user_name in self.dr_keys:
            print('Already stored ' + user_name + ' locally, no need handshake again')
            return False

    def init_handshake(self, server, user_name):
       
        return

    
user1 = User(name="Alice")

print(user1.name, user1.SPK_sig) 