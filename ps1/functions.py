DOMAIN = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
a = ord('a')
z = ord('z')

def additive_cipher_encrypt(text, key):
    encrypted = ""
    
    for ch in text.lower():
        character = ord(ch)
        if a <= character <= z:
            index = a + (character + key - a) % 26
            encrypted += chr(index)
        else:
            encrypted += ch
    
    return encrypted


def additive_cipher_decrypt(text, key):
    decrypted = ""
    
    for ch in text:
        character = ord(ch)
        if a <= character <= z:
            index = a + (character - key - a) % 26
            decrypted += chr(index)
        else:
            decrypted += ch
    
    return decrypted


def multiplicative_cipher_encrypt(text, key):
    if 26 % key == 0 or key < 1 or key > 25:
        return "invalid key"
    
    encrypted = ""
    
    for ch in text.lower():
        character = ord(ch)
        if a <= character <= z:
            index = a + ((character - a) * key) % 26
            encrypted += chr(index)
        else:
            encrypted += ch
            
    return encrypted


def get_multiplicative_inverse(key):
    for i in DOMAIN:
        if key * i % 26 == 1:
            return i
    return None


def multiplicative_cipher_decrypt(text, key):
    decrypted = ""
    
    inverse_key = get_multiplicative_inverse(key)

    if inverse_key is None:
        return "invalid key"
    
    for ch in text:
        character = ord(ch)
        if a <= character <= z:
            index = a + ((character - a) * inverse_key) % 26
            decrypted += chr(index)
        else:
            decrypted += ch
    
    return decrypted


def affine_cipher_encrypt(text, k1, k2):
    encrypted = ""
    
    for ch in text.lower():
        character = ord(ch)
        if a <= character <= z:
            index = a + ((character - a) * k1 + k2) % 26
            encrypted += chr(index)
        else:
            encrypted += ch
            
    return encrypted


def affine_cipher_decrypt(text, k1, k2):
    decrypted = ""
    
    k1_inverse = get_multiplicative_inverse(k1)

    if k1_inverse is None:
        return "invalid key"
    
    for ch in text:
        character = ord(ch)
        if a <= character <= z:
            index = a + (((character - k2 - a) * k1_inverse) % 26)
            decrypted += chr(index)
        else:
            decrypted += ch
            
    return decrypted


def autokey_cipher_encrypt(text, key):
    encrypted = ""
    
    for ch in text.lower():
        character = ord(ch)
        if a <= character <= z:
            index = a + (character + key - a) % 26
            encrypted += chr(index)
            key = ord(ch) - a
        else:
            encrypted += ch
            
    return encrypted


def autokey_cipher_decrypt(text, key):
    decrypted = ""
    
    for ch in text.lower():
        character = ord(ch)
        if a <= character <= z:
            index = a + (character - key - a) % 26
            decrypted += chr(index)
            key = ord(decrypted[-1]) - a
        else:
            decrypted += ch
            
    return decrypted