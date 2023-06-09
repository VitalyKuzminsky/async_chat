from threading import Thread, Lock
import time


done = Lock()


def idle_release():
    print("Running release!")
    time.sleep(5)
    done.release()


done.acquire()
Thread(target=idle_release).start()
done.acquire()
print("Странное поведение мьютексов в Python...")
