# 科学坐标图绘制：根据给定的数据绘制阻尼衰减曲线图

import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# 生成离散的点
My_x = np.linspace(0, 10, 100)

# 阻尼衰减曲线
My_y = np.exp( - My_x) * np.cos(2 * pi * My_x)
print(My_y)

plt.plot(My_x, My_y)
plt.show()



