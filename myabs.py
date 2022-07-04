def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

r = move(100, 100, 60, math.pi / 6)

print(r)


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(3))
print(power(2,4))

# 注意两个方法的区别
def add_end1(L=[]):
    L.append('END')
    return L
print(add_end1())
print(add_end1())
print(add_end1())
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end2([1,2,3]))
print(add_end2([1,2,3]))