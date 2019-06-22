import random
import keyword

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

print(keyword.kwlist)
str = 'Elichen'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串

list = ['abcd', 786, 2.23, 'elichen', 70.2]
tinylist = [123, 'elichen']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

list1 = ['e', 'l', 'i', 'c', 'h', 'e', 'n']
print(list1[1:4:2])

tuple = ('abcd', 786, 2.23, 'elichen', 70.2)
tinytuple = (123, 'elichen')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

dict = {}
dict['one'] = "1"
dict[2] = "2"

tinydict = {'name': 'elichen', 'code': 1, 'site': 'www.elichen.club'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值