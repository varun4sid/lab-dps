from ps1.scfunctions import (
    additive_cipher_encrypt,
    additive_cipher_decrypt,
    multiplicative_cipher_encrypt,
    multiplicative_cipher_decrypt,
    affine_cipher_encrypt,
    affine_cipher_decrypt,
    autokey_cipher_encrypt,
    autokey_cipher_decrypt
)

text = "this is an exercise"
ace = additive_cipher_encrypt(text, 20)
acd = additive_cipher_decrypt(ace, 20)

mce = multiplicative_cipher_encrypt(text, 15)
mcd = multiplicative_cipher_decrypt(mce, 15)

affce = affine_cipher_encrypt(text, 15, 20)
affcd = affine_cipher_decrypt(affce, 15, 20)

autoce = autokey_cipher_encrypt(text, 7)
autocd = autokey_cipher_decrypt(autoce, 7)

print("Additive Cipher")
print(f"Encrypt({text}) = ", ace)
print(f"Decrypt({ace}) = ", acd)

print("Multiplicative Cipher")
print(f"Encrypt({text}) = ", mce)
print(f"Decrypt({mce}) = ", mcd)

print("Affine Cipher")
print(f"Encrypt({text}) = ", affce)
print(f"Decrypt({affce}) = ", affcd)

print("Autokey Cipher")
print(f"Encrypt({text}) = ", autoce)
print(f"Decrypt({autoce}) = ", autocd)