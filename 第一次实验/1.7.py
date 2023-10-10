# 文本进度条：编程通过格式化字符串输出和时间延迟实现控制台，风格文本进度条
import time

c = 0

for i in range(0, 105, 5):
    c = c + 1
    k = 21 - c
    print("\r{0:3}% |{1}{2}".format(i, c * '*', k * '-'), end=' ')
    time.sleep(0.2)



