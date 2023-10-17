# 输入两个整数，打印他们相除后的结果，若输入的不是整数或除数为0，进行异常处理

def My_Divi(x, y):
    if isinstance(x, int) and isinstance(y, int) and y != 0:    # 如果被除数x和除数y都是整数
        num = x / y
        print(num)
    elif not isinstance(x, int):
        print("被除数{0}不是整数".format(x))
    elif not isinstance(y, int):
        print("除数{0}不是整数".format(y))
    elif y == 0:
        print("除数为0啦")
    else:
        print("错误")


num1 = eval(input("请输入被除数："))
num2 = eval(input("请输入除数："))
My_Divi(num1, num2)




