from typing import Any

var1 = "Some data"

var2 = 123


def func(var1 : str, var2: int) -> tuple:

    additional = []
    additional.append(var1)
    additional.append(var2)
    return tuple(additional)

def addition(var_1:Any, var_2:Any) -> int:
    return var_1 + var_2

def substact(first:int, second: list) -> int :
    result = first
    for i in second:
        result -= i
    return result


if __name__ == "__main__":

    result = func("first", "second")
    print(result)
    print(var1)
