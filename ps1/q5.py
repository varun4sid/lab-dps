from tcfunctions import double_transposition_encrypt, get_encryption_key

key1 = get_encryption_key("nick")
key2 = get_encryption_key("boat")
plaintext = "enemyattackstonight"
ciphertext = double_transposition_encrypt(plaintext, key1, key2)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
