# Transposition Cipher functions

def get_decryption_key(encryption_key):
    mapping = { position: index+1  for index, position in enumerate(encryption_key)}
    decryption_key = [mapping[i] for i in range(1,len(mapping)+1)]
    
    return decryption_key

def get_encryption_key(key):
    indexed_key = list(enumerate(key))
    sorted_key = sorted(indexed_key, key=lambda x: x[1])
    indices = [0] * len(key)
    for order, (index, _) in enumerate(sorted_key):
        indices[index] = order + 1
    return tuple(indices)


def transposition_encrypt(plaintext:str, key:str):
    if key == "" or plaintext == "":
        return "Invalid input: key and plaintext cannot be empty"
    
    plaintext = plaintext.replace(" ","_")
    matrix = [['_' for _ in range(len(key))] for _ in range((len(plaintext)) // len(key)+1)]
    
    for i in range(len(plaintext)):
        x = i // len(key)
        y = i % len(key)
        matrix[x][y] = plaintext[i]
    
    ciphertext = []
    for i in range(len(key)):
        column = key.index(i+1)
        for row in matrix:
            ciphertext += row[column]

    return ''.join(ciphertext)


def transposition_decrypt(ciphertext:str, key:str):
    if key == "" or ciphertext == "":
        return "Invalid input: key and ciphertext cannot be empty"
    
    order = get_encryption_key(key)
    num_rows = len(ciphertext) // len(key)
    matrix = [['_' for _ in range(len(key))] for _ in range(num_rows)]
    
    index = 0
    for i in range(len(key)):
        column = order.index(i+1)
        for row in range(num_rows):
            matrix[row][column] = ciphertext[index]
            index += 1
    
    plaintext = []
    for row in matrix:
        plaintext += row

    return ''.join(plaintext).replace("_", " ")