from threading import Thread


def simple_worker():
    print('hello')


if __name__ == '__main__':
    t1 = Thread(target=simple_worker)
    t1.start()

    print(t1.name)
    print(t1.ident)
    print(t1.is_alive())
