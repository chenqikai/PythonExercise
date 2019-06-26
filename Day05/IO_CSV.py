# -*- coding: utf-8 -*-
import csv
#
# try:
#     with open("000001.csv", "r")as f:
#         csv_reader = csv.reader(f)
#         print(csv_reader)
#         for r in csv_reader:
#             print(r)
# except FileNotFoundError as e:
#     print(e)
#
# try:
#     with open("000002.csv", "w", newline="")as f:
#         csv_writer = csv.writer(f)
#         csv_writer.writerow(["id", "name", "age"])
#         csv_writer.writerow([1, "奥巴马", 20])
#         csv_writer.writerow([2, "特朗普", 15])
# except Exception as e:
#     print(e)
import csv

# csv 写入
stu1 = ['marry', 26]
stu2 = ['bob', 23]
# 打开文件，追加a
out = open('Stu_csv.csv', 'a', newline='')
# 设定写入模式
csv_write = csv.writer(out, dialect='excel')
# 写入具体内容
csv_write.writerow(stu1)
csv_write.writerow(stu2)
print("write over")
