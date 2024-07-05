from eskmo import api

cst = api.const

# Order
@api.event.order.send_success
def onOrderSendSuccess(data):
    print("Order send success", data)

@api.event.order.placed_success
def onOrderPlaced(data):
    print("Order placed success", data)

@api.event.order.changed
def onOrderChanged(data):
    print("Order Changed", data)

# order.cancel_success 本來就沒有實作, 透過 order.changed 監控
@api.event.order.cancel_fail
def onCancelOrderFailed(data):
    print(f"Cancel Order Failed: '{data}'")
    
# MIT Order
@api.event.mit_order.send_success
def onMITOrderSendSuccess(data):
    print(f"MIT order send success: {data}")

@api.event.mit_order.placed_fail
def onMITOrderPlacedFail(data):
    print("mit order place fail", data)    

@api.event.mit_order.changed
def onMITOrderChanged(data):
    print("Smart Order Changed", data)

@api.event.mit_order.cancel_fail
def onMITCancelOrderFailed(data):
    print(f"Cancel MIT Order Failed", data)