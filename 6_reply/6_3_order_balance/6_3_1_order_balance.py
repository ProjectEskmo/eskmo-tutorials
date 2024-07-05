from starter import *
from eskmo import api
from eskmo import Logger, User, Stock, StockBalance, StocksBalance

cst = api.const

@api.start
def main():
    Logger.show = True
    user: User = api.login(userId="A123456789", password="*************", tag="me")

    # 6.3.1.1. 拿指定商品的 pos
    stock: Stock = api.stocks["2888"]
    balance: StockBalance = stock.position(user.id)
    print(f"現股: {balance.stock}")
    print(f"融資: {balance.margin}")
    print(f"融券: {balance.short}")
    print(f"先賣: {balance.daytrade_short}")
    # 現股: {'昨餘': 0, '委買': 0, '買成': 0, '委賣': 0, '賣成': 0}
    # 融資: {'昨餘': 0, '委買': 0, '買成': 0, '委賣': 0, '賣成': 0}
    # 融券: {'昨餘': 0, '委買': 0, '買成': 0, '委賣': 0, '賣成': 0}
    # 先賣: {'昨餘': 0, '委買': 0, '買成': 0, '委賣': 0, '賣成': 0}

    # 6.3.1.2. 拿全部商品的 pos
    balances: StocksBalance = api.stocks.position(user.id)
    balance: StockBalance = balances["2401"]
    print(balance.all)
    # {'現': {'昨餘': 0, '委買': 0, '買成': 0, '委賣': 0, '賣成': 0}, 
    #  '資': {'昨餘': 0, '委買': 0, '買成': 0, '委賣': 0, '賣成': 0}, 
    #  '券': {'昨餘': 0, '委買': 0, '買成': 0, '委賣': 0, '賣成': 0}, 
    #  '先賣': {'昨餘': 0, '委買': 0, '買成': 0, '委賣': 0, '賣成': 0}}


    
if __name__ == "__main__":
    main()


