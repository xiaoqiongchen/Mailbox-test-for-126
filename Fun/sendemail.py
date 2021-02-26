import time
from Conf.ReadIni import *
from Util.LocateElement import *
from selenium import webdriver
from Fun.login126 import *
class send_email:
    def __init__(self,driver):
        self.driver=driver
    def Send_Email(self,sender,title,filename,contents):
        self.driver.implicitly_wait(4)

        locate_method_header, locate_exp_header = read_ini_file_option(ini_path(),"126mail_sendEamilPage","sendEamilPage.header").split(">")
        header = find_element(self.driver, locate_method_header, locate_exp_header)
        header.click()

        locate_method_b, locate_exp_b = read_ini_file_option(ini_path(), "126mail_sendEamilPage","sendEamilPage.b").split(">")
        header = find_element(self.driver, locate_method_b, locate_exp_b)
        header.click()

        locate_method_sender, locate_exp_sender = read_ini_file_option(ini_path(), "126mail_sendEamilPage","sendEamilPage.sender").split(">")
        user_sender = find_element(self.driver, locate_method_sender, locate_exp_sender)
        user_sender.send_keys(sender)

        locate_method_title, locate_exp_title = read_ini_file_option(ini_path(), "126mail_sendEamilPage","sendEamilPage.title").split(">")
        user_title = find_element(self.driver, locate_method_title, locate_exp_title)
        user_title.send_keys(title)

        locate_method_filename, locate_exp_filename = read_ini_file_option(ini_path(), "126mail_sendEamilPage","sendEamilPage.filename").split(">")
        user_filename = find_element(self.driver, locate_method_filename, locate_exp_filename)
        user_filename.send_keys(filename)

        locate_method_iframe, locate_exp_iframe = read_ini_file_option(ini_path(), "126mail_sendEamilPage","sendEamilPage.iframe").split(">")
        user_filename = find_element(self.driver, locate_method_iframe, locate_exp_iframe)
        self.driver.switch_to.frame(user_filename)

        locate_method_content, locate_exp_content = read_ini_file_option(ini_path(), "126mail_sendEamilPage","sendEamilPage.content").split(">")
        content = find_element(self.driver, locate_method_content, locate_exp_content)
        content.send_keys(contents)

        self.driver.switch_to.default_content()
        time.sleep(4)

        locate_method_footer, locate_exp_footer = read_ini_file_option(ini_path(), "126mail_sendEamilPage","sendEmailPage.footer").split(">")
        print(locate_method_footer)
        print(locate_exp_footer)
        footer = find_element(self.driver, locate_method_footer, locate_exp_footer)
        print("footer的值为：",footer)
        footer.click()

if __name__ == "__main__":
            driver = webdriver.Chrome()
            driver.get("https://126.com/")
            lo = login(driver)
            lo.login("xiaoxiao945", "123456a")
            cc = send_email(driver)
            cc.Send_Email("172787078@qq.com","人生苦短，我用python",r"E:\pic\1.jpg","xiaoxiao945用夕阳余晖为你温床，用傍晚的安详静你心房")
























        # self.driver.find_element_by_xpath('//b[@class="nui-ico fn-bg ga0"]').click()#点击写信按钮
        # send=self.driver.find_element_by_xpath('//div[@class="kZ0 eB0"]/div/div/div[2]/div/input')#获取收件人输入元素
        # send.clear()
        # send.send_keys(sender)
        # theme=self.driver.find_element_by_xpath('//div[@class="kZ0 fu0"]/div/div/div/input')#获取主体输入元素
        # theme.clear()
        # theme.send_keys(title)
        # enclosure=self.driver.find_element_by_xpath('//div[@class="ia0"]/div/div[2]/input')#获取附件输入元素
        # enclosure.send_keys(filename)
        # el_iframe=self.driver.find_element_by_xpath('//iframe[@class="APP-editor-iframe"]')#获取iframe元素
        # self.driver.switch_to.frame(el_iframe)#切换至iframe
        # content=self.driver.find_element_by_xpath('//body[@class="nui-scroll"]')
        # content.clear()
        # content.send_keys(contents)
        # self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath('//footer[@class="jp0"]/div/span[2]').click()
        # time.sleep(2)





