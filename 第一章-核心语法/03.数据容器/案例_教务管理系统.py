# -----------------------------------------------------案例一--------------------------------------------------------
# 开发一个教务管理系统,在该系统中可以维护和管理学员的成绩信息,具体需求如下:

# 1. 添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩,录入完成保存到系统中。
# 2. 修改学生信息:要求输入要修改的学生姓名,然后再提示输入语文、数学、英语成绩,输入完成后修改学员信息。
# 3. 删除学生信息:要求输入要删除的学生姓名,根据姓名删除学生信息。
# 4. 查询学生信息:要求输入要查询的学生姓名,根据姓名查询学生信息并输出。
# 5. 列出所有学生:遍历所有学生信息并输出。
# 6. 统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分,以及语文、数学、英语最高分和最低分的学员姓名。
# 7. 退出系统。

# 制作教务系统菜单
students = {}

mune = """
##########教务管理系统##########
#        1. 添加学生信息        #
#        2. 修改学生信息        #
#        3. 删除学生信息        #
#        4. 查询学生信息        #
#        5. 列出所有学生        #
#        6. 统计班级成绩        #
#        7. 退出系统           #
#############################
"""

# 执行操作
while True :
    print(mune)
    operation = input("输入你要执行的操作:")
    match operation:

    # 1. 添加学生信息
        case "1":
            name = input("输入学生姓名:")
            if name not in students:
                grade_ch = int(input("输入语文成绩:"))
                grade_ma = int(input("输入数学成绩:"))
                grade_en = int(input("输入英语成绩:"))
                students[name] = {"ch":grade_ch, "ma":grade_ma, "en":grade_en}
                print(f"录入学生 {name} 成功")
            else :
                print("该学生已存在")

    # 2. 修改学生信息
        case "2":
            name = input("输入要修改的学生姓名:")
            if name not in students:
                print("学生不存在！！！")
            else :
                new_ch = int(input("输入新的语文成绩:"))
                new_ma = int(input("输入新的数学成绩:"))
                new_en = int(input("输入新的英语成绩:"))
                students[name] = {"ch":new_ch, "ma":new_ma, "en":new_en}

    # 3. 删除学生信息
        case "3":
            name = input("输入要删除的学生姓名:")
            if name not in students:
                print("学生不存在！！！")
            else:
                del students[name]
                print("删除成功~")

    # 4. 查询学生信息
        case "4":
            name = input("输入要查询的学生姓名:")
            if name not in students:
                print("学生不存在！！！")
            else:
                student = students[name]
                print(f"学生姓名：{name}，语文成绩：{student["ch"]},数学成绩：{student["ma"]},英语成绩{student["en"]}")

    # 5. 列出所有学生
        case "5":
            for name in students.keys():
                student = students[name]
                print(f"学生姓名：{name}，语文成绩：{student["ch"]},数学成绩：{student["ma"]},英语成绩{student["en"]}")


    # 6. 统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分,以及语文、数学、英语最高分和最低分的学员姓名。
        case "6":
            ch = []
            ma = []
            en = []
            for name in students.keys():
                student = students[name]
                ch.append(student["ch"])
                ma.append(student["ma"])
                en.append(student["en"])
            print(f"语文最高分为{max(ch)}，最低分为{min(ch)}，平均分为{sum(ch)/len(ch)}")
            print(f"数学最高分为{max(ma)}，最低分为{min(ma)}，平均分为{sum(ma)/len(ma)}")
            print(f"英语最高分为{max(en)}，最低分为{min(en)}，平均分为{sum(en)/len(en)}")
            for k , v in students.items():
                if v["ch"] == max(ch):
                    print(f"语文最高分为 {k} : {max(ch)} ")
                if v["ma"] == max(ma):
                    print(f"数学最高分为 {k} : {max(ma)} ")
                if v["en"] == max(en):
                    print(f"英语最高分为 {k} : {max(en)} ")
    # 7. 退出系统
        case "7":
            print("退出成功！！！")
            break
        case _ :
            print("无效操作")