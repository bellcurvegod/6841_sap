    # Generate random 32-byte seed 
    # random_seed = os.urandom(32)

    # # Create Bob's Identity Key Pair using the random seed
    # b_identity_key_pair = x3dh.identity_key_pair.IdentityKeyPairSeed(seed=random_seed)

    # # Access Bob's public and private keys 
    # b_private_key = b_identity_key_pair.secret
    # b_public_key = b_identity_key_pair.as_priv().priv

    # 



    # Create Bob's signed prekey 


    # Create bundle
    # custom_state = Custom_State()
    # bundle = x3dh.Bundle(
    #     identity_key=custom_state._encode_public_key()
    # )
    # # Publish bundle to server
    # custom_state._publish_bundle(bundle)




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
