
def menu():
    user_info = []
    menu = '''欢迎来到彩虹洗脚城
    1. 登录
    2. 注册
    3. 洗脚
    4. 洗澡
    5. 按摩
    6. 退出'''
    with open("./db.txt", "r", encoding="utf-8") as read_f:
        for line in read_f.readlines():
            username = line.split(":")[0].strip()
            password = line.split(":")[1].strip()
            user_info.append({"username":username, "password":password})
    print(user_info)
    print(menu)
    user_select = int(input("请输入您的选择："))
    return user_info, user_select
