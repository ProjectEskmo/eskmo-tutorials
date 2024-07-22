import csv
from datetime import datetime
from eskmo import api
from eskmo import Stock
from eskmo import SubscribeFailResult, SubscribeStartResult, SubscribeSuccessResult

api.logger.enable()

def append_number_to_csv(number):
    with open("quote_speed_microsecs.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([number])

@api.start
def main():
    api.login(userId="A123456789", password="*************", tag="王睿麒")

    # 4.1.1. 透過 stock 訂閱
    # for code in api.stocks.keys():
    #     stock: Stock = api.stocks[code]
    #     stock.subscribe_quote() 

    stock: Stock = api.stocks["2609"]
    stock.subscribe_quote() 

@api.event.quote.subscribe_start
def onSubscribeStart(data: SubscribeStartResult):
    print(f"[onSubscribeStart] symbol: {data.symbol}")

@api.event.quote.subscribe_fail
def onSubscribeFail(data: SubscribeFailResult):
    print(f"[onSubscribeFail] error_code: {data.error_code}")

@api.event.quote.subscribe_success
def onSubscribeSuccess(data: SubscribeSuccessResult):   
    print(f"[onSubscribeSuccess] Messages: {data.messages}")

# 4.1.2. 透過裝飾器獲得事件通知
@api.event.quote.bidask_changed
def onBidAskChanged(data):
    append_number_to_csv(datetime.now().timestamp())
    print(f"[ALL] Quote:: {data}")

@api.event.quote.price_changed
def onPriceChanged(data):
    print(f"onPriceChanged:: Quote:: {data}")

@api.event.quote.tick_changed
def onTickChanged(data):
    print(f"onTickChanged:: Quote:: {data}")   
    # Quote(idx=(0, 29898), market='Stock', decimal=2, sector=15, symbol='2609',
    #  name='陽明', high=45.65, open=45.0, low=44.25, close=45.2, tickQty=153,
    #  ref=45.2, bid=45.2, bidQty=137, ask=45.25, askQty=6, totalBidQty=12550,
    #  totalAskQty=9206, futureOI=0, totalQty=21909, yestQty=14819, up=49.7,
    #  down=40.7, simulate=0, dayTradeType=2, tradingDay=20240415) 

# # 4.1.3. 透過裝飾器訂閱與綁定事件
# @api.event.quote.bidask_changed(symbol="2330")
# def onBidAskChanged2330(quote):
#     print(f"[2330] Quote:: {quote}")

# # 4.1.4. 透過裝飾器訂閱多檔與綁定多檔事件
# @api.event.quote.bidask_changed(symbol=["2330", "2601"])
# def onBidAskOneOfTwoChanged(quote):
#     print(f"[2330, 2601] Quote:: {quote}")

    
if __name__ == "__main__":
    main()


