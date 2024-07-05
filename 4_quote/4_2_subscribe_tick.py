from starter import *
from eskmo import api
from eskmo import Logger, Stock, Tick

@api.start
def main():
    Logger.show = True
    api.login(userId="A123456789", password="*************", tag="me")

    # 4.2.1. 透過 stock 訂閱 Tick
    stock: Stock = api.stocks["2609"]
    stock.subscribe_tick() 


# # 4.2.2. 透過裝飾器獲得 Tick 事件通知
@api.event.tick.notify
def onTickNotify(tick: Tick):
    print(f"[ALL] Tick:: {tick.date_str} {tick.time_str} BID: {tick.bid}, QTY: {tick.qty}")
# [ALL] Tick(count=1759, date_str='2024/04/16', time_str='10:01:39', ms_str=344385, timestamp=1713232899.385344, time=datetime.datetime(2024, 4, 16, 10, 1, 39, 385344), symbol='2609', bid=44.15, ask=44.2, close=44.15, qty=3, simulate=False)

# # # 4.2.3. 透過裝飾器訂閱 Tick 與綁定事件
# @api.event.tick.notify(symbol="2330")
# def onTickNotify2330(tick):
#     print(f"[2330] Tick:: {tick}")

# # # 4.2.4. 透過裝飾器訂閱多檔 Tick 與綁定多檔事件
# @api.event.tick.notify(symbol=["2330", "2601"])
# def onTickNotifyTwo(tick):
#     print(f"[2330, 2601] Tick:: {tick}")
    
if __name__ == "__main__":
    main()


