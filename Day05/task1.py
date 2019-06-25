try:
    with open("aaa.jpg", mode="rb")as f:
        content = f.read()
        for i in range(1, 11):
            with open(str(i) + ".jpg", mode="wb")as ff:
                ff.write(content)
except FileNotFoundError as e:
    print(e)
