# 导入整个模块 ---> 调用方式 ：模块名.功能名
import random
import random as r

for i in range(10):
    print(random.randint(1,100))
    print(r.randint(1,100))


# 导入模块当中的功能
from random import randint
from random import randint as rt
from random import *

print(randint(1,100))
print(rt(1,100))