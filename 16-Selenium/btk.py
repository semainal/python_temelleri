from btkUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class Btk:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.btkakademi.gov.tr/")
        time.sleep(10)
        self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/a").click()
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='tridField']").send_keys(self.username)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='egpField']").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div[2]/input[4]").click()
        time.sleep(1)

    def learningpage(self):
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div/ul/li[1]/a").click()




btk = Btk(username,password)
btk.signIn()
btk.learningpage()