# function that calculate fibonachi
cache = {}

def fibonachi(n):
    if n < 2:
        return n
    elif cache.get(n):
        return cache[n]
    else:
        cache[n] = fibonachi(n-1) + fibonachi(n-2)
        return cache[n]

print(fibonachi(50))
