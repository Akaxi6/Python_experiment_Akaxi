# 使用蒙特.卡洛法计算圆周率近似值
import random
from tqdm import tqdm    # 进度条


def MY_Pi(N):    # 一共在正方形扔N次数
    count = 0    # 统计落在圆内的次数
    for i in tqdm(range(N)):    # 一共抛N次
        x = random.uniform(-1, 1)    # 随机浮点数
        y = random.uniform(-1, 1)
        if pow(x, 2) + pow(y, 2) <= 1:    # 在圆内
            count += 1    # 落在圆内，计数器加1
    pi = 4 * count/N
    print("运用蒙特卡洛法，执行{0}次，近似pi={1}".format(N, pi))


k = int(input("请输入执行次数:"))
MY_Pi(k)








