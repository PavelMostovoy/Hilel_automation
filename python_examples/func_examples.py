def func(var1, var2, var3=0):
    return var1 + var2 + var3


print(func(1, 2, var3=4))


def func_1(a, b, /, var1, var2, *args, var3=0, **kwargs):
    print(a, b)
    return var1 + var2 + var3


print(func_1(1, 3, var1=1, var2=2, var7=4, var3=7))


def func_2(*, var1=0, var2=0, var3=0, ):
    return var1 + var2 + var3


print(func_2(var1=1, var2=2, var3=3))
