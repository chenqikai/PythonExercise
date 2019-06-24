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


b1 = Boll("red", "mat1", "20")
print(b1.color)
print(b1.ProductionPlace)
# print(Boll.color)
"""
出错原因：实例属性必须经过实例化之后才能调用，在实例中访问一个属性，会先查找实例属性然后才是类属性,如果没有找到实例就会报错.
"""