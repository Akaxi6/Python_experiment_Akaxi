# 编写一个猜年龄的小游戏

'''
输入：当前真正年龄rel_age，猜的年龄整数ges_age,
输出：字符“猜大了”或者是字符“猜小了”,”猜对了“
'''

def Guess_age(rel_age,ges_age):
    if rel_age < ges_age:
        print("您猜的年龄{0}大啦~".format(ges_age))
        return False
    elif rel_age > ges_age:
        print("您猜的年龄{0}小啦~".format(ges_age))
        return False
    else:
        print("猜对啦~年龄是{0}岁".format(rel_age))
        return True


x = int(input("请输入真实的年龄："))
flag = False
while not flag:
    flag = Guess_age(x, int(input("请输入您猜的年龄：")))





