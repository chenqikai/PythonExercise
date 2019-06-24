"""
为什么进行异常捕获
    程序运行时如果出现非法输入程序崩溃
    进行异常捕获在一定程度避免程序崩溃
    输入a, b 输出 a/b
"""
# try:
#     pass
# except DeprecationWarning as e:
#     pass
# finally:
#     pass

a = input("请输入第一个数")
try:
    a = int(a)
    b = input("请输入第二个数")
    try:
        b = int(b)
        try:
            c = a / b
            print("结果为", c)
        except ZeroDivisionError as e:
            print(e)
    except ValueError as e:
        print(e)
except ValueError as e:
    print(e)

print("finish")
