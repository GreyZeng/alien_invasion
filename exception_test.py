try:
    print(5/0)
except ZeroDivisionError:
    # 如果不处理异常，则可以写 pass
    print("Zero div error")