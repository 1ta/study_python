cache = {}

def fibnacci(n):
    global cache
    if n == 1:
        return 0
    if n == 2:
        return 1
    if cache.get(n):
        return cache[n]
    fibnacci_n = fibnacci(n-1) + fibnacci(n-2)
    cache[n] = fibnacci_n
    return fibnacci_n

print(fibnacci(30))
print(cache)
