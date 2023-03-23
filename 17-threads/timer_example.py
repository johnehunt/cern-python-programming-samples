from threading import Timer


def hello():
    print('hello')

if __name__ == '__main__':
    print('Starting')
    t = Timer(5, hello)
    t.start()

    print('Done')
