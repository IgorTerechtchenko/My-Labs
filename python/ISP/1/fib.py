def generate_fib_sequence(n):
    a = 0
    b = 1
    for x in range(n):
        a = a + b
        temp = a
        a = b
        b = temp
        yield a
