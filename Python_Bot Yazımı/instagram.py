from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)

        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()

        time.sleep(3)
        

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/semaozmeninal/followers")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {followerCount}")

        action = webdriver.ActionChains(self.browser)
       

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount!= newCount:
                followerCount = newCount
                print(f"Second count: {newCount}")
                time.sleep(1)
            else:
                break
                
        followers = dialog.find_elements_by_css_selector("li")       
        

        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            print(link)
       


instagram = Instagram(username,password)
instagram.signIn()
instagram.getFollowers()



