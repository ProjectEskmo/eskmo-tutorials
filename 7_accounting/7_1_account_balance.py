import time
from starter import *
from eskmo import api
from eskmo import Logger, User, Account

cst = api.const

@api.start
def main():
    Logger.show = True
    user: User = api.login(userId="A123456789", password="*************", tag="me")

    # 7.1. 取得 account balance
    account: Account = user.account
    print(f"Balance: {account.balance}") 
    print(f"Summary: {account.balance.summary}")
    print(f"Unrealized: {account.balance.summary.unrealized} (updated={account.balance.updated})")
    
    # 7.2. 更新 Account balance (有 API 限制, 需稍等否則會沒辦法更新) 
    time.sleep(5)
    account.balance.update(type="summary", pnl="unrealized")
    print(f"Summary: {account.balance.summary.unrealized} (updated={account.balance.updated})")
    # Summary: {'臺幣': {'股票名稱': '', '股票代號': '', '幣別': '臺幣', '交易種類': '9999', '庫存股數': '0', 
    # '市價': '0.00', '今日市價漲跌': '0.00', '市值': '194460.00', '淨值': '193956.00', '損益': '-4281.00', 
    # '平均買進(券賣)成本': '0.00', '付出成本': '198237.00', '成交價金': '198140.00', '手續費': '97.00', 
    # '預估手續費': '277.00', '交易稅': '0.00', '預估交易稅': '227.00', '融資自備款/融券保證金': '0', '融資金/擔保品': '0', '預估利息': '0', '股息': '0.00', '試算報酬率': '0.00', '未知成本股數': '0', '備註': '', '有無詳細資料': 'N', '排序序號': '3', '交易種類代號': '0', '損益兩平點': '0.000000', 'LOGIN_ID': 'A123456789', 'ACCOUNT_NO': '1234567890'}, '人民': {'股票名稱': '', '股票代號': '', '幣別': '人民', '交易種類': '9999', '庫存股數': '0', '市價': '0.00', '今日市價漲跌': '0.00', '市值': '0.00', '淨值': '0.00', '損益': '0.00', '平均買進(券賣)成本': '0.00', '付出成本': '0.00', '成交價金': '0.00', '手續費': '0.00', '預估手續費': '0.00', '交易稅': '0.00', '預估交易稅': '0.00', '融資自備款/融券保證金': '0', '融資金/擔保品': '0', '預估利息': '0', '股息': '0.00', '試算報酬率': '0.00', '未知成本股數': '0', '備註': '', '有無詳細資料': 'N', '排序序號': '4', '交易種類代號': '0', '損益兩平點': '0.000000', 'LOGIN_ID': 'A123456789', 'ACCOUNT_NO': '1234567890'}} (updated=2024-04-10 11:51:53.025944)

    
if __name__ == "__main__":
    main()


