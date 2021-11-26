def task() -> list:
    temp_tuple = (0, 36.6, 100)
    n = []
    for n in temp_tuple:
        (temp_tuple * 9 / 5) + 32

        return n   # TODO  вернуть список температур по Фаренгейту


if __name__ == "__main__":
    print(task())
