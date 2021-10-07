weight = float(input("请输入果子的重量，单位g："))
if weight < 200:
    print("小果")
elif weight < 500:
    print("中果")
else:
    print("大果")
