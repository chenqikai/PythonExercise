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
