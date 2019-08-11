import requests
from bs4 import BeautifulSoup
import pandas as pd
stocknamelist = []
stockpricelist = []
stockpercentagelist = []
for stock in range(100):
    try:
        stockstring = str(stock)
        if stock < 100:
            stockstring = '00'+str(stock)
        if stock < 10:
            stockstring = '000'+str(stock)
        res = requests.get('https://hk.finance.yahoo.com/quote/'+stockstring+'.HK')
        soup = BeautifulSoup(res.text,'html.parser')
        stockname = soup.find_all('h1','D(ib)')
        stock_detail = soup.find_all('span',class_="Trsdu(0.3s)")
        print(stockname[0].string+' $'+stock_detail[0].string+" "+stock_detail[1].string)
        stocknamelist.append(stockname[0].string)
        stockpricelist.append(stock_detail[0].string)
        stockpercentagelist.append(stock_detail[1].string)
    except:
        print("股票編號錯誤")
df1 = pd.DataFrame({'Name':stocknamelist,'Price':stockpricelist,'Percentage':stockpercentagelist})
print(df1)
df1.to_excel('stock_output.xlsx',startcol=0,index=False,encoding='utf8')
