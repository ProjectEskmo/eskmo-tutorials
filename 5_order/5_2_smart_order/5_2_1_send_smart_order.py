import time
from starter import *
from eskmo import api
from eskmo import Logger, User, Stock
from eskmo import MITOrderSendSuccessResult, MITOrderSendStartResult, MITOrderSendFailResult

cst = api.const
    
# MIT Order
@api.event.mit_order.send_start
def onMITOrderSendStart(data: MITOrderSendStartResult):
    print(f"MIT order send start: '{data}'")
    # MITOrderSendStartResult(account='91829808465', symbol='2888', buysell='yoyo', price='', qty=-1, trigger_price='', trigger_dir=2, order_flag=0, price_type=2, order_type=0, is_pre_trade_risk_controlled=False, is_gtc_order=False, gtc_date='', gtc_end_by=1, callbackId=0)

@api.event.mit_order.send_fail
def onMITOrderSendFail(data: MITOrderSendFailResult):
    print("MIT order send fail", data)
    # MITOrderSendFailResult(account='91829808465', symbol='2888', buysell='yoyo', price='', qty=-1, trigger_price='', trigger_dir=2, order_flag=0, price_type=2, order_type=0, is_pre_trade_risk_controlled=False, is_gtc_order=False, gtc_date='', gtc_end_by=1, callbackId=None, errors=["error..."], error_code=None)    

@api.event.mit_order.send_success
def onMITOrderSendSuccess(data: MITOrderSendSuccessResult):
    print(f"MIT order send success: {data}")
    # MITOrderSendSuccessResult(account='91829808465', symbol='2888', buysell=0, price=7.5, qty=1, trigger_price=7.5, trigger_dir=2, order_flag=0, price_type=2, trade_type=0, is_pre_trade_risk_controlled=False, is_gtc_order=False, gtc_date='', gtc_end_by=1, state='Pending', created=datetime.datetime(2024, 4, 17, 11, 15, 36, 939000), callbackId=0, threadId='31152')

@api.event.mit_order.placed_fail
def onMITOrderPlacedFail(data):
    print("mit order placed fail", data)  
    #  MITOrderPlaceFailResult(threadId='6092', order=None, errors=["'2888' MIT 委託失敗: 國內證券超光速MIT最後收單時間為13:25:00,超過收單時間或非交易時間請確認!"])

@api.event.mit_order.placed_success
def onMITOrderPlacedSuccess(data):
    print("mit order placed success", data)  
    #  MITOrderPlaceSuccessResult(threadId='15616', order=PlacedMITOrderResult(account='91829808465', symbol='2888', buysell=0, price=7.5, qty=1, trigger_price=7.5, trigger_dir=2, order_flag=0, price_type=2, trade_type=0, is_pre_trade_risk_controlled=False, is_gtc_order=False, gtc_date='', gtc_end_by=1, seqNo='11891358')  

@api.event.mit_order.changed
def onMITOrderChanged(data):
    print("Smart Order Changed", data)
    # MITOrderChangedResult(count=8, order=MITOrderStatus(reply=MITReply(user_id='A123456789', trade_kind='8', market='TS', type='1', exchange_code='0', smart_key_no='11894570', pub_seq_no='2', broker='9182', account='9808465', sub_account='0000000', exchange_id='TSE', seq_no='1685000010880', o_seq_no='1685000010880', order_no='', symbol='2888', buysell_str='B', order_type='0', order_price_mark='7', order_price='7.5', price_type='2', order_cond='0', qty='1', trigger_price='7.5', trigger_time='', trigger_dir='2', day_trade=None, created=datetime.datetime(1970, 1, 21, 3, 55, 30, 480000), sale_no='8890', user_ip='27.51.90.228', trade_source='y', status='34', error_msg='N', message='已加入洗價', updated=datetime.datetime(1970, 1, 21, 3, 55, 30, 478000), universal_msg='', base_price='0', market_deal_trigger='', num=8, buysell='買'), is_closed=False, price='7.5', volume=1000, volume_remain=1000, volume_cancel=0, volume_deal=0))

@api.event.mit_order.cancel_fail
def onMITCancelOrderFailed(data):
    print(f"Cancel MIT Order Failed", data)

@api.start
def main():
    Logger.show = True
    user: User = api.login(userId="A123456789", password="*************", tag="me")

    # 5.2.1.1. 送出 MIT 委託
    stock: Stock = api.stocks["2888"]
    smartOrder = stock.smartOrder.mit(cst.ORDER.ACTION.BUY, 8, 1, 8).send(user.id) # 
    print(smartOrder) 
    # MITOrder(status='Placed', seqNo='11755088', reply='11755088')
    # or
    # MITOrder(status='Error', errors='["'2888' MIT 委託失敗: 國內證券超光速MIT最後收單時間為13:25:00,超過收單時間或非交易時間請確認!"]')
    
    
if __name__ == "__main__":
    main()

