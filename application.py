# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

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

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_page(self):
        wd = self.wd
        # retun to main page
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_page()

    def open_group_page(self):
        wd = self.wd
        # open group page
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://testtiny/")

    def destroy(self):
        self.wd.quit()
