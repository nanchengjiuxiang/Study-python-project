# 捕获异常:按照我们自己的处理方式,处理完异常,程序继续执行。(编写程序时,做好预案,出现异常,按预案处理)

try:
    # print(my_name)    # NameError: name 'my_name' is not defined
    print(1 / 0)   # division by zero

# 捕获异常 NameError
except NameError as e:
    print("名字异常, 代码错误：", e)

except ZeroDivisionError as e:
    print("0不能做除数,  代码错误：", e)

# 捕获所有异常
except Exception as e:
    print("代码错误：", e)

finally:
    print("资源释放")