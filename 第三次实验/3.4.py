# 编写一个程序计算出球、圆柱和圆锥的表面积和体积，要求：
# 定义一个基类，至少含有一个数据成员半径，并设为私有成员；
# 定义基类的派生类球、圆柱、圆锥，都含有求表面积和体积的成员函数和打印函数；
# 编写主函数，求球、圆柱、圆锥的表面积和体积。
import math
pi = math.pi


class My_R(object):
    def __init__(self, r):
        self.__r = r

    def public_r(self):    # 公有方法访问私有r
        return self.__r


# 球
class My_Qiu(My_R):
    def __init__(self, r):
        super().__init__(r)
        self.r = self.public_r()

    def My_Qiu_V(self):
        return 4 / 3 * pi * pow(self.r, 3)

    def My_Qiu_S(self):
        return 4 * pi * pow(self.r, 2)

    def show(self):
        print("圆的半径：{0},体积：{1:.2f},表面积：{2:.2f}".format(self.r, self.My_Qiu_V(), self.My_Qiu_S()))


# 圆柱
class My_Yuanzhu(My_R):
    def __init__(self, r, h):
        super().__init__(r)
        self.r = self.public_r()
        self.h = h

    def My_Yuanzhu_V(self):
        return pi * pow(self.r, 2) * self.h

    def My_Yuanzhu_S(self):
        return 2 * pi * pow(self.r, 2) + 2 * pi * self.r * self.h

    def show(self):
        print("圆柱的半径：{0},体积：{1:.2f},表面积：{2:.2f}".format(self.r, self.My_Yuanzhu_V(), self.My_Yuanzhu_S()))


class My_Yuanzhui(My_R):
    def __init__(self, r, h, l):
        super().__init__(r)
        self.r = self.public_r()
        self.h = h
        self.l = l

    def My_Yuanzhui_V(self):
        return 1 / 3 * pi * pow(self.r, 2) * self.h

    def My_Yuanzhui_S(self):
        return pi * self.r * self.l + pi * pow(self.r, 2)

    def show(self):
        print("圆锥的半径：{0},体积：{1:.2f},表面积：{2:.2f}".format(self.r, self.My_Yuanzhui_V(), self.My_Yuanzhui_S()))

# 打印输入
Qiu1 = My_Qiu(2)
Qiu1.show()

Yuanzhu1 = My_Yuanzhu(2, 5)
Yuanzhu1.show()

Yuanzhi1 = My_Yuanzhui(2, 5, 8)
Yuanzhi1.show()



