# 编写程序，输入球的半径，计算表面积和体积，半径为实数，用pi，结输出为浮点数，共10位其中2位有效数字
import math

r = float(input("请输入球半径："))
pi = math.pi  # 定义pi
S = 4.0/3 * pi * pow(r, 3)
V = 4 * pi * pow(r, 2)

print('半径为{0:.2f}球的表面积为{1:.2f}，体积为{2:.2f}'.format(r, S, V))




