# 多级雷达图绘制：根据给定任务能力数据，绘制多级雷达图

import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
# plt绘图显示中文名
plt.rcParams['font.sans-serif'] = ['SimHei']

# 使用字典存储
My_Score = [{'高等数学': 93, '大学物理': 80, '大学体育': 60, 'C语言': 98, '线性代数': 85},
            {'高等数学': 80, '大学物理': 65, '大学体育': 90, 'C语言': 80, '线性代数': 85}]
data_len = len(My_Score[0])    # 五维度
print(data_len)

angles = np.linspace(0, 2 * pi, data_len, endpoint=False)    # 把360度分成5个，不包括最后值

lab = [key for key in My_Score[0].keys()]    # 获取五个维度的标签
print(lab)
My_score_evey = [[v for v in socre.values()] for socre in My_Score]    # 获取各课成绩
print(My_score_evey)

My_score_evey_1 = np.concatenate((My_score_evey[0], [My_score_evey[0][0]]))    # 获取第一个
print(My_score_evey_1)

My_score_evey_2 = np.concatenate((My_score_evey[1], [My_score_evey[1][0]]))    # 获取第二个
print(My_score_evey_2)

angles = np.concatenate((angles, [angles[0]]))
lab = np.concatenate((lab, [lab[0]]))
print(angles)
print(lab)

My_fig = plt.figure(figsize=(8, 6), dpi=100)
ax = plt.subplot(111, polar=True)

ax.plot(angles, My_score_evey_1, color='red')
ax.plot(angles, My_score_evey_2, color='blue')

ax.set_thetagrids(angles * 180 / pi, lab)
ax.set_theta_zero_location('N')

ax.set_rlabel_position(270)

plt.show()



