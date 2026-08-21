# Transposition Cipher functions

import math


def get_decryption_key(encryption_key):
    mapping = { position: index+1  for index, position in enumerate(encryption_key)}
    decryption_key = [mapping[i] for i in range(1,len(mapping)+1)]

    return decryption_key

def get_encryption_key(key:str):
    indexed_key = list(enumerate(key.upper()))
    sorted_key = sorted(indexed_key, key=lambda x: x[1])
    indices = [0] * len(key)
    for order, (index, _) in enumerate(sorted_key):
        indices[index] = order + 1
    return tuple(indices)


def transposition_encrypt(input_text:str, key:tuple):
    if key == "" or input_text == "":
        return "Invalid input: key and plaintext cannot be empty"

    pad_char = "_"
    num_rows = math.ceil(len(input_text) / len(key))
    padded_text = input_text.ljust(num_rows * len(key), pad_char)
    
    matrix = [padded_text[i:i+len(key)] for i in range(0, len(padded_text), len(key))]

    output_text = ""
    for column in key:
        col_index = column - 1
        column_chars = [matrix[row][col_index] for row in range(num_rows)]
        output_text += ''.join(column_chars)

    return output_text


def get_key_order(key):
    indexed_key = list(enumerate(key))
    sorted_key = sorted(indexed_key, key=lambda x: x[1])
    indices = [0] * len(key)
    for order, (index, _) in enumerate(sorted_key):
        indices[index] = order + 1
    return tuple(indices)


def transposition_decrypt(
    ciphertext: str,
    key: tuple,
    strip_padding: bool = True,
):
    if not key or not ciphertext:
        return "Invalid input: key and ciphertext cannot be empty"
    
    num_rows = len(ciphertext) // len(key)
    matrix = [['_' for _ in range(len(key))] for _ in range(num_rows)]
    
    for chunk_index, order in enumerate(key):
        column = order - 1
        start = chunk_index * num_rows
        end = start + num_rows
        column_chars = ciphertext[start:end]
        for row in range(num_rows):
            matrix[row][column] = column_chars[row]
    
    plaintext = ''.join(''.join(row) for row in matrix)
    return plaintext.rstrip("_") if strip_padding else plaintext



def double_transposition_encrypt(plaintext:str, key1:tuple, key2:tuple):
    first_encryption = transposition_encrypt(plaintext, key1)
    second_encryption = transposition_encrypt(first_encryption, key2)
    return second_encryption


def double_transposition_decrypt(ciphertext:str, key1:tuple, key2:tuple):
    first_decryption = transposition_decrypt(
        ciphertext,
        key2,
        strip_padding=False,
    )
    second_decryption = transposition_decrypt(
        first_decryption,
        key1,
        strip_padding=True,
    )
    return second_decryption