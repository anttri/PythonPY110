def pow_gen(base: int):
      # TODO записать функцию-генератор
    for i in range(base):
        yield i

if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(10):
        print(next(pow_numbers))
