from starter import *
from eskmo import api
from eskmo import Logger, Stock, Best5

@api.start
def main():
    Logger.show = True
    api.login(userId="A123456789", password="*************", tag="me")

    # 4.3.1. 透過 stock 訂閱 Best5
    stock: Stock = api.stocks["2409"]
    stock.subscribe_best5() 

    # stock2330 = api.stocks["2330"]
    # stock2330.unsubscribe_best5()


# 4.3.2. 透過裝飾器獲得 Best5 事件通知
@api.event.best5.notify
def onBest5Notify(best5: Best5):
    print(f"[ALL] Best5:: {best5.bid[0].price}, {best5.bid[0].qty}, {best5}")
    # Best5(code='2409', bid=[OrderBookLevel(price=17.45, qty=924),
    #          OrderBookLevel(price=17.4, qty=737), 
    #          OrderBookLevel(price=17.35, qty=482),
    #          OrderBookLevel(price=17.3, qty=415),
    #          OrderBookLevel(price=17.25, qty=198)],
    #    ask=[OrderBookLevel(price=17.5, qty=697),
    #         OrderBookLevel(price=17.55, qty=592),
    #         OrderBookLevel(price=17.6, qty=211),
    #         OrderBookLevel(price=17.65, qty=304),
    #         OrderBookLevel(price=17.7, qty=189)],
    #    simulate=0)

# [ALL] Best5:: {'nPtr': 9547, 'lDate': '2024/04/03', 'lTimehms': '14:30:00',
# 'lTimemillismicros': 0, 'TickTimestamp': 1712125800.0, 'nBid': 0.0,
# 'nAsk': 0.0, 'nClose': 780.0, 'nQty': 58, 'nSimulate': 0, 'SymbolCode': '2330'}

# # 4.3.3. 透過裝飾器訂閱 Best5 與綁定事件
# @api.event.best5.notify(symbol="2330")
# def onBest5Notify2330(best5):
#     print(f"[2330] Best5:: {best5}")

# # 4.3.4. 透過裝飾器訂閱多檔 Best5 與綁定多檔事件
# @api.event.best5.notify(symbol=["2330", "2601"])
# def onBest5NotifyTwo(best5):
#     print(f"[2330, 2601] Best5:: {best5}")


if __name__ == "__main__":
    main()


