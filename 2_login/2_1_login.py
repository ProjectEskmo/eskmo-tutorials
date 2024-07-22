import csv
from datetime import datetime
from eskmo import api
from eskmo import User
from eskmo import LoginStartResult, LoginSuccessResult, APIExecuteErrorResult, LoginFailResult, LoginProgressNotifyResult

starttime = 0

def append_number_to_csv(number):
    with open("login_speed_microsecs.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([number])

@api.event.user.login_start
def onLoginStart(data: LoginStartResult):
    global starttime
    starttime = datetime.now()
    print(data)
    # LoginStartResult(event='LoginStart', type='MultiLogin', connection=2)    

@api.event.user.login_success
def onLoginSuccess(data: LoginSuccessResult):
    global starttime
    t = (datetime.now() - starttime).seconds
    print(f"[ LOGIN DURATION ] {t}s")
    append_number_to_csv(t)
    print(data)      
    # LoginSuccessResult(event='LoginSuccess', api='SKCOM', userId='A123456789') 

@api.event.user.login_progress_notify
def onLoginProgressNotify(data: LoginProgressNotifyResult):
    print(data)
    # LoginProgressNotifyResult(event='LoginProgressNotify', progress='SKCOM API 已就位，可以開始使用')

# @api.event.user.login_fail
# def onLoginFailed(data: LoginFailResult):
#     print(f"Login failed: {data}")
#     # LoginFailResult(event='LoginFail', auto_relogin=False, account='rgegrerg', error_code=507, errors=['507: 帳號或憑證錯誤'])

# @api.event.api.execute_error
# def onAPIExecuteError(data: APIExecuteErrorResult):
#     print(f"API execute error:: {data}")
#     # APIExecuteErrorResult(event='SkcomExecFail', phase='AfterExec', function='SKCenterLib_Login', error_code=507, errors=['帳號或憑證錯誤'])

@api.start
def main():
    api.logger.show = True
    
    # 2.1.1 登入
    tag = "爸爸"
    userId = "A123456789"
    password = "*************"
    user: User = api.login(userId=userId, password=password, tag=tag)
    print(user)

    # 2.1.2. 使用者列表
    users = api.users # get_all_users()
    print(users)

    user.cancelMITOrderBySmartKeyNo("12230849")

    
if __name__ == "__main__":
    main()
