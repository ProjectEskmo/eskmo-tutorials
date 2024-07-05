from starter import *
from eskmo import api
from eskmo import Logger

cst = api.const

@api.event.user.login_fail
def onLoginFailed(data):
    print("登入失敗", data[cst.DATA.ERRORS])
    # ['507: 帳號或憑證錯誤']

@api.start
def main():
    Logger.show = True

    api.login(userId="wrongId", password="*****")

if __name__ == "__main__":
    main()
