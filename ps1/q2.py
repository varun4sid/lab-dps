from ps1.scfunctions import additive_cipher_decrypt

DOMAIN = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
ciphertext = "NCJAEZRCLASJLYODEPRLYZRCLASJLCPEHZDTOPDZQLNZTY"

for key in DOMAIN:
    decrypted_text = additive_cipher_decrypt(ciphertext, key)
    print(f"Key {key}: {decrypted_text}")
    
print("The decrypted text with key 11 is meaningful : ",
      additive_cipher_decrypt(ciphertext, 11))