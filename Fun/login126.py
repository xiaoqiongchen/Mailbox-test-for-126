import time
from Conf.ReadIni import *
from Util.LocateElement import *
from selenium import webdriver
class login:
    def __init__(self,driver):
        self.driver=driver

    def login(self,username,password):
        self.driver.implicitly_wait(3)

        locate_method_iframe,locate_exp_iframe = read_ini_file_option(ini_path(),"126mail_indexPage","indexPage.frame").split(">")
        el_iframe = find_element(self.driver,locate_method_iframe,locate_exp_iframe)
        self.driver.switch_to.frame(el_iframe)

        locate_method_name,locate_exp_name=read_ini_file_option(ini_path(),"126mail_indexPage","indexPage.username").split(">")
        user_name =find_element(self.driver,locate_method_name,locate_exp_name)
        user_name.clear()
        user_name.send_keys(username)

        locate_method_pwd,locate_exp_pwd=read_ini_file_option(ini_path(),"126mail_indexPage","indexPage.password").split(">")
        pwd =find_element(self.driver,locate_method_pwd,locate_exp_pwd)
        pwd.clear()
        pwd.send_keys(password)

        locate_method_login,locate_exp_login=read_ini_file_option(ini_path(),"126mail_indexPage","indexPage.loginbutton").split(">")
        find_element(self.driver,locate_method_login,locate_exp_login).click()

        self.driver.switch_to.default_content()

        page_source = self.driver.page_source
        time.sleep(3)
        return page_source
if __name__=="__main__":
   driver=webdriver.Chrome()
   driver.get("https://126.com/")
   lo=login(driver)
   lo.login("xiaoxiao945","123456a")
