"""
Swapping 2 numbers without temp variable, using XOR operation.

Ex. with x=3 and y=6 and we want x=6 and y=3
x=3 in base2 is 011 and y=6 in base2 is 110

step 1 : x = x XOR y (x=x^y)
x: 0 1 1
y: 1 1 0 
   -----
x: 1 0 1 = 5

step 2 : y = x XOR y
x: 1 0 1
y: 1 1 0 
   -----
y: 0 1 1 = 3

step 3 : repeat step 1 with new x and new y
x: 1 0 1
y: 0 1 1 
   -----
x: 1 1 0 = 6
"""

# swap 2 numbers with xor
def swap(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y 
    return x,y

assert(swap(456, 123) == (123, 456))
assert(swap(-3, 4) == (4,-3))

x = int(input('x: '))
y = int(input('y: '))
print('Before swap, x={} and y={}'.format(x, y))

x, y = swap(x,y)
print('After swap, x={} and y={}'.format(x, y))