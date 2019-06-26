# -*- coding: utf-8 -*-

"""
请求 ：request 在服务器输入网址回车
响应 ：response 浏览器返回数据

分析一次请求响应
    1.general 基本项目
        URL
        方法
        状态
    2.请求头


"""
import urllib.request

urllib.request.urlretrieve("https://www.elichen.club", filename=r"C:\Users\13126\Desktop\Python小学期\陈旗开\Day06\elichen.html")
urllib.request.urlcleanup()
