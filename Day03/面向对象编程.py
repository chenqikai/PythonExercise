"""
一切皆是对象
将物理世界进行抽象
提取相应属性和相关操作
进行封装得到类
面向对象编程简单理解为类编程
"""


class Student:
    # name = "elichen"
    # age = 20

    def __init__(self, _name, _age, _addr):
        """
        添加构造函数
        :param name: 姓名
        :param age: 年龄
        """
        self.name = _name
        self.age = _age
        self.addr = _addr

    def getinfo(self):
        return {"姓名": self.name, "年龄": self.age, "地址": self.addr}

    def sleep(self):
        """
        普通函数 睡觉
        :return:
        """
        print("睡觉")

    def eat(self):
        print("吃饭")

    def move(self):
        print("走路")


student = Student("奥巴马", 20, "纽约")
print(student.getinfo())


def ChangeInt(a):
    print(a)
    a = 10
    print(a)


b = 2
ChangeInt(b)
print(b)  # 结果是 2