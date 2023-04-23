import threading
import time


def Function(i, n, name):
    time.sleep(n)
    print(i, name)


class MyThread(threading.Thread):
    def __init__(self, interval=1, threadName="Default"):
        threading.Thread.__init__(self)
        self.interval = interval
        self.threadName = threadName

    def run(self):
        for i in range(10):
            Function(i, self.interval, self.threadName)


threads = []
for i in range(10):
    t = MyThread(interval=2 + i, threadName="{} thread".format(i))
    threads.append(t)

for t in threads:
    t.start()
