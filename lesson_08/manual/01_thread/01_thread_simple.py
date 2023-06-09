# from threading import Thread
# import time
#
#
# def clock(interval):
#     while True:
#         print("Текущее время: %s" % time.ctime())
#         time.sleep(interval)
#
#
# t = Thread(target=clock, args=(15, ))
# t.daemon = True
# t.start()


# Тот же поток в виде класса.
from threading import Thread
import time


class ClockThread(Thread):
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval

    def run(self):
        while True:
            print("Текущее время: %s" % time.ctime())
            time.sleep(self.interval)


t = ClockThread(15)
t.start()
