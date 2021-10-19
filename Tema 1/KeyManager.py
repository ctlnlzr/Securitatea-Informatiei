import utility
from Crypto.Random import get_random_bytes


def generate_key(encryption_type):
    initial_key = get_random_bytes(16)
    aes = utility.getAES(encryption_type, utility.initial_key)
    return aes.encrypt(initial_key)