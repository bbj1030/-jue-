def login(user_info):
    while True:
        username = input("请输入用户名：")
        # 当flag为True时，用户不存在
        flag = True
        for user in user_info:
            if user["username"] == username:
                flag = False
                break
        if flag:
            print("用户不存在")
        else:
            print("用户存在")
            break

    while True:
        password = input("请输入密码")
        # 当flag为True时代表密码输入正确
        flag = False
        for user in user_info:
            if user["username"] == username and user["password"] == password:
                print("登录成功")
                flag = True
                break
        if flag:
            return True
        else:
            print("密码输入错误！！")
            continue
