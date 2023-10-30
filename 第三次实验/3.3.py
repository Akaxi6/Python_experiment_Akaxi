# 定义一个员工类Employee，有数据成员姓名，编号。
# 定义一个销售员继承自员工类Sales，工资为销售额的提成10%
# 定义一个经理类Manager，固定工资8000
# 定义一个销售经理类，继承自销售员类以及经理类，工资为固定工资5000加销售额提成5%
# 每个类均有Display函数输出信息，编写主程序测试函数

# 员工类Employee
class Employee(object):
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def Display(self):
        print('姓名：', self.name)
        print('编号：', self.num)


# 销售员类Sales
class Sales(Employee):
    def __init__(self, name, num, money):
        super().__init__(name, num)
        self.money = money

    def money_10per(self):
        money_10 = self.money * 0.1
        return money_10

    def Display(self):
        super(Sales, self).Display()
        print("销售员工资：", self.money_10per())


# 经理类Manager
class Manager(Employee):
    def __init__(self, name, num):
        super().__init__(name, num)

    def money_static(self):
        return 8000


    def Display(self):
        super(Manager, self).Display()
        print("经理工资：", self.money_static())


# 销售经理类SalesManager
class SalesManager(Sales, Manager):
    def __init__(self, name, number, money):
        Sales.__init__(self, name, number, money)
        Manager.__init__(self, name, number)

    def money_static_add(self):
        total_money = self.money * 0.05 + 5000
        return total_money

    def Display(self):
        super(SalesManager, self).Display()
        print("销售经理工资：", self.money_static_add())


print("----------")
xiaowang = Employee('小王', 2021212981)
xiaowang.Display()

print("----------")
xiaohu = Sales('小胡', 2021212989, 5400)
xiaohu.Display()

print("----------")
xiaonuo = Manager('小虎', 2020202964)
xiaonuo.Display()

print("----------")
xiaoguo = SalesManager('小狮', 2019264695, 7000)
xiaoguo.Display()
