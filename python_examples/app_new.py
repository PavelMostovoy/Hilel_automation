from sandbox import func, addition, substact

second = [1, 4, 5, 3, 5]

data = (51, second)

var = func("str", 56)

print(addition("a", "b"))

print(substact(*data))
"""
many different imports 
"""
second[3] = "new_data"

print(substact(*data))

if __name__ == "__main__":
    print(var)
