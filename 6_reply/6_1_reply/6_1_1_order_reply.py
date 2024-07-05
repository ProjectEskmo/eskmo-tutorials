from starter import *
from eskmo import api
from eskmo import Logger, User, Stock, StockOrder, StockOrders

cst = api.const

@api.start
def main():
    Logger.show = True
    user: User = api.login(userId="A123456789", password="*************", tag="me")

    # 6.1.1.1. 從送出的 Order 拿 Reply
    stock: Stock = api.stocks["2888"]
    order: StockOrder = stock.order(cst.ORDER.ACTION.BUY, 7.5, 1).send(user.id)
    print(order)
    # Order(status='Placed', seqNo='4304091286057', reply='1010000646899')
    reply = order.reply
    print(reply)
    # replys
    print(order.replys)
    # # TODO 要包 reply

    # 6.1.1.2. 從 Orders 中的 Order 拿 Reply 和歷史 Replys
    ## A. 指定商品
    stock: Stock = api.stocks["2888"]
    orders: StockOrders = stock.orders(user.id)
    # (i) 遍歷一遍 2888 的 Reply
    for order in orders:
        print(f"A. Reply: {order.reply}")    
        print(f"A. Replys: {order.replys}")
    # (ii) 指定 seqNo
    seqNo = "4304091539554"
    order: StockOrder = orders[seqNo]
    print(f"A. ({seqNo}) Reply: {order.reply}")    
    print(f"A. ({seqNo}) Replys: {order.replys}")

    ## B. 全部商品
    orders: StockOrders = api.stocks.orders(user.id)
    # (i) 遍歷一遍所有 Reply
    for order in orders:
        print(f"B. Reply: {order.reply}")    
        print(f"B. Replys: {order.replys}")
    # (ii) 指定 seqNo
    seqNo = "4304091539554"
    order: StockOrder = orders[seqNo]
    print(f"B. ({seqNo}) Reply: {order.reply}")    
    print(f"B. ({seqNo}) Replys: {order.replys}")
    
if __name__ == "__main__":
    main()


