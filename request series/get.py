import requests
r = requests.get('https://www.youbike.com.tw/')
print(r.status_code)
#r.status_code http 請求返回狀態 200成功 404失敗
#r.text http 響應內容字符串形式＝url對應頁面內容
#r.encoding http header 猜測編碼方式
#r.apparent_encoding 從內容中分析出來的編碼方式
#r.content 二進制形式
print(r.encoding)
print(r.apparent_encoding)
#requests.ConnectionError 網路連接異常
#requests.HTTPError http錯誤異常
#requests.URLRequired url缺失異常
#requests.toomanyredirects 超過最大定向次數
#requests.Connecttimeout 連接遠程服務器異常
#requests.timeout 請求url超時異常
#Scrapy 中規模，數據規模較大，爬取速度敏感
#user agent 
#robots協議：網路爬蟲排除標準
