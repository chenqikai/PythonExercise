"""
面向对象编程 : 类编程
类编程 : 通过抽象物理世界对象
    特征 : 属性
    行为 : 方法



特征：属性
    实例属性
    类属性
"""


class Boll(object):
    ProductionPlace = "China"

    def __init__(self, _color, _materials, _price):
        """
        构造函数可以创建类：通过构造函数确定实例属性
        """
        self.color = _color
        self.materials = _materials
        self.price = _price

    def getcolor(self):
        return self.color


# 类属性存储于类内存
print(Boll.ProductionPlace)
b1 = Boll("red", "mat1", "200")
b2 = Boll("black", "mat2", "100")
print(b1.getcolor(), b2.getcolor())
