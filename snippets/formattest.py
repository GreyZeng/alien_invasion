#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数
print('Hello, %s' % 'world')


print('Hi, %s, you have $%d.'%('Mike',100))


# %s永远起作用，它会把任何数据类型转换为字符串：

print('Age : %s, Gender :%s' % (24,True))

print('growth rate: %d %%' % 7)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))


r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')


print('中文'.encode('gb2312'))
