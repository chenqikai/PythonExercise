"""
三引号多用于类，函数，模块注释
如果在.py文件的头部 代表文档注释
"""
import math

pi = math.pi


def my_fun():
    """
    my_sun()是一个可以打印hello world！的函数
    :return: 没有返回值
    """
    print("hello world!")


def my_add(a, b):
    """
    两个数相加的函数
    :param a: 第一个数
    :param b: 第二个数
    :return: 返回两个数之和
    """
    return a + b


d1 = {"name": "elicen", 'age': "20"}


class Temp:
    name = "elichen"

    def f(self):
        return "hello"
