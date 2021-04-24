from emailUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Mail:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        

    def signIn(self):
        self.browser.get("https://accounts.google.com/")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]").click
        time.sleep(2)

mail = Mail(username,password)
mail.signIn()




