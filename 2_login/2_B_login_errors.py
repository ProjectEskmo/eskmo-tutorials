from eskmo import api

@api.event.user.login_fail
def onLoginFailed(data):
    print("Login failed", data)

@api.event.api.execute_error
def onAPIExecuteError(data):
    print("API execute error", data)