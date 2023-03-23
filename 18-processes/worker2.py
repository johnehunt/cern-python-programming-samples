from multiprocessing import Process, set_start_method
from time import sleep
import os


def worker(msg):
    print(f'process id: {os.getpid()}')
    for _ in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)


if __name__ == '__main__':
    set_start_method('spawn')
    print('Starting')
    print(f'Root application process id: {os.getpid()}')

    t2 = Process(target=worker, args='A')
    t3 = Process(target=worker, args='B')
    t4 = Process(target=worker, args='C')

    t2.start()
    t3.start()
    t4.start()

    print('Done')
