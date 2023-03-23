from multiprocessing import Process, set_start_method
from time import sleep
import os


def worker(msg):
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    for _ in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)


if __name__ == '__main__':
    print('Starting')
    print('Root application process id:', os.getpid())
    set_start_method('spawn')
    t = Process(target=worker, args='A')
    t.start()
    print('Done')
