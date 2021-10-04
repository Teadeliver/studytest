print("请输入本金：")
benjin = int(input())
print("请输入年利率：")
nianlilv = float(input())
print("请输入年数：")
nianshu = int(input())
i = 0
print(benjin)
while i < nianshu:
    benjin = benjin * (1 + nianlilv / 100)
    i += 1
print("本金利率和为：{0；2.2f}", benjin)
print("本金利率和为：{0；2.2f}", benjin)