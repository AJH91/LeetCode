def climbStairs(n):
    if n <= 2:
        return n

    a = 0
    b = 1
    c = 2

    while (n > 2):
        a = b
        b = c
        c = a + b
        n = n - 1

    return c



