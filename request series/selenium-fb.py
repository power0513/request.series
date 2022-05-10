from selenium import webdriver 
#設定facebook 登入資訊
url = 'https://zh-tw.facebook.com/'
email = 'tsai0267@gmail.com'
password = 'Az12345678!'
driver = webdriver.Chrome('request series/chromedriver')
driver. maximize_window()
driver.get(url)

driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_name('login').click()

