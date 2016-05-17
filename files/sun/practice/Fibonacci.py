

def cachify(old_f):
    cache = {}
    def new_f(n):
        r = cache.get(n)
        if r: return r
        r = old_f(n)
        cache[n] = r
        return r
    return new_f

@cachify
def f(n):
    if n < 2:
        return 1
    fn = f(n-1) + f(n-2)
    return fn

@cachify
def ff(n):
    if n < 2:
        return 1
    fn = ff(n-1) + ff(n-2) + ff(n-3) + ff(n-4)
    return fn


#f = cachify(f)

print(f(100))
