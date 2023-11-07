# 使用matplotlib绘制折现图，对龟兔赛跑中兔子和乌龟行走轨迹进行可视化

import matplotlib.pyplot as plt
# plt绘图显示中文名
plt.rcParams['font.sans-serif'] = ['SimHei']

# 乌龟行走轨迹
turtle_path = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 兔子行走轨迹
rabbit_path = [0, 2, 4, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10, 12, 14, 16]

# 绘制折线图
plt.plot(turtle_path, label='乌龟')  # 绘制乌龟行走轨迹
plt.plot(rabbit_path, label='兔子')  # 绘制兔子行走轨迹

# 设置图表标题、坐标轴名称、图例等属性
plt.title('---龟兔赛跑轨迹---')
plt.xlabel('时间（s）')
plt.ylabel('距离（m）')
plt.legend()    # 线例

# 显示图形
plt.show()









