import csv
from datetime import datetime
import time
from eskmo import api    
from eskmo import User, Stock

cst = api.const
api.logger.enable()

starttime = 0

def append_number_to_csv(number):
    with open("speed_microsecs.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([number])

# Order
@api.event.order.send_start
def onOrderSendStart(data):
    global starttime
    starttime = datetime.now()
    print(f"Order send start: {data}")
    # OrderSendStartResult(account='1234567890', symbol='2888', exchange=0, period=0, order_flag=0, buysell=0, price=7.5, qty=1, price_type=0, trade_type=2, callbackId=0)
    
@api.event.order.send_fail
def onOrderSendFail(data):
    print(f"Order send fail: {data}")
    # OrderSendFailResult(account='1234567890', symbol='2888', exchange=0, period=0, order_flag=0, buysell='yoyo', price=-7.5, qty=-1, price_type=0, trade_type=2, callbackId=0, errors=["無效送單: Failed to prepare inputs before executing 'SendStockOrder': invalid literal for int() with base 10: 'yoyo'."], error_code=None)
    
@api.event.order.send_success
def onOrderSendSuccess(data):
    print(f"Order send success: {data}")
    # OrderSendSuccessResult(account='1234567890', symbol='2888', exchange=0, period=0, order_flag=0, buysell=0, price=-7.5, qty=-1, price_type=0, trade_type=2, state='Pending', created=datetime.datetime(2024, 4, 16, 16, 42, 50, 663000), callbackId=0, threadId='38448')

@api.event.order.placed_success
def onOrderPlacedSuccess(data):
    print(f"Order placed success: {data}")
    # OrderPlaceSuccessResult(threadId='9728', order=PlacedOrderResult(account='1234567890', symbol='2888', exchange=0, period=0, order_flag=0, buysell=0, price=7.5, qty=1, price_type=0, trade_type=2, seqNo='4304171180151')

@api.event.order.placed_fail
def onOrderPlacedFail(data):
    print(f"Order placed fail: {data}")
    # OrderPlaceFailResult(threadId='14196', order={'pid': 26940, 'bstrFullAccount': '1234567890', 'bstrStockNo': '2888', 'sPrime': 0, 'sPeriod': 0, 'sFlag': 0, 'sBuySell': 0, 'bstrPrice': -7.5, 'nQty': -1, 'nTradeType': 0, 'nSpecialTradeType': 2, 'OrderState': 'Pending', 'APICallbackID': 0, 'StartTime': 1713258953597, 'OrderFrom': 'BasicOrder', 'PendingNewThreadID': '14196', 'ThreadID': '14196'}, errors=["ThreadID=14196 委託不明, 可能功能尚未實作 (未知nCode=106): 'price -7.5 error 13493'"], error_code=106)
     
@api.event.order.changed
def onOrderChanged(data):
    global starttime
    print("Order Changed", data)
    endtime = datetime.now()
    while True:
        if starttime != 0:
            break
    duration = endtime - starttime
    append_number_to_csv(duration.microseconds)
    print(f"[ TIME DURATION ] {duration.microseconds} microsec(s).")
    print(f"[ TIME DURATION ] {duration.microseconds} microsec(s).")
    print(f"[ TIME DURATION ] {duration.microseconds} microsec(s).")
    # OrderChangedResult(count=29, order=OrderStatus(reply=Reply(num=29, key_no='4304171126614', market='TS', type='委託', status='成功', broker='9182', cust_no='9808465', buysell_info='B00R2', exchange_id='TW', symbol='2888', strike_price='', book_no='T00LC', price='7.5000', numerator='', denominator='', price_lags=[ReplyPrice(price='', numerator='', denominator=''), ReplyPrice(price='', numerator='', denominator='')], volume='1000', before_qty='0', after_qty='1000', date_str='20240417', time_str='10:05:56', ok_seq='', sub_id='0000000', sale_no='8890', agent='y', trade_date='20240417', msg_no='1010000422480', pre_order='A', commodity_lags=[ReplyCommodity(com_id='2888', year_month='', strike_price=''), ReplyCommodity(com_id='', year_month='', strike_price='')], execution_no='', price_symbol='', reserved='', order_effective='', call_put='', order_seq='', error_msg='', cancel_order_mark_by_exchange='', exchange_tandem_msg='', seq_no='4304171126614', buysell='買', trade_type='現股', order_type='ROD', price_type='限價'), is_closed=False, price='7.5000', volume=1000, volume_remain=1000, volume_cancel=0, volume_deal=0))

@api.event.order.cancel_fail
def onCancelOrderFailed(data):
    print(f"Cancel Order Failed", data)
    # OrderCancelFailResult(errors=['已刪單: [073]取消失敗，此委託已取消(KEY)(0)'], error_code=None, order_class='BasicOrder', cancel_action='CancelOrderBySeqNo', seq_no='4304171180151', is_already_cancelled=False)


@api.start
def main():
    user: User = api.login(userId="A123456789", password="*************", tag="me")

    # 5.1.1.1. 送出一般委託
    stock: Stock = api.stocks["2888"]
    while True:
        order = stock.order(cst.ORDER.ACTION.BUY, 9.18, 1).send(user.id)
        
        print(f"order: {order}")
        print(f"order.price: {order.price}")
        print(f"order.status: {order.status}")
        print(f"order.qty: {order.qty}")
        print(f"order.deal_qty: {order.deal_qty}")
        print(f"order.remain_qty: {order.remain_qty}")
        print(f"order.canceled_qty: {order.canceled_qty}")
        time.sleep(5)

    api.exit()
    
    
if __name__ == "__main__":
    main()


