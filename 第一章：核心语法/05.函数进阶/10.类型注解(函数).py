# 函数类型注解
def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 * r*r, 1), round(2 *3.14*r, 1)

al = circle_area_len(10)
print(al)