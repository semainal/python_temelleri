from selenium import webdriver
import time 


driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")
url = "http://github.com/semainal"
driver.get(url)

print(driver.title)

if "semainal" in driver.title:
    driver.save_screenshot("github-semainal.png")

time.sleep(2)

driver.back()
# diver.forward()

time.sleep(2)
driver.close()