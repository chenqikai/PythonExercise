def tell(name, *args, **kwargs):
    print("我是：", name)
    print("我要告诉一下人员：")
    for i in args:
        print(i)
    print("找对象有以下要求：")
    for k, v in kwargs.items():
        print(k, v)


tell("elichen", '张三', '李四', '王五', 身高="180±5 cm", 体重="70KG", 房子="150平米以上",车子 = "20万以上")
