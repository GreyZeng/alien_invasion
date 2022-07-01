a = 'ABC'
b = a
a = 'XYZ'
# 这里b依然输出是ABC
print(b)


# 精确
# 3.33333333

print(10/3)
# 3.0
print(9/3)
# 地板除
print(10//3)
print(7//3)

age = 7
if age >= 18:
    print('adult')
elif age >= 6:
    print('青少年')
else:
    print('kid')