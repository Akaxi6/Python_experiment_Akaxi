# 查找磁盘内大小相同的文件
# 遍历目录及其子目录中的所有文件，将它们的文件大小作为键，文件路径作为值存储在一个字典中。
# 如果多个文件具有相同的文件大小，则将路径添加到相应的列表中

import os


def My_find_file(fp):
    file_size = {}    # 定义一个文件大小字典

    for dirpath, dirnames, filenames in os.walk(fp):
        # os.walk() 函数
        # 第一个参数 dirpath：需要遍历的文件夹路径
        # 第二个参数 dirnames：当前文件夹下所有子文件夹的名称列表
        # 第三个参数 filenames：当前文件夹下所有文件的名称列表
        for filename in filenames:
            path = os.path.join(dirpath, filename)    # 拼接函数
            print(path)
            size = os.path.getsize(path)
            print("文件大小：", size)

            if size not in file_size:      # 按照文件大小存储文件路径
                file_size[size] = [path]   # 键是文件大小，值是文件路径
            else:
                file_size[size].append(path)    # 如果有相同文件大小，则直接存路径

    # 开始查找相同大小文件
    for size, paths in file_size.items():
        if len(paths) >= 2:     # 如果一个文件大小键下有两个路径值 -- 则重复
            print("\n发现具有相同大小的文件啦:")
            for path in paths:
                print(path)

    print("\n程序结束~")


My_path = "C:/Users/Akaxi/Desktop/Akaxi_python/Python_experiment_Akaxi/第三次实验"  # 替换为你所需的目录
My_find_file(My_path)
