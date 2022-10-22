
def login_required(func):
    def inner(login_flag):
        if login_flag:
            print("贵宾一位".center(40, "*"))
            func(login_flag)
        else:
            print("请先登录")
    return inner
