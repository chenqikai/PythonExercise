class MightMarket:
    def __init__(self, _name, _addr, _sells, _pay=("WechatPay", "AliPay", "CashPay", "PayPal")):
        self.name = _name
        self.loc = _addr
        self.sales = _sells
        self.pay = _pay

    def canEatBy(self, foodType, payType):
        if foodType in self.sales:
            if payType in self.pay:
                print("快来吃")
            else:
                print("只能用", self.pay, "!!")
        else:
            print("没有", foodType)


rs1 = MightMarket("华苑餐厅", "华苑", ["炒面", "鸭架饭", "自选菜"])
rs1.canEatBy("鸭架饭", "Wechat")

rs2 = MightMarket("教苑餐厅", "教苑", ["鸡蛋灌饼", "烩面", "热干面"])
rs2.canEatBy("烩面", "AliPay")
