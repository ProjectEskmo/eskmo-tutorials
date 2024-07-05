from eskmo import api

@api.event.quote.subscribe_fail
def onSubscribeQuoteFail(data):
    print(data)

@api.event.tick.subscribe_fail
def onSubscribeTickFail(data):
    print(data)

@api.event.best5.subscribe_fail
def onSubscribeTickFail(data):
    print(data)    