def count(start_number: float = 1, step: float = 1):
    # TODO написать функцию-генератор возвращающую целые числа
    for i in range(start_number):
        for n in range(step):
            yield n ** 2 + step



if __name__ == "__main__":
    my_count = count(10, 0.5)
    for _ in range(10):
        print(next(my_count))
