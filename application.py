# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

#by Chrome
#from selenium.webdriver.chrome.webdriver import WebDriver
#driver = WebDriver(executable_path="chromedriver.exe", service_args=["--ignore-certificate-errors", "--log-path=E:\\qc1.log"])

#by Firefox
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#binary = FirefoxBinary('C:/Users/9a4459/AppData/Local/Mozilla Firefox/')
#browser = webdriver.Firefox(firefox_binary=binary)

from selenium.webdriver.common.action_chains import ActionChains

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def return_to_page(self):
        wd = self.wd
        # retun to main page
        wd.find_element_by_link_text("group page").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://testtiny/")

    def destroy(self):
        self.wd.quit()
