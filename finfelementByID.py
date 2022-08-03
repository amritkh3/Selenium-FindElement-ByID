"""find element by ID
1. import time  from python
2. import webdriver from selenium.
3.import chromedrivermanager.in order to import chromedrivermanager 
ask pip to installwebdriver_manager
4.install chromedrivermanager and assign it to the variale driver.
5.use get fumction to open the web page with the help of url.
ie.driver.get("url")
6.use find.element function to locate  the textbox and use send key function to enter the key
    use id and value 

"""

import time#this is python time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager#if weddriver_manager is not found run
#pip install webdrive_manager
driver=webdriver.Chrome(ChromeDriverManager().install())# your entire selenium chrome package
from selenium.webdriver.common.by import By
driver.get("http://omayo.blogspot.com")
time.sleep(3)#this will hold the time for 3 seconds

driver.refresh()#refresh the page
time.sleep(5)#hold time for 5  sec

driver.maximize_window()#maximize the window
time.sleep(5)

checkurl=driver.current_url#checking the url of the webpage
print(checkurl)
time.sleep(3)

driver.save_screenshot("omayoscreenshot.png")#capturing the screenchot of the opened page
time.sleep(3)

driver.find_element(By.ID,"ta1").send_keys("i want to write something on the textbox")
time.sleep(3)

driver.find_element(By.ID,"textbox1").send_keys("batch")
time.sleep(3)
driver.quit()#close the webpage



