import requests
from phe import paillier

print("=== CLIENT EXECUTION STARTED ===")

public_key, private_key = paillier.generate_paillier_keypair()

plaintext = 5
encrypted_payload = public_key.encrypt(plaintext)

print("Encrypted payload sent to server:")
print(encrypted_payload.ciphertext())

response = requests.post(
    "http://127.0.0.1:5000/process",
    json={'ciphertext': encrypted_payload}
)

encrypted_result = response.json()['ciphertext']

print("\nEncrypted result returned:")
print(encrypted_result)

print("\n=== CLIENT EXECUTION COMPLETED ===")

