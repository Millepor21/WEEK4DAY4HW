def memoize_decorator(f):
    cache = {}
    def inner(inp):
        if (inp) not in cache:
            cache[inp] = f(inp)
        return cache[inp]
    return inner

def fib2(n):
    if n <= 1:
        return 1
    return fib2(n-1) + fib2(n-2)

@memoize_decorator
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(50))

print(fib2(35))