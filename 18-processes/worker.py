from multiprocessing import Process, freeze_support
from time import sleep

def worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)


if __name__ == '__main__':
    freeze_support()
    print('Starting')

    t2 = Process(target=worker, args='A')
    t3 = Process(target=worker, args='B')
    t4 = Process(target=worker, args='C')

    t2.start()
    t3.start()
    t4.start()

    print('Done')
