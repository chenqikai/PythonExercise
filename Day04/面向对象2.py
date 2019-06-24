class Boll(object):
    ProdectPlace = "China"

    def __init__(self, _color):
        self.color = _color


print("Boll", id(Boll))
print(Boll.ProdectPlace, id(Boll.ProdectPlace))
b1 = Boll("red")
b2 = Boll("black")
print(id(b1.ProdectPlace))
b1.ProdectPlace = ("USA")
print(id(b1.ProdectPlace))
print(id(b2.ProdectPlace))


