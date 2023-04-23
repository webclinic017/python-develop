from multiprocessing import Process
from multiprocessing import Pool
import time
import os


def f(n):
    if (n <= 1):
        return 1
    else:
        return f(n - 1) + f(n - 2)


def t(i, n):
    print(i, os.getpid())
    print("   ", i, f(n))


if __name__ == '__main__':
    start_time = time.time()

    ps = Pool(10)
    for i in range(10):
        # print(i,f(35))
        # p = Process(target=t, args=(i,35,))
        # p.start()
        # ps.append(p)
        ps.apply_async(t, args=(i, 35,))

    ps.close()
    ps.join()
    '''for p in ps:
        p.start()
        p.join()'''

    end_time = time.time()
    print((int(end_time - start_time)) // 60, "min", (int(end_time - start_time)) % 60, "s")
