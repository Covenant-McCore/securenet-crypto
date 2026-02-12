from flask import Flask, request, jsonify
from phe import paillier

app = Flask(__name__)

# Generate homomorphic keypair
public_key, private_key = paillier.generate_paillier_keypair()

@app.route('/process', methods=['POST'])
def process_data():
    encrypted_number = request.json['ciphertext']
    print("Server received encrypted data")
    print("Processing encrypted computation...")

    encrypted_result = encrypted_number + public_key.encrypt(10)

    return jsonify({'ciphertext': encrypted_result})

if __name__ == '__main__':
    print("Server running on http://127.0.0.1:5000")
    app.run()

