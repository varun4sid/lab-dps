from tcfunctions import get_decryption_key

ekey = (3,2,6,1,5,4)
dkey = get_decryption_key(ekey)

print("Encryption Key: ", ekey)
print("Decryption Key: ", dkey)