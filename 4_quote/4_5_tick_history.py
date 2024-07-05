from starter import *
from eskmo import api
from eskmo import Logger, Stock
@api.start
def main():
    Logger.show = True
    api.login(userId="A123456789", password="*************", tag="me")

    # REMIND 取得歷史 history 會取消當前訂閱並再訂閱, 會打斷已訂閱商品檔的 tick notify
    # 最佳實踐是在訂閱時同時監聽 tick_history_notify 保存歷史 tick

    # 4.5.1. 透過 stock 取得歷史 Tick
    stock: Stock = api.stocks["2409"]

    ticks = stock.tick_history() 
    for idx, tick in enumerate(ticks):
        if idx % 100 == 99:
            print(f"({idx+1}) tick:: {tick}")
    
    # (100) tick:: {'nPtr': 99, 'lDate': '2024/04/03', 'lTimehms': '08:43:58', 'lTimemillismicros': 677961, 'TickTimestamp': 1712105038.961677, 'nBid': 18.0, 'nAsk': 18.05, 'nClose': 18.0, 'nQty': 192, 'nSimulate': 1, 'SymbolCode': '2409'}       
    # (200) tick:: {'nPtr': 199, 'lDate': '2024/04/03', 'lTimehms': '08:55:31', 'lTimemillismicros': 754799, 'TickTimestamp': 1712105731.799754, 'nBid': 17.95, 'nAsk': 18.0, 'nClose': 17.95, 'nQty': 352, 'nSimulate': 1, 'SymbolCode': '2409'}     
    # (300) tick:: {'nPtr': 299, 'lDate': '2024/04/03', 'lTimehms': '09:01:36', 'lTimemillismicros': 506495, 'TickTimestamp': 1712106096.495506, 'nBid': 17.75, 'nAsk': 17.8, 'nClose': 17.75, 'nQty': 6, 'nSimulate': 0, 'SymbolCode': '2409'}    

    # 4.5.2. 透過訂閱取得歷史 Tick
    stock.tick_history(isAsync=True) 

@api.event.tick.history_notify
def onTickHistoryNotify(tick):
    print(f"[ALL] Tick history:: {tick}")
# [ALL] Tick history:: {'nPtr': 3912, 'lDate': '2024/04/03', 'lTimehms': '13:29:11',
# 'lTimemillismicros': 836960, 'TickTimestamp': 1712122151.960836, 'nBid': 17.75,
# 'nAsk': 17.8, 'nClose': 17.75, 'nQty': 1717, 'nSimulate': 1, 'SymbolCode': '2409'}

# 4.5.3. 透過事件取得特定商品歷史 Tick
@api.event.tick.history_notify(symbol="2330")
def onTickHistoryNotify2330(tick):
    print(f"[2330] Tick history:: {tick}")

# 4.5.4. 透過事件取得多檔商品歷史 Tick
@api.event.tick.history_notify(symbol=["2330", "2601"])
def onTickHistoryNotifyTWO(tick):
    print(f"[2330, 2601] Tick history:: {tick}")

if __name__ == "__main__":
    main()


