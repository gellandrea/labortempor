def add(a, b):
    return a + b

# Each call to `add` is independent of the other
result1 = add(2, 3)  # result1 is 5
result2 = add(2, 3)  # result2 is also 5, independently of result1
