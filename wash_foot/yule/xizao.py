from wash_foot.resources.login_required import login_required

@login_required
def xizao(login_flag):
    print("洗澡")