# 编写一个学生和教师数据输入和显示程序。其中，学生数据有编号、姓名和成绩，教师数据有编号、姓名、职称和部门。要求：
# 将编号、姓名输入和显示设计成一个类person
# 设计类person的派生类：学生类student和教师类teacher


class person(object):
    def __init__(self, num, name):
        self.num = num
        self.name = name

    def show(self):
        print(self.num, self.name)


class student(person):
    def __init__(self, num, name, cls, grades):
        super().__init__(num, name)    # 继承父类
        self.cls = cls
        self.grades = grades

    def show(self):
        print(self.num, self.name, self.cls, self.grades)


class teacher(person):
    def __init__(self, num, name, oppostion, location):
        super().__init__(num, name)    # 继承父类
        self.oppostion = oppostion
        self.location = location

    def show(self):
        print(self.num, self.name, self.oppostion, self.location)

# person1 = person(2021212981, '王忠全')
# person1.show()


student2 = student(2021212981, '王忠全', 8052102, 98,)
student2.show()

teacher3 = teacher(1013198974, '张老师', 'Python实验老师', '自动化学院')
teacher3.show()