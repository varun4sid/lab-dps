# Transposition Cipher functions

def get_decryption_key(encryption_key):
    mapping = { position: index+1  for index, position in enumerate(encryption_key)}
    decryption_key = [mapping[i] for i in range(1,len(mapping)+1)]
    
    return decryption_key