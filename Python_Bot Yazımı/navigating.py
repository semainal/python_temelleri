from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()


url = "http://github.com"
driver.get(url)


# searchInput = driver.find_element_by_name("q")
searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)


# result = driver.page_source
# print(result)
result = driver.find_elements_by_css_selector(".repo-list-item a")

for element in result:
    print(element.text)

driver.close()