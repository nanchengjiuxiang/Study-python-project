# 1. 定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)
def triangle_area(bottom, high) :
    """
    此函数用于根据底和高计算三角形面积
    :param bottom: 三角形的底边长
    :param high: 三角形的高
    :return: 三角形的面积
    """
    area = bottom * high / 2
    return area

print("底为30，高为20的三角形面积为",triangle_area(30,20))


# 2. 定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。
def vowel_count(st) :
    """
    此函数用于计算传入字符串中元音字母的个数
    :param st: 传入的字符串
    :return: 元音字母个数
    """
    count = 0
    for char in st:
        if char in "aeiouAEIOU":
            count += 1
    return count

print(vowel_count("hello wore "))


# 3. 定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数), 并返回。
def calc_score(score_list) :
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)
    :param score_list: 高考成绩列表
    :return: 最高分、最低分、平均分
    """
    max_score = max(score_list)
    min_score = min(score_list)
    average_score = round(sum(score_list) / len(score_list) , 1)
    return max_score, min_score, average_score

s_list = [540,550,600,605,490,499,505,502]
print(f"最高分为 {calc_score(s_list)[0]} \n最低分为 {calc_score(s_list)[1]} \n平均分为 {calc_score(s_list)[2]}")