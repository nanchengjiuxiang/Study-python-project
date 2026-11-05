# 类型注解是Python中的一种语法特性,用于明确标识变量、函数参数和返回值的数据类型,从而使代码更清晰、更安全、更易维护。

# 变量定义 - 未指定类型注解 ---> 类型推断:指Python解释器自动推断出变量、表达式或函数返回值的数据类型的能力,而无需开发者显式声明。
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count":2 , "total":10}
goods=("手机", 6999, 1)

# 类型推断:指Python解释器自动推断出变量、表达式或函数返回值的数据类型的能力,而无需开发者显式声明。
names.append(1000)   # 应为类型 str (匹配的泛型类型 _T)，但实际为 Literal[1000]   Literal[1000] 无法赋值给 str


# 变量定义 - 指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str] = ["A", "C", "E"]
phones2: set[str | int] = {"13309091111", "15209101902", "18809019201", 1000, 5000}
options2: dict[str, int] = {"count":2, "total":10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)

names2.append(1000)  # 应为类型 str (匹配的泛型类型 _T)，但实际为 Literal[1000]   Literal[1000] 无法赋值给 str