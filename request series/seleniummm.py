from selenium import webdriver
import time
import urllib
import os
# 存圖位置
local_path = 'imgs'
# 爬取頁面網址 
url = 'https://mega.nz/folder/D74CXI6J#NrJn-P_was9jkqmvRdI1Zg/folder/e2In3Kya'
# 目標元素的xpath
xpath = '//div[@id="imgid"]/ul/li/a/img'
# 啟動chrome瀏覽器
chromeDriver = r'/Users/chuang/Downloads/chormedriver' # chromedriver檔案放的位置
driver = webdriver.Chrome(chromeDriver) 
  
# 最大化窗口，因為每一次爬取只能看到視窗内的圖片  
driver.maximize_window()  
  
# 紀錄下載過的圖片網址，避免重複下載  
img_url_dic = {}  
  
# 瀏覽器打開爬取頁面
driver.get(url)  
  
# 模擬滾動視窗瀏覽更多圖片
pos = 0  
m = 0 # 圖片編號 
for i in range(100):  
    pos += i*500 # 每次下滾500  
    js = "document.documentElement.scrollTop=%d" % pos  
    driver.execute_script(js)  
    time.sleep(1)
    
    for element in driver.find_elements_by_xpath(xpath):
        try:
            img_url = element.get_attribute('src')
            
            # 保存圖片到指定路徑
            if img_url != None and not img_url in img_url_dic:
                img_url_dic[img_url] = ''  
                m += 1
                # print(img_url)
                ext = img_url.split('/')[-1]
                # print(ext)
                filename = str(m) + 'kerGee' + '_' + ext +'.jpg'
                print(filename)
                
                # 保存圖片
                urllib.request.urlretrieve(img_url, os.path.join(local_path , filename))
                
        except OSError:
            print('發生OSError!')
            print(pos)
            break;
            
driver.close()