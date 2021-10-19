"""
A - cel care initiaza comunicarea
"""
import KeyManager
import utility


def talk_with_b(queue_to_write, queue_to_read, encryption_type):
    queue_to_write.put(encryption_type)
    key = KeyManager.generate_key(encryption_type)
    queue_to_write.put(key)

    aes = utility.getAES(encryption_type, utility.decrypt_key(key, encryption_type))

    can_sent_message = queue_to_read.get()
    print("Should start sending messages? " + can_sent_message)

    with open("initial_file", "r") as f:
        while True:
            current_message = f.read(128)
            queue_to_write.put(aes.encrypt((current_message.ljust(128, '\0')).encode()))
            if len(current_message) < 128:
                queue_to_write.put("stop")
                break
    queue_to_write.close()


