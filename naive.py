def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

print naive(2,3)
print naive(4,3)

# counting steps in naive as a function of a
def time(a):
    # The number of steps it takes to execute naive(a, b)
    # as a function of a
    steps = 0
    # your code here
    return steps
