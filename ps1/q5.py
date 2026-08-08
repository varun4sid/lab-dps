from tcfunctions import transposition_decrypt, transposition_encrypt, get_encryption_key

key = get_encryption_key("nick")
plaintext = "enemyattackstonight"
ciphertext = transposition_encrypt(plaintext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {transposition_decrypt(ciphertext, key)}")