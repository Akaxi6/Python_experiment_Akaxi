# 使用列表，实现筛选法求素数
import math

k = int(input("请输入要求素数的上限："))

t = [1]
for i in range(1, k):
    t.append(i + 1)
print("原始列表：", list(t))

for i in t:    # 在列表中进行操作
    for j in range(2, int(math.sqrt(i)) + 1):    # 使用循环来判断，到这个数的一半
        if i % j == 0:         # 如果数能够被整除，就不是素数
            break
    else:     # 否则就是素数
        print("在列表中{0}是一个素数".format(i))

