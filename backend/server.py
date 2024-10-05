# This file contains the implementation of the backend server that stores the keys 
from flask import Flask, request, jsonify
import json
import os
from cryptography.fernet import Fernet
from x3dh import Bundle  

app = Flask(__name__)

@app.route('/publish_bundle', methods=['POST'])
def publish_bundle():
    data = request.get_json()

    if data:
        # Extract data from the received JSON
        identity_key = data.get('identity_key')
        signed_pre_key = data.get('signed_pre_key')
        signed_pre_key_sig = data.get('signed_pre_key_sig')
        pre_keys = data.get('pre_keys')

        # Create the Bundle instance
        bundle = Bundle(identity_key, signed_pre_key, signed_pre_key_sig, pre_keys)

        # Process the bundle (e.g., save it or validate it)
        return jsonify({"message": "Bundle received successfully!"}), 200
    else:
        return jsonify({"error": "Invalid data!"}), 400   

if __name__ == '__main__':
    app.run(debug=True)
    keys = {
        "publicKey": "abcd1234",
        "privateKey": "efgh5678"
    }

    curr_dir = os.getcwd()
    file_path = '../data/keys.json'

    with open(file_path, 'a') as f:
        for key, value in keys.items():
            f.write(f'{key}:{value}\n')
