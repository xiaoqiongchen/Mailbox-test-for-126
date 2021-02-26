import pytest
import time
from selenium import webdriver
from Fun.sendemail import send_email
from Fun.create_contact import create_contact
from Conf.readexcel import ExcelUtil
from Conf import ConfigPath
from Fun.login126 import login
import allure

file_path=ConfigPath.test_data_path()
print(file_path)
def login_data():#登录测试用例数据
    eu=ExcelUtil(file_path,"login")
    return eu.dict_data()

def get_contact_data():#创建联系人测试用例数据
    eu=ExcelUtil(file_path,"create_contact")
    return eu.dict_data()

def get_send_email_data():#发送邮件测试数据
    eu = ExcelUtil(file_path, "send_email")
    return eu.dict_data()

class Test_main:
      driver=""

      def setup(self):
          global driver
          driver=webdriver.Chrome()
          driver.get("https://mail.126.com/")

      def teardown(self):
          global driver
          driver.quit()

      @allure.story('登录')
      @pytest.mark.parametrize("datalist", login_data())
      def test_login(self, datalist):#登录测试方法
          global driver
          lo=login(driver)
          actual_value=lo.login(datalist["username"],datalist["password"])
          expect_value=datalist["assert_word"]
          assert expect_value in actual_value

      @allure.story('新增联系人')
      @pytest.mark.parametrize('contact_dicdata', get_contact_data())
      def test_create_contact(self, contact_dicdata):#创建联系人测试方法
          global driver
          lo=login(driver)
          lo.login("xiaoxiao945","123456a")
          cc=create_contact(driver)
          cc.add_contact(contact_dicdata["name"],contact_dicdata["email"],contact_dicdata["tel"],contact_dicdata["remark"],contact_dicdata["Fax1"],contact_dicdata["Fax2"],
                            contact_dicdata["Fax3"],contact_dicdata["address"],contact_dicdata["POPO"],contact_dicdata["bir_year"],contact_dicdata["bir_month"],contact_dicdata["bir_day"],
                            contact_dicdata["homepage"],contact_dicdata["organization"],contact_dicdata["department"],contact_dicdata["position"],contact_dicdata["role"],contact_dicdata["member"])

      @allure.story('发送邮件')
      @pytest.mark.parametrize('send_emaildata', get_send_email_data())#发送邮件测试方法
      def test_send_email(self,send_emaildata):
          print(send_emaildata)
          global driver
          lo = login(driver)
          lo.login("xiaoxiao945", "123456a")
          time.sleep(1)
          se=send_email(driver)
          se.Send_Email(send_emaildata["sender"],send_emaildata["title"],send_emaildata["filename"],send_emaildata["content"])