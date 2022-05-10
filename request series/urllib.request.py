import urllib.request
headers = {'User-Agent':'Mozilla/5.0(Windows NT 6.1; WOW64)\AppleWebKit/537.36(KHTML, like Gecko) Chrome/45.0.2454.101\Safari/537.36'}
url = 'https://www.ncu.edu.tw/tw/'
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

