def a(n):
    if n == 0:
        return 0
    return n + a(n-1)


print(a(3))