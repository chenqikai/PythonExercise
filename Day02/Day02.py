import random

"""
列表 ： 类似数组，元素可以是任意数据类型
"""
List1 = [4, 5, 6, 7, 8]
# print(List1)
# print(type(List1))
# print(len(List1))
List1.pop(0)
print(List1)

# 元组 内容不可变 不能添加 不能删除
t1 = (1, 2, 3, 4, 5)
print(t1)
print(type(t1))

t2 = (4, 5, 6, 7, 8)
print(t2[1:4])

for l in List1:
    print(l)

for key in t1:
    print(key)

if False:
    print(List1)
else:
    print(False)
# while True:
#     score = int(input("请输入成绩"))
#     if score >= 90:
#         print("成绩为优")
#     elif score >= 80:
#         print("成绩为良")
#     elif score >= 60:
#         print("成绩为中")
#     else:
#         print("成绩为差")
# for i in range(1, 10, 2):
#     print(i)

List2 = []
for i in range(10):
    num = random.randrange(50, 100)
    List2.append(num)
while True:
    List2lenth = len(List2)
    if List2lenth > 0:
        index = random.randrange(0, List2lenth)
        ele = List2.pop(index)
        print("删除了", ele)
    else:
        print('列表以清空')
        print(List2)
        break
