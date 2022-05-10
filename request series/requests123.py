import requests
url = 'https://www.ncu.edu.tw/tw/'
response = requests.get(url)
if response.status_code == requests.codes.ok:
    pattern = input ('請輸入欲搜尋的關鍵字')
    if pattern in response.text:
        print('搜尋 %s 成功' %pattern)
    else:
        print('搜尋 %s 失敗' %pattern)
    
    #print('取得網頁內容成功')
    #print(response.text)  #列印網頁內容
    #print('網址訊息 :', response.url)
    #print('表頭訊息 :', response.headers)
    #print('cookie訊息 :',response.cookies)
else:
    print('取得網頁內容失敗')

