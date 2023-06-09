import threading

produced = threading.Semaphore(0)
consumed = threading.Semaphore(1)


def producer():
    while True:
        consumed.acquire()
        produce_item()
        produced.release()

def consumer():
    while True:
        produced.acquire()
        item = get_item()
        consumed.release()
        