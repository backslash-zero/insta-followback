from selenium import webdriver
from time import sleep
from secret import pw

follower = []
unfollowers = []
unfollowers = []

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        
        # Wait for page to load
        sleep(2)
        
        #Username and password
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')] | //button[contains(text(), 'Not now')]")\
            .click()
        sleep(2)
        self.driver.get("https://instagram.com/" + username)
        sleep(4)
    
    def get_followers(self):

    def get_following(self):



InstaBot("cele_stin", pw)
InstaBot.get_followers()
InstaBot.get_following()
