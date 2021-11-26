from traceback import print_exc


def second_gen(input_):
    #  step one
    yield input_  # step two
    input_ += 1

    yield input_  # step three
    input_ += 1

    return input_  # step four



if __name__ == "__main__":
    my_second_gen = second_gen(10)
    #  step one

    print(next(my_second_gen))  # 10
    #  step two
    print(next(my_second_gen))  # 11
    #  step three
    try:
        print(next(my_second_gen))
        # step four
    except StopIteration as e:
        print("Генератор закончился", e)
        print_exc()
