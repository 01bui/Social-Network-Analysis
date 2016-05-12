def russian(a,b):
    """a * b = x * y + z"""
    x = a
    y = b
    z = 0
    count = 0
    while x > 0:
        if x == 7 and z == 84:
            print y
        if x % 2 == 1:
            z = z + y
            count += 1
        y = y << 1
        x = x >> 1
        print x,y,z
    return z, count

#print russian(20,7)
print russian(63,12)
