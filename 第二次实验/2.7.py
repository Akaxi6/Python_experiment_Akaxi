# 7、一年365天，如果好好学习时能力值比前一天提高1%，当放任时相比前一天下降1%，编程计算两种情况效果相差值。

def My_Study(day):
    num_pro = 100
    num_des = 100
    for i in range(day):
        num_pro = num_pro * 1.01
        num_des = num_des * 0.99
    diff = (num_pro - num_des) / num_pro * 100
    print("{0}天后，好好学习成绩：{1:.2f}；放任后成绩{2:.2f};好好学习成绩与放任成绩相比：{3:.2f}%".format(day, num_pro, num_des, diff))


x = int(input('请输入多少天：'))
My_Study(x)






