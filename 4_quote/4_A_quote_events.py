from eskmo import api

cst = api.const
STOCK = cst.MARKET.STOCK

# Subscribe/Unsubscribe
@api.event.quote.subscribe_success
def onQuoteSubscribeSuccess(data):
    print("Quote subscribe success", data)

@api.event.quote.unsubscribe_start
def onQuoteUnsubscribeStart(data):
    print("Quote unsubscribe Start", data)

# Quote
@api.event.quote.price_changed(symbol="2330", market=STOCK)
def onPriceChanged(data):
    print("Price Changed", data)

@api.event.quote.bidask_changed(symbol="2330", market=STOCK)
def onPriceChanged(data):
    print("BidAsk Changed", data)

@api.event.quote.tick_changed(symbol="2330", market=STOCK)
def onPriceChanged(data):
    print("Tick Changed", data)    

# Tick    
@api.event.tick.notify(symbol="2330", market=STOCK)
def onTickNotify(tick):
    print("On Tick Notify", tick)

# Tick History
@api.event.tick.history_notify(symbol="2330", market=STOCK)
def onTickHistoryNotify(tick):
    print("Tick History", tick)

# Best5    
@api.event.best5.notify(symbol="2330", market=STOCK)
def onBest5Notify(tick):
    print("Best5 Notify", tick)