def register(user_info):
    while True:
        username = input("请输入用户名：")
        # 当flag为True时，用户不存在
        flag = True
        for user in user_info:
            if user["username"] == username:
                flag = False
                break
        if flag:
            print("用户名合法")
            break
        else:
            print("用户已存在，请重新输入用户名")

    while True:
        # 确保用户密码未被注册过
        password1 = input("请输入用户密码")
        if password1.isdigit():
            print("密码必须由字母和数字组成, 不能全部是数字")
            continue
        elif password1.isalpha():
            print("密码必须由字母和数字组成, 不能全部是字母")
            continue
        elif password1.isalnum():
            print("密码合法")

        else:
            print("密码必须由字母和数字组成, 不能是其他字符")
            continue
        password2 = input("请确认用户密码")
        if password1 == password2:
            print("两次用户密码确认成功")
            break
        else:
            continue
    # user_info[username] =password1

    with open("../../db.txt", "a", encoding="utf-8") as write_f:
        user = username + ":" + password1 + "\n"
        write_f.write(user)
