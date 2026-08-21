from tcfunctions import get_encryption_key, transposition_decrypt, transposition_encrypt

key1 = get_encryption_key("nick")
key2 = get_encryption_key("boat")
plaintext = "Krishna Ranjan"
ciphertext = transposition_encrypt(plaintext, key1)
decrypted_text = transposition_decrypt(ciphertext, key1)



print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")