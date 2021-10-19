from Crypto.Cipher import AES

initial_key = b'F_dQcd2rg8FSRcsd'
initialize_vector = b'cfrdtE524RaY8IKH'


def decrypt_key(key, encryption_type):
    if encryption_type == "CBC":
        aes = AES.new(initial_key, AES.MODE_CBC, initialize_vector)
    else:
        aes = AES.new(initial_key, AES.MODE_ECB)
    return aes.decrypt(key)


def getAES(encryption_type, decrypted_key):
    if encryption_type == "CBC":
        aes = AES.new(decrypted_key, AES.MODE_CBC, initialize_vector)
    else:
        aes = AES.new(decrypted_key, AES.MODE_ECB)
    return aes
