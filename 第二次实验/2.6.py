# 模拟转盘抽奖游戏
# 一等奖、二等奖、三等奖
# 一等奖【0--0.1】
# 二等奖【0.1--0.3】
# 三等奖【0.3--1】

import random
from tqdm import tqdm


def My_gift(n):
    count = [0, 0, 0]
    for i in tqdm(range(n)):
        k = random.uniform(0, 1)
        if 0 <= k < 0.1:
            count[0] += 1
        elif 0.1 <= k < 0.3:
            count[1] += 1
        elif 0.3 <= k < 1:
            count[2] += 1
        else:
            print("错误")
    print("一等奖个数{0}二等奖个数{1}三等奖个数{2}".format(count[0], count[1], count[2]))


x = int(input("请输入抽奖多少次："))
My_gift(x)











