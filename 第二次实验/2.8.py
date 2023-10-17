# 凯撒加密算法原理与实现。
import string


def My_kaisa(s, k):
    low = string.ascii_lowercase    # 小写字母
    up = string.ascii_uppercase     # 大写字母
    before = string.ascii_letters   # 变换前的字母表
    after = low[k:] + low[:k] + up[k:] + up[:k]
    table = ''.maketrans(before, after)
    new_s = s.translate(table)
    print("凯撒加密后前的字符串：{0}-->凯撒加密后的字符串{1}".format(s, new_s))


m = input("请输入代加密字符：")
n = int(input("请输入凯撒加密移动数："))
My_kaisa(m, n)





















