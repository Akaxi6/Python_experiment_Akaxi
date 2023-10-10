# 检测密码安全强度
import string

d = {1: "这个密码很不安全嘞~", 2: "这个密码弱安全度嘞~", 3: "这个密码比较安全嘞~", 4: "这个密码很安全嘞~"}

flag = [False] * 4

s = input("请输入您的密码：")

for ch in s:
    if not flag[0] and ch.isupper():    # 大写字母
        flag[0] = True
    elif not flag[1] and ch.islower():    # 小写字母
        flag[1] = True
    elif not flag[2] and ch.isdigit():    # 大写字母
        flag[2] = True
    elif not flag[3] and ch in '~`!@#$%^&*()_+{}[]:;:?/>.<,':  # 大写字母
        flag[3] = True

print(d.get(sum(flag)))



