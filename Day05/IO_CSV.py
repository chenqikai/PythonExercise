# -*- coding: utf-8 -*-
import csv

# try:
#     with open("000001.csv", "r")as f:
#         csv_reader = csv.reader(f)
#         for row in csv_reader:
#             print(row[0])
# except FileNotFoundError as e:
#     print(e)

try:
    with open("000002.csv", "w", newline="")as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["id", "name", "age"])
        csv_writer.writerow([1, "奥巴马", 20])
        csv_writer.writerow([2, "特朗普", 15])
except Exception as e:
    print(e)
