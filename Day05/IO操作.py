"""
IO操作
内存 =》 临时存储
磁盘 =》 永久存储

1 建立一个文件的连接句柄
2 读取或写入文件
3 释放文件句柄
"""

# Exp1

filehandler = open("data.txt", mode="r", encoding="utf8")
content = filehandler.read()
filehandler.close()

print(content)

for i in range(1, 11):
    filehandlertemp = open("data" + str(i) + ".txt", "w", encoding="utf8")
    filehandlertemp.write(content)
    filehandlertemp.close()
