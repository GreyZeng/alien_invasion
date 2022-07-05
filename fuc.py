def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 可变参数
print(calc(1, 3, 5, 7))
print(calc(1, 3, 5))
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
# number作为list或者tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum