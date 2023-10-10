# 输入直角三角形直角边a,b。求斜边c输出 (from math import *)
from math import *

a = int(input("请输入三角形的直角边a："))
b = int(input("请输入三角形的直角边b："))
c = pow(pow(a, 2) + pow(b, 2), 0.5)
print("斜边长度是：{0}".format(c))




