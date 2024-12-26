from typing import Union


def logger(func):
    def wrapper(*args):
        print(f"Начало работы функции: {func.__name__}")
        import time
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        result_time = end_time - start_time
        print(f"Окончание работы функции: {func.__name__}, время выполнения: {result_time}")
        return result

    return wrapper


@logger
def summ(*args) -> Union[int, float]:
    # def summ(*args) :
    result = 0
    for arg in args:
        if isinstance(arg, int) or isinstance(arg, float):
            result += arg
        # else: raise Exception.TypeError
    return result


if __name__ == '__main__':
    function = summ(1, 2, 3, 4.758654)
    print(function)
    # function = summ(1,2,3,4,5)
    # print(function)
    # print(summ(1,2,3,4,5,"Hello world"))
