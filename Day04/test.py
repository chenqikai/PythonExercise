import random

print(random.randrange(10, 100))
# 第一个datetime 代表文件夹 第二个代表文件
from datetime import datetime

print(datetime.now())
# 引入自己的模块
from Day04 import 面向对象1
from Day04 import PEP8 as p

p.my_fun()
print(p.__doc__)  # __doc__可以获取模块说明
print(help(p))
print(dir(p))  # 以列表的形式 展示模块中拥有的内容

print(dict(p.d1))

if hasattr(p, "Temp"):
    print("有")
else:
    print("没有")

"""
Python 中一切皆对象
模块也可以看作一个对象
    模块中定义的变量可以成为属性名 变量的值称为属性值
    函数名可以称为属性名 函数具体内容称为属性值
    类名可以称为属性名 类内容可以称为属性值
"""
