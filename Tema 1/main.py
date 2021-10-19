import A
import B
import multiprocessing

if __name__ == '__main__':
    encryption_type = input("Introduceti tipul de encriptare: ")
    if encryption_type != "ECB" and encryption_type != "CBC":
        encryption_type = "ECB"

    queue_a_to_b = multiprocessing.Queue()
    queue_b_to_a = multiprocessing.Queue()
    p = multiprocessing.Process(target=A.talk_with_b, args=(queue_a_to_b, queue_b_to_a, encryption_type,))
    q = multiprocessing.Process(target=B.talk_with_a, args=(queue_b_to_a, queue_a_to_b,))
    p.start()
    q.start()
