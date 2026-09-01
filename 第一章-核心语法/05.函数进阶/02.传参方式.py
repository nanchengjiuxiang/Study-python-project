# 传参方式指的是,在调用函数时,传递实参的方式。

# 1. 位置参数:调用函数时根据函数定义时的位置来传递参数。---> 要求:调用函数时参数顺序与定义函数时参数顺序完全一致
def reg_stu(name,age,gender,city) :
    print("姓名:",name,"年龄",age,"性别",gender,"城市",city)
    return {"姓名:":name,"年龄":age,"性别":gender,"城市":city}

stu = reg_stu("张三",18,"男","北京")
print(stu)



# 2. 关键字参数:调用函数时以函数定义时形参名称作为关键字,以 “键=值” 的形式来传递参数(不要求顺序)。
stu1 = reg_stu(age="18",name="张三",city="北京",gender="男")
print(stu1)

# 混合使用---位置传参 + 关键字传参   ---> 位置参数在前，关键字参数在后
stu2 = reg_stu("赵四",28,city="上海",gender="男")
print(stu2)