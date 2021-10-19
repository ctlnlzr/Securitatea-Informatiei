"""
B - cel care primeste mesajele
"""
import utility


def talk_with_a(queue_to_write, queue_to_read):

    encrypting_mode = queue_to_read.get()
    print("The encrypting mode received from A is: " + encrypting_mode)

    encrypted_key = queue_to_read.get()

    aes = utility.getAES(encrypting_mode, utility.decrypt_key(encrypted_key, encrypting_mode))

    queue_to_write.put("y")
    queue_to_write.close()

    while True:
        message = queue_to_read.get()
        # print(message)
        if message == "stop":
            break
        decoded_message = aes.decrypt(message)
        print(decoded_message.decode().rstrip('\0'), end="")
    print("\nEnd of file")

