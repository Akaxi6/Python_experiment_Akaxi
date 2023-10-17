# 2.1-肥胖指数BMI计算
# 输入小明身高1.75m，体重80.5kg.请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，计算规则为：
# 18.5<     过轻
# 18.5-25   正常
# 25-28     过重
# 28-32     肥胖
# >32       严重肥胖

def My_BMI(tall, kilo):
    BMI = kilo / pow(tall, 2)
    if 0 <= BMI < 18.5:
        print('BMI为{0:.2f}：过轻'.format(BMI))
    elif 18.5 <= BMI < 25:
        print('BMI为{0:.2f}：正常'.format(BMI))
    elif 25 <= BMI < 28:
        print('BMI为{0:.2f}：过重'.format(BMI))
    elif 28 <= BMI < 32:
        print('BMI为{0:.2f}：肥胖'.format(BMI))
    elif 32 <= BMI < 50:
        print('BMI为{0:.2f}：严重肥胖'.format(BMI))
    else:
        print('输入错误'.format(BMI))


x = float(input("请输入身高："))
y = float(input("请输入体重："))
My_BMI(x, y)





