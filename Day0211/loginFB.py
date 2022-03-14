from selenium import webdriver

url = 'https://www.facebook.com/'
email = 'FBId'
password = 'FBpassword'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)

driver.find_element_by_name('login').click()