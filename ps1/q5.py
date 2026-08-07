from tcfunctions import transposition_encrypt

key = "nick"
plaintext = "Krishna Ranjan"
ciphertext = transposition_encrypt(plaintext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")