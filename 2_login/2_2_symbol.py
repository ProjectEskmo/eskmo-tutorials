from starter import *
from eskmo import api
from eskmo import Logger, Stocks, Stock

@api.start
def main():
    Logger.show = True
    api.login(userId="A123456789", password="*************", tag="me")

    # 2.2.1. 商品檔列表
    stocks: Stocks = api.stocks
    print(stocks)

    # 2.2.2. 個別商品檔
    stock: Stock = stocks["2330"]
    print(stock)

    
if __name__ == "__main__":
    main()
