"""
采用面向对象的编程思想,完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息,通过
控制台菜单与用户交互,具体的功能如下:
    1. 添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩,记录在系统中
    2. 修改学生成绩:根据输入的学生姓名,修改对应的学生成绩
    3. 删除学生成绩:根据输入的学生姓名,删除对应的学生成绩
    4. 查询指定学生成绩:根据输入的学生姓名,查找对应的学生成绩,并输出
    5. 展示全部学生成绩:展示出系统中所有学生的成绩
"""
from os import name


# 定义一个类为学生
class Student:

    # 初始化学生属性，包含学生姓名、语文成绩、数学成绩、英语成绩
    def __init__(self, name, chinese_grade, math_grade, english_grade):
        self.name = name
        self.chinese = chinese_grade
        self.math = math_grade
        self.english = english_grade

    # 将实例属性转化为字符串
    def __str__(self):

        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"

    # 修改学生分数
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None :
            self.chinese = chinese
        if math is not None :
            self.math = math
        if english is not None :
            self.english = english


# 定义一个类为教务管理系统
class EduManagement:
    system_version = "1.0.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []   # 列表，记录学生信息

    # 添加学生成绩: 根据输入的学生姓名、语文成绩、数学成绩、英语成绩, 记录在系统中
    def add_student(self):
        name = input("输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print("学生已存在")
                return
        chinese = int(input("输入语文成绩："))
        math = int(input("输入数学成绩："))
        english = int(input("输入英语成绩："))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print(f"学生{name}添加完成")
            return
        else:
            print("分数范围在0 - 100 之间！！！")

    # 修改学生成绩: 根据输入的学生姓名, 修改对应的学生成绩
    def update_student(self):
        name = input("输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")

                chinese = int(input("输入修改后语文成绩："))
                math = int(input("输入修改后数学成绩："))
                english = int(input("输入修改后英语成绩："))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print(f"学生{name}成绩更新完成")
                    print(f"新成绩：{s}")
                    return
                else:
                    print("分数范围在0 - 100 之间！！！")
                    return
        print("未找到该学生！！！")

    # 删除学生成绩: 根据输入的学生姓名, 删除对应的学生成绩
    def delete_student(self):
        name = input("输入要删除的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功！")
                return
            else:
                print("学生不存在")
                return

    # 查询指定学生成绩: 根据输入的学生姓名, 查找对应的学生成绩, 并输出
    def show_student(self):
        name = input("输入要查找的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print(s)
                return
            else:
                print("学生不存在")

    # 展示全部学生成绩: 展示出系统中所有学生的成绩
    def show_all_student(self):
        for s in self.student_list:
            print(s)
            return

    # 运行系统
    def run(self):
        print("欢迎使用")

        while True:
            print("-----------------------------------------------------------------------------------------------")
            print(mune)

            choice = int(input("输入要执行的操作（1 - 6）:"))

            try:
                match choice:
                    case 1:
                        self.add_student()
                    case 2:
                        self.update_student()
                    case 3:
                        self.delete_student()
                    case 4:
                        self.show_student()
                    case 5:
                        self.show_all_student()
                    case 6:
                        break
                    case _:
                        print("无效操作")
            except Exception as e:
                print("程序出错了，错误信息：", e)
# 菜单
mune = """
##########教务管理系统##########
#        1. 添加学生信息        #
#        2. 修改学生信息        #
#        3. 删除学生信息        #
#        4. 查询学生信息        #
#        5. 列出所有学生        #
#        6. 退出系统           #
#############################
"""

edu_management = EduManagement()
edu_management.run()