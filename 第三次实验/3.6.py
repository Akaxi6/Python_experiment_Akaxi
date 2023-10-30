# 读写文本文件并添加行号。

def My_Addline(file, file_change):
    with open(file, 'r', encoding='utf-8', errors='ignore') as fp:    # 以读模式打开文件
        lines = fp.readlines()    # 读取每一行
        print(lines)

    with open(file_change, 'w', encoding='utf-8') as fp_change:    # 以写模式打开文件
        # for i, line in enumerate(lines, 1):
        #     fp_change.write(f"{i}: {line}")
        for index, item in enumerate(lines):    # 获取行数与行内容
            print(index+1)    # 行数需要+1，不然是从第0行开始的
            print(item)
            fp_change.write("第{0}行:{1}".format(index+1, item))


file = "My_file_2.txt"  # 输入文件名
file_change = "My_file_change.txt"  # 输出文件名
My_Addline(file, file_change)
