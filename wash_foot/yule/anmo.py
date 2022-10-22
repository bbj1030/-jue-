from wash_foot.resources.login_required import login_required

@login_required
def anmo(login_flag):
    print("按摩")