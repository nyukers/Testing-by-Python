# -*- coding: utf-8 -*-
from selenium import WebDriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper

#by Chrome
#from selenium.webdriver.chrome.webdriver import WebDriver
#driver = WebDriver(executable_path="chromedriver.exe", service_args=["--ignore-certificate-errors", "--log-path=E:\\qc1.log"])

#by Firefox
#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#binary = FirefoxBinary('C:/Users/username/AppData/Local/Mozilla Firefox/')
#browser = webdriver.Firefox(firefox_binary=binary)

#from selenium.webdriver.common.action_chains import ActionChains

class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = WebDriver.Firefox()
        elif browser == "chrome":
            self.wd = WebDriver.Chrome()
        elif browser == "opera":
            self.wd = WebDriver.Opera()
        elif browser == "ie":
            self.wd = WebDriver.Ie()
        else:
            raise ValueError("Unknown web-browser" % browser)

        #it's delay for real Web
        #self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.base_url = base_url

# check running browser
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def return_to_page(self):
        wd = self.wd
        # retun to main page
        wd.find_element_by_link_text("group page").click()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
