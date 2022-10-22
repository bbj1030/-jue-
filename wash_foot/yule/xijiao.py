from wash_foot.resources.login_required import login_required


@login_required
def xijiao(login_flag):
    print("洗脚")