# -*- coding: utf-8 -*-
print('包含中文的str')

print(len('中文'))

# “中” 字
str = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(str)

# 6
print(len('中文'.encode('utf-8')))