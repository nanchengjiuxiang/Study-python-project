import json

# 写入json数据文件
user = {
    "name" : "Nqx",
    "age" : 18,
    "gender" : "female",
}
with open("Resources/user.json", "w", encoding="utf-8") as f:
    # 写入json数据
    json.dump(user, f, ensure_ascii=False, indent=4)


# 读取json数据文件
with open("Resources/user.json", "r", encoding="utf-8") as f:
    content = json.load(f)
    print(content)
    print(type(content))