b = 33
k = 2
cache = {0:0, 1:1}

def fib(n, k):
    cache = {0:0, 1:1}
    if n in cache: return cache[n]
    cache[n] = fib(n - 1, k) + k * fib(n - 2, k)
    return cache[n]

print(fib(33,2))