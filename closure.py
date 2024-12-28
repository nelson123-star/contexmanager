"""
Замыкание - это функция, которая запоминает значения из объемлющей области видимости,
даже если эта область уже не существует.
Такая функция может сохранять доступ к этим значениям и использовать их при последующих вызовах.
"""


def all_names():
    all_names = []

    def inner(name_in: str)-> list:
        all_names.append(name_in)
        return all_names

    return inner


if __name__ == '__main__':
    persons = all_names()
    # print(persons("Дима"))
    # print(persons("Андрей"))
    # print(persons("Влад"))
    print(persons("Дима"))
