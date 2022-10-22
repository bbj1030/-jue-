from wash_foot.user.login import login
from wash_foot.user.register import register
from wash_foot.resources.menu import menu
from wash_foot.yule.xizao import xizao
from wash_foot.yule.xijiao import xijiao
from wash_foot.yule.anmo import anmo
from wash_foot.resources.settings import login_flag

if __name__ == '__main__':

    while True:
        # 打印菜单
        user_info, user_select = menu()

        if user_select == 1:
            login_flag = login(user_info)

        elif user_select == 2:
            register(user_info)

        elif user_select == 3:
            xijiao(login_flag)
        elif user_select == 4:
            xizao(login_flag)
        elif user_select == 5:
            anmo(login_flag)
        elif user_select == 6:
            print("退出")
            break
        else:
            print("输入错误！！！")
else:
    print("欢迎导入洗脚城代码")