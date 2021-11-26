from traceback import print_exc


def int_not_iterable():
    int_number = 10
    try:
        iter(int_number)  # объект не является итерируемым объектом
    except TypeError:  # ожидаем ошибку TypeError: 'int' object is not iterable
        print_exc()


def list_not_iterator():
    list_ = [1, 2, 3]

    try:
        next(list_)
    except TypeError:  # ожидаем ошибку TypeError: 'list' object is not an iterator
        print_exc()


if __name__ == "__main__":
    l = [1, 2, 3]
    iter_l = iter(l)
    print(next(iter_l))
    print(next(iter_l))
    print(next(iter_l))
    print(next(iter_l))
    print(next(iter_l))
    int_not_iterable()
    list_not_iterator()

