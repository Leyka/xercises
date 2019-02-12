"""
Multiply 2 numbers without using * operator
"""

# recursive way
def multiply(x, y, accum=0):
    if y == 0:
        return accum
    y -= 1
    accum += x
    return multiply(x, y, accum)

assert(multiply(3, 4) == 12)
assert(multiply(-12, 12) == -144)

x = int(input('x: '))
y = int(input('y: '))
print('{} multiply by {} = {}'.format(x, y, multiply(x,y)))