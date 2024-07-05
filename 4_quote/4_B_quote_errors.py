from eskmo import api

# Subscribe/Unsubscribe
@api.event.quote.subscribe_fail
def onQuoteSubscribeFail(data):
    print("Quote subscribe fail", data)

@api.event.quote.unsubscribe_fail
def onQuoteUnsubscribeFail(data):
    print("Quote unsubscribe fail", data)