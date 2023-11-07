# 批量生成姓名、家庭住址、电子邮箱等随机信息，并以二进制进行文件读 / 写。
# fake 库即可随机生成伪数据

import random
import faker
import struct

fake = faker.Faker()    # 实例化fake


# 随机生成：姓名、家庭住址、电子邮箱
def My_message():
    name = fake.name()
    address = fake.address().replace('\n', ', ')    # 把地址拼接到一段
    email = fake.email()
    return name, address, email  # 返回随机的姓名，地址，邮箱


# 批量生成随机信息写入二进制文件
def My_write(file_path, num_entries):
    with open(file_path, 'wb') as fp:
        for i in range(num_entries):    # 写入多少数量
            name, address, email = My_message()

            name_2data = name.encode('utf-8')    # 将字符串转换为二进制数据
            address_2data = address.encode('utf-8')
            email_2data = email.encode('utf-8')
            data = struct.pack('I', len(name_2data)) + name_2data     # 使用struct将数据打包为二进制格式
            data += struct.pack('I', len(address_2data)) + address_2data
            data += struct.pack('I', len(email_2data)) + email_2data
            fp.write(data)    # 写



# 从二进制文件中读取信息
def My_read(file_path):
    with open(file_path, 'rb') as fp:
        while True:
            length_data = fp.read(4)    # 从文件中读取4字节的数据，解析为字符串长度
            if not length_data:
                break
            length = struct.unpack('I', length_data)[0]
            data = fp.read(length)      # 读取指定长度的数据，并解码为字符串
            print(data.decode('utf-8')) # 打印


# 调用函数生成随机信息并写入二进制文件
file_path = 'My_file.bin'     # 写的文件名字
num_entries = 3                   # 随机生成信息的数量
My_write(file_path, num_entries)  # 写入文件
My_read(file_path)    # 从二进制文件中读取信息并打印