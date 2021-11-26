def to_upper(word: str) -> str:
    return word.upper()


def task(words: list) -> list:
    return list(map(str.upper, words))
    #return [word.upper() for word in words]  # TODO перевести слова в верхний регистр c помощью map


if __name__ == "__main__":
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    print(task(list_words))
