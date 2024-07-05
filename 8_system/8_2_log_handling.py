import time
from starter import *
from eskmo import api
from eskmo import Logger, User, Account

@api.event.log.error
def onLogError(data):
    print(f"Warning log: {data}")
    # LogResult(level='ERROR', time_str='2024-04-17 13:49:23.264653', time=datetime.datetime(2024, 4, 17, 13, 49, 23, 264653), process_id=8696, message="SKError: 'SKQuoteLib_GetStockByNoLONG' 報價尚未連線，請先連線", full_message="%QE INFO  2024-04-17 13:49:23.264653 | API  |  8696 |SKError: 'SKQuoteLib_GetStockByNoLONG' 報價尚未連線，請先連線", signature='QE')

@api.event.log.fatal
def onLogFatal(data):
    print(f"Fatal log: {data}")

@api.start
def main():
    Logger.show = True
    api.login(userId="A123456789", password="*************", tag="me")
    time.sleep(2)
    Logger.error("Error testing!")
    Logger.fatal("Fatal testing!")


if __name__ == '__main__':
    main()