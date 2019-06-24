class Human(object):
    character = "互帮互助"

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def getinfo(self):
        return self.name


class Programmer(Human):
    character = "严谨细密"

    def __init__(self, _name, _age, _language):
        Human.__init__(self, _name, _age)
        self.language = _language

    def getinfo(self):
        return self.name + " 擅长的语言" + str(self.language)


"""
封装：
    在面向对象思想中，对一个类，将数据和过程封包围起来，对外隐藏具体的实现细节 
    并且数据（成员变量和成员函数）在内部是完全自由使用的，而外部对数据的访问是加访问限定的，某些对操作只能根据由内部提供接口，增加安全性。
继承：
    是面向对象最显著的一个特性，继承是从已有的类中派生出新的类称为子类，子类继承父类的数据属性和行为，并能根据自己的需求扩展出新的行为，提高了代码的复用性。
多态：
    指允许不同的对象对同一消息做出相应。即同一消息可以根据发送对象的不同而采用多种不同的行为方式（发送消息就是函数调用）。
    封装和继承几乎都是为多态而准备的，在执行期间判断引用对象的实际类型，根据其实际的类型调用其相应的方法。
"""
