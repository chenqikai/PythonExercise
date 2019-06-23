"""
函数 ：为了完成特定的工作，进行的代码封装
"""

# 计算 1 到 100 累加
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)


sum = 0
for i in range(1, 201):
    sum += i
print(sum)


def getsum(b):
    sum = 0
    for i in range(1, (b + 1)):
        sum += i
    return sum


# getsum = getsum(int(input("请输入想要计算的累加数：")))
# print(getsum)

# 可变列表参数
def my_fun1(h1, *args):
    print(type(args), args)
    print("Hello")


my_fun1("特朗普", "小布什")


# 可变字典参数
def my_fun2(a, *args, **kwargs):
    print(a)
    print(type(args), args)
    print(type(kwargs), kwargs)


my_fun2(100, 200, 300, 400, name="heda", address="kaifeng")
"""
参数

普通形参
带有默认值的参数
普通参数，可变元组形参
普通参数，可变元祖形参，可变字典形参
"""
"""
我是：name
我要告诉一下人员：*args
我要告诉他们河大的信息：**kwargs
"""


def tell(name, *args, **kwargs):
    print("我是：", name)
    print("我要告诉一下人员：")
    for i in args:
        print(i)
    print("我要告诉他们河大的信息：")
    for k, v in kwargs.items():
        print(k, v)


tell("chenqikai", '张三', '李四', '王五', message1="赶紧装空调", message2="赶紧")


