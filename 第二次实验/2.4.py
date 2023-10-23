# 使用枚举法验证6174猜想：6174猜想 ，1955年，卡普耶卡(D.R.Kaprekar)研究了对四位数的一种变换：
# 任给出四位数k0,用它的四个数字由大到小重新排列成一个四位数m,再减去它的反序数rev(m),得出数k1=m-rev(m),
# 然后，继续对k1重复上述变换，得数k2.如此进行下去，卡普耶卡发现，无论k0是多大的四位数， 只要四个数字不全相同，最多进行7次上述变换，就会出现四位数6174
def My_sort(n):    # 把数字从大到小排序
    s = str(n)         # s是n的字符串
    s_bu = '0' * (4 - len(s)) + s   # 把不足四位的数补零
    s_sort = ''.join(sorted(s_bu, reverse=True))   # 返回排序后的数字
    return s_sort


def My_6174(n):
    step = 1
    old_n = n
    print('验证：', old_n)
    while step <= 8:  # 一直循环
        n = int(n)  # 把n改成整数
        m = int(My_sort(n))  # 把n从大到小排序
        m_re = int(str(m)[::-1])  # 把m变成字符串后反序再变成整数
        k = m - m_re  # 新的差
        print("{0} - {1} = {2}".format(m, m_re, k))
        if k == 6174:  # 如果是6174则跳出循环
            break
        else:
            n = k  # 把差值作为新的数字
        step += 1  # 步数加一
    if k == 6174 and step <= 8:
        print('{0}进行了{1}次算法得到了6174'.format(old_n, step))
        return True
    else:
        print('验证6174失败')
        return False


Flag = True
i = 999

while Flag and i < 9999:    # 如果正确就会一直验证
    i += 1
    if len(set(str(i))) == 1:    # 如果所有数字都相同，则跳过
        continue
    else:    # 否则就进行验证
        Flag = My_6174(i)

if Flag == True:
    print('在四位数中验证6174没有失败！！猜想正确！')
elif Flag == False:
    print('在四位数中验证6174有失败！！猜想错误！')