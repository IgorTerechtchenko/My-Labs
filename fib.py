def generate_fib(n): #here i assume that sequence starts with 0
    if n == 1:
        return 1
    if n == 0:
        return 0
    else: 
        return generate_fib(n-1) + generate_fib(n-2)

def generate_fib_sequence(n):
    for x in range(n):
        yield generate_fib(x)

for x in generate_fib_sequence(10):
    print x
