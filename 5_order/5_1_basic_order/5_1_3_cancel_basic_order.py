from starter import *
from eskmo import api
from eskmo import Logger, User, Stock

cst = api.const

@api.start
def main():
    Logger.show = True
    user: User = api.login(userId="A123456789", password="*************", tag="me")

    # 5.1.3.1. 一般委託刪單
    stock: Stock = api.stocks["2888"]
    order = stock.order(cst.ORDER.ACTION.BUY, 7.5, 1).send(user.id)
    print(order)
    # Order(status='Placed', seqNo='4304081356311', reply='1010000649939')
    order.cancel()
    print(order)
    # Order(status='Canceled', seqNo='4304081356311')
    
    
if __name__ == "__main__":
    main()


