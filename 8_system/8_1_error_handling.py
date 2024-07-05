from starter import *
from eskmo import api

@api.event.log.debug
def onLogDebug(data):
    print(f"Debug log: {data}")

@api.event.log.info
def onLogInfo(data):
    print(f"Info log: {data}")

@api.event.log.warning
def onLogWarning(data):
    print(f"Warning log: {data}")

@api.start
def main():
    api.login(userId="A123456789", password="*************", tag="me")

if __name__ == "__main__":
    main()    