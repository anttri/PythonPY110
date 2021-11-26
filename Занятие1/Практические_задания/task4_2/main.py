from itertools import count

#def foo(i):
#    return i ** 2

def task():
    iterator_numbers = count(1, 1)
    #numbers = (i ** 2 for i in iterator_numbers if i % 2 == 0)  # TODO заменить на map и filter
    map(lambda i: i**2, iterator_numbers)
    numbers = (i ** 2 for i in iterator_numbers if i % 2 == 0)

    for _ in range(10):  # TODO напечатать первые 10 чисел
        print(next(numbers))  # TODO с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()
