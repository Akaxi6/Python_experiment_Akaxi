# 自定义类模拟三维向量及其运算，加法、减法、向量与标量的乘法和除法


class My_3D(object):
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def __add__(self, other):
        my_add = My_3D(self.a + other.a, self.b + other.b, self.c + other.c)
        return my_add

    def __sub__(self, other):
        my_sub = My_3D(self.a - other.a, self.b - other.b, self.c - other.c)
        return my_sub

    def __mul__(self, other):
        my_mul = My_3D(self.a * other.a, self.b * other.b, self.c * other.c)
        return my_mul

    def show(self):
        print((self.a, self.b, self.c))


v1 = My_3D(1, 2, 3)
v2 = My_3D(4, 5, 6)
v_sum = v1 + v2
v_sub = v1 - v2
v_mul = v1 * v2

# 输出
print('原来的v1：')
v1.show()
print('原来的v2：')
v2.show()
print('相加得：')
v_sum.show()
print('相减得：')
v_sub.show()
print('相乘得：')
v_mul.show()
