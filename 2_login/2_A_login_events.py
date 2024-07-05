from eskmo import api

@api.event.user.login_start
def onLoginStart(data):
    print("Login Start", data)

@api.event.user.login_success
def onLoginSuccess(data):
    print("Login Success", data)       

@api.event.user.login_progress_notify
def onLoginProgressNotify(data):
    print("Login Progress Notify", data)
