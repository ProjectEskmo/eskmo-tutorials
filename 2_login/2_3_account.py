from starter import *
from eskmo import api
from eskmo import Logger, User, Account, StockAccount

@api.start
def main():
    Logger.show = True
    user: User = api.login(userId="A123456789", password="*************", tag="me")

    # 2.3.1. 帳戶列表 (含證券, 期貨帳戶)
    accounts: dict[str, Account] = user.accounts
    print(accounts)

    user.accounts["egerger"]

    # 2.3.2. 主要帳戶 (預設證券帳戶第一戶)
    account: Account = user.account
    print(account)

    # 2.3.3. 設定主要帳戶
    user.set_main_account(account.name)
    print(user.account)

    # 2.3.4. 取得帳戶號碼
    accountIds = user.get_account_ids()
    print(accountIds)

    # 2.3.5. 更新帳戶名稱
    account_info = ("91829808465", "主帳戶")
    user.update_account_name(*account_info)
    account: StockAccount = user.accounts["主帳戶"]

    
if __name__ == "__main__":
    main()
