from selenium import webdriver
from time import sleep
from secret import pw

shortWait = 1
longWait = 4

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        self.username = username
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
        sleep(4)

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

    def get_followers(self):
        self.driver.get("https://instagram.com/" + self.username)
        sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        sleep(4)
        return(self._get_names())
    
    def get_following(self):
        self.driver.get("https://instagram.com/" + self.username)
        sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        return(self._get_names())

    def check_follow_back(self):
        followers = self.get_followers()
        following = self.get_following()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

myBot = InstaBot("cele_stin", pw)
myBot.check_follow_back()
