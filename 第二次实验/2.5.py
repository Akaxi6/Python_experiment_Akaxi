# 模拟报数游戏（约瑟夫环问题）
# 有n个人围成一圈，从1开始按顺序编号，从第一个人开始从1到k（假设k=3）报数，
# 报到k的人退出圈子；然后圈子缩小，从下一个人继续游戏，问最后留下的是原来的第几号。

def My_baoshu(n, k):
    t = [1]    # 生成原始列表--圈圈
    for i in range(1, n):
        t.append(i + 1)
    count = 0    # 定义计数指针
    while len(t) != 1:
        t_new = t[:]
        print(list(t_new))
        for j in range(0, len(t_new)):    # 循环新列表
            count += 1
            if count % k == 0:    # 当报到k时弹出
                t.remove(t_new[j])    # 在原来的列表里除去点到的数
    print('留下的是原来的{0}号'.format(list(t)))


n = int(input("请输入多少个人参与："))
k = int(input("请输入报到多少退出圈子："))
My_baoshu(n, k)




