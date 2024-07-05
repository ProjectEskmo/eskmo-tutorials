from starter import *
from eskmo import api
from eskmo import Logger, Stocks, Stock

@api.start
def main():
    Logger.show = True
    api.login(userId="A123456789", password="*************", tag="me")

    stock: Stock = api.stocks["2330"]
    print(stock)

    # 3.1.1. 商品檔基本資訊
    print(stock.info)
    # ADD stock.info.ok_short <--- 用英文
    # ADD 初始 Quote 有的值, 今天不會變的值, 合併到 info

    # {'商品代號': '2330', '融資標記': '0', '融資限量': '9999', '融資比率': '60.000',
    #  '融券標記': '0', '融券限量': '313', '融券比率': '90.000', '當沖標記': '1', '被降成標記': '0',
    #  '平盤放空標記': '1', '全額交割標記': '0', '警示標記': '0', '處置股票標記': '0', '注意股票標記': '0',
    #  '受限股票標記': '0', '異常推介標記': '0', '特殊異常標記': '0', '單筆委託張數限制': '0', '多筆委託張數限制': '0',
    #  '款券預收成數': '0', 'LOGIN_ID': 'A123456789', 'ACCOUNT_NO': '91829808465'}

    # 3.1.2. 商品檔價格資訊
    print(stock.quote)
    # {'nStockIdx': 29715, 'sDecimal': 2, 'sTypeNo': 24, 'bstrMarketNo': '0', 'bstrStockNo': '2330',
    #  'bstrStockName': '台積電', 'nHigh': 0.0, 'nOpen': 0.0, 'nLow': 0.0, 'nClose': 0.0, 'nTickQty': 0, 
    #  'nRef': 790.0, 'nBid': 0.0, 'nBc': 0, 'nAsk': 0.0, 'nAc': 0, 'nTBc': 0, 'nTAc': 0, 'nFutureOI': 0,
    #  'nTQty': 0, 'nYQty': 37925, 'nUp': 869.0, 'nDown': 711.0, 'nSimulate': 0, 'nDayTrade': 1, 'nTradingDay': 20240403}

    
if __name__ == "__main__":
    main()
