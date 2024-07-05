from eskmo import api

@api.start
def main():
    print(f"Hello: {api.logger}")
    result = api.api_testing()
    print(result)
    # {'檢測項目': [('啟動多進程', '成功'),
    #              ('依賴套件初始化', '成功'),
    #              ('Eskmo 初始化', '成功'),
    #              ('Comtypes 初始化', '成功'),
    #              ('SKCOM 初始化', '成功')], 
    #  'Messages': ['SKCOM API 已就位，可以開始使用']}
    print("Finished")

if __name__ == "__main__":
    main()
