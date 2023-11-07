# k-means聚类算法进行分类  （可以沿用第一题的身高体重数据 | 或者是手写数据集MINIST）

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# plt绘图显示中文名
plt.rcParams['font.sans-serif'] = ['SimHei']

# 定义身高体重数据
My_tall_weight_train = [
    [180, 50], [180, 65], [180, 90], [180, 95], [180, 55],
    [168, 57], [176, 65], [163, 48], [182, 80], [159, 51],
    [175, 90], [165, 50], [185, 100], [160, 45], [180, 95],
    [170, 55], [190, 105], [155, 40], [176, 85], [162, 48],
    [172, 60], [195, 110], [158, 42], [182, 94], [168, 52],
    [178, 80], [150, 35], [188, 98], [157, 43], [173, 68],
    [165, 37], [188, 70], [175, 80], [183, 88], [162, 45],
    [176, 75], [168, 58], [158, 41], [179, 82], [170, 50],
    [187, 97], [152, 38], [169, 62], [181, 92], [172, 56],
    [191, 103], [157, 44], [174, 78], [164, 49], [184, 90]
]

My_kmeans = KMeans(n_clusters=3)
# n_clusters 生成的聚类数

My_kmeans.fit(My_tall_weight_train)    # 训练

cls1 = [My_tall_weight_train[i] for i in range(len(My_kmeans.labels_)) if My_kmeans.labels_[i] == 0]
cls2 = [My_tall_weight_train[i] for i in range(len(My_kmeans.labels_)) if My_kmeans.labels_[i] == 1]
cls3 = [My_tall_weight_train[i] for i in range(len(My_kmeans.labels_)) if My_kmeans.labels_[i] == 2]

plt.scatter([x[0] for x in cls1], [y[1] for y in cls1], color = 'red')
plt.scatter([x[0] for x in cls2], [y[1] for y in cls2], color = 'blue')
plt.scatter([x[0] for x in cls3], [y[1] for y in cls3], color = 'green')

plt.xlabel('身高')
plt.ylabel('体重')
plt.title("使用K-Means进行聚类")
plt.show()




