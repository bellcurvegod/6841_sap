from flask import Flask, request, jsonify
import x3dh
# from key_agreement import Bundle, Custom_State

app = Flask(__name__)

@app.route('/publish_bundle', methods=['POST'])

def publish_bundle():
    data = request.json

    if not data:
        return jsonify({'error': 'no data provided'}), 400
    
    try:
        identity_key = bytes(data['identity_key'], 'utf-8')
        signed_prekey = bytes(data['identity_key'], 'utf-8')
        signed_prekey_sig = bytes(data['identity_key'], 'utf-8')
        pre_keys = frozenset(bytes(key, 'utf-8') for key in data['pre_keys'])

        # Create Bundle instance 
        bundle = Bundle(identity_key, signed_prekey, signed_prekey_sig, pre_keys)
        print("Received bundle:", bundle)

        return jsonify({"message": "Bundle published successfully"}), 200

    # Return error if key is missing 
    except KeyError as key_error:
        return jsonify({'error': f'Missing key: {str(key_error)}'})
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)