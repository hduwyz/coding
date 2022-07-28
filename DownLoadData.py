import requests
import csv

stock_base_info_api = r'http://api.waizaowang.com/doc/getStockHSABaseInfo?code=all&fields=all&export=4&token=6d00f1b914f13f122924aa2807017c67'
stock_day_k_line_api = 'http://api.waizaowang.com/doc/getStockHSADayKLine?code=all&ktype=101&fq=0&startDate=2022-07-15&endDate=2022-07-15&fields=all&export=4&token=6d00f1b914f13f122924aa2807017c67'
def getDataInfo(url, file_name):
    r = requests.get(url)
    with open(file_name, 'w') as fp:
        writer = csv.writer(fp)
        for line in r.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))

getDataInfo(stock_base_info_api, 'stock_base_info.csv')

getDataInfo(stock_day_k_line_api, 'stock_day_k_line_api.csv')
