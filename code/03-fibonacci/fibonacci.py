from functools import lru_cache

def fibruim(n):
    print ('fibruim(%d)' %n)
    if n <= 2:
        return 1
    return fibruim(n-1) + fibruim(n-2)

@lru_cache(maxsize=None)
def fib(n):
    print ('fib(%d)' %n)
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)