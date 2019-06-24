class Human:
    character = "互帮互助"

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def getinfo(self):
        return self.name


class Business(Human):
    def __init__(self, _name, _age, _price):
        # 使用父类构造方法赋值
        Human.__init__(self, _name, _age)
        self.price = _price

    def getinfo(self):
        return self.name + " " + str(self.price)


class Programmer(Human):
    character = "严谨细密"

    def __init__(self, _name, _age, _language):
        Human.__init__(self, _name, _age)
        self.language = _language

    def getinfo(self):
        return self.name + " " + str(self.language)


h1 = Human("北京人", 1000)
print(Human.character)
print(h1.getinfo())

b1 = Business("周鸿祎", 50, 520)
print(b1.character)
print(b1.getinfo())

p1 = Programmer("程序员", 25, "Python")
print(p1.character)
print(p1.getinfo())
