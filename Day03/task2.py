class MightMarket:
    def __init__(self, _name, _loc, _sells, _pay=("WechatPay", "AliPay", "CashPay")):
        self.name = _name
        self.loc = _loc
        self.sales = _sells
        self.pay = _pay

    def canEatBy(self, _foodType, _patType):
        if _foodType in self.sales:
            if _patType in self.pay:
                print("速度来吃")
            else:
                print("只能用", self.pay, "!!!!")
        else:
            print("没饭，快滚！！！", "没有", _foodType)


rs1 = MightMarket("南苑餐厅", "南苑", ["炒面", "盖浇饭", "自选菜"])
rs1.canEatBy("烧烤", "WechatPay")

rs2 = MightMarket("北苑餐厅", "北苑", ["鸡蛋灌饼", "水煎包", "热干面"])
rs2.canEatBy("水煎包", "AliPay")
