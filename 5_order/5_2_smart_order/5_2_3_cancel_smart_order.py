from starter import *
from eskmo import api
from eskmo import Logger, User, Stock

cst = api.const

@api.start
def main():
    Logger.show = True
    user: User = api.login(userId="A123456789", password="*************", tag="me")

    # 5.2.3.1. MIT 委託刪單
    stock: Stock = api.stocks["2888"]
    smartOrder = stock.smartOrder.mit(cst.ORDER.ACTION.BUY, 7.5, 1, 7.5).send(user.id)
    print(smartOrder) 
    # MITOrder(status='Placed', seqNo='11755516', reply='11755516')
    smartOrder.cancel()
    print(smartOrder)
    # MITOrder(status='Canceled', seqNo='11755516')
    
    
if __name__ == "__main__":
    main()

