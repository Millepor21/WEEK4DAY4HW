count_calls = 0

def memoize_decorator(f):
    cache = {}
    def inner(inp):
        if (inp) not in cache:
            cache[inp] = f(inp)
        return cache[inp]
    return inner

def times_activated(f):
    def inner(n):
        global count_calls
        count_calls += 1
        return f(n)
    return inner

@memoize_decorator
@times_activated
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)    

print(fib(333))
print(count_calls)