import time
from Conf.ReadIni import *
from Util.LocateElement import *
from selenium import webdriver
from Fun.login126 import *
class create_contact:

    def __init__(self,driver):
        self.driver=driver

    def add_contact(self,name,email,telphone,remark,fax1,fax2,fax3,address,popo,bir_year,bir_month,bir_day,homepage,organization,department,position,role,member):
        self.driver.implicitly_wait(4)

        locate_method_addressLink,locate_exp_addressLink = read_ini_file_option(ini_path(),"126mail_contactPersonPage","contactPersonPage.addressLink").split(">")
        addressLink = find_element(self.driver,locate_method_addressLink,locate_exp_addressLink)
        addressLink.click() #点击通讯录

        time.sleep(2)

        locate_method_contact_button,locate_exp_contact_button=read_ini_file_option(ini_path(),"126mail_contactPersonPage","contactPersonPage.clickcontactButton").split(">")
        contact_button=find_element(self.driver,locate_method_contact_button,locate_exp_contact_button)
        contact_button.click() #点击新建联系人按钮

        locate_method_name,locate_exp_name=read_ini_file_option(ini_path(),"126mail_contactPersonPage","contactPersonPage.name").split(">")
        user_name=find_element(self.driver,locate_method_name,locate_exp_name)
        user_name.clear()
        user_name.send_keys(name) #输入姓名

        locate_method_email, locate_exp_email = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.email").split(">")
        user_email = find_element(self.driver, locate_method_email, locate_exp_email)
        user_email.clear()
        user_email.send_keys(email)  #电子邮箱

        locate_method_setstar,locate_exp_setstar=read_ini_file_option(ini_path(),"126mail_contactPersonPage","contactPersonPage.setstar").split(">")
        setstar=find_element(self.driver,locate_method_setstar,locate_exp_setstar)
        setstar.click() #设置星标联系人

        locate_method_phone, locate_exp_phone = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.phone").split(">")
        phone = find_element(self.driver, locate_method_phone, locate_exp_phone)
        phone.clear()
        phone.send_keys(telphone) #输入手机号码

        locate_method_otherinfo, locate_exp_otherinfo = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.otherinfo").split(">")
        otherinfo = find_element(self.driver, locate_method_otherinfo, locate_exp_otherinfo)
        otherinfo.clear()
        otherinfo.send_keys(remark) #输入备注

        locate_method_select, locate_exp_select = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.select").split(">")
        select = find_element(self.driver, locate_method_select, locate_exp_select)
        select.click() #点击请选择

        time.sleep(2)

        locate_method_selectrelatives, locate_exp_selectrelatives = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.selectrelatives").split(">")
        selectrelatives = find_element(self.driver, locate_method_selectrelatives, locate_exp_selectrelatives)
        selectrelatives.click() # 选择亲人分组

        locate_method_clicksave, locate_exp_clicksave = read_ini_file_option(ini_path(),"126mail_contactPersonPage","contactPersonPage.clicksave").split(">")
        clicksave = find_element(self.driver, locate_method_clicksave, locate_exp_clicksave)
        clicksave.click()  # 点击保存按钮

        time.sleep(2)

        locate_method_clickmore, locate_exp_clickmore = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.clickmore").split(">")
        clickmore = find_element(self.driver, locate_method_clickmore, locate_exp_clickmore)
        clickmore.click()  # 点击更多选项

        time.sleep(2)

        locate_method_fax1, locate_exp_fax1 = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.fax1").split(">")
        cz1 = find_element(self.driver, locate_method_fax1, locate_exp_fax1)
        cz1.clear()
        cz1.send_keys(fax1)  #输入传真1

        locate_method_fax2, locate_exp_fax2 = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.fax2").split(">")
        cz2 = find_element(self.driver, locate_method_fax2, locate_exp_fax2)
        cz2.clear()
        cz2.send_keys(fax2)  #输入传真2

        locate_method_fax3, locate_exp_fax3 = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.fax3").split(">")
        cz3 = find_element(self.driver, locate_method_fax3, locate_exp_fax3)
        cz3.clear()
        cz3.send_keys(fax3)  #输入传真3

        locate_method_address, locate_exp_address = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.address").split(">")
        useraddress = find_element(self.driver, locate_method_address, locate_exp_address)
        useraddress.clear()
        useraddress.send_keys(address)  # 输入居住地址

        locate_method_clickpopo, locate_exp_clickpopo = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.clickpopo").split(">")
        clickpopo = find_element(self.driver, locate_method_clickpopo, locate_exp_clickpopo)
        clickpopo.click() #点击popo下拉框选择qq

        locate_method_qq, locate_exp_qq = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.qq").split(">")
        qq = find_element(self.driver, locate_method_qq, locate_exp_qq)
        qq.clear()
        qq.send_keys(popo)  # 输入qq值

        locate_method_birth_year, locate_exp_birth_year = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.birth_year").split(">")
        birthyear = find_element(self.driver, locate_method_birth_year, locate_exp_birth_year)
        birthyear.clear()
        birthyear.send_keys(bir_year)  # 输入生日年

        locate_method_birth_month, locate_exp_birth_month = read_ini_file_option(ini_path(), "126mail_contactPersonPage", "contactPersonPage.birth_month").split(">")
        birthmonth = find_element(self.driver, locate_method_birth_month, locate_exp_birth_month)
        birthmonth.clear()
        birthmonth.send_keys(bir_month)  # 输入生日月

        locate_method_birth_day, locate_exp_birth_day = read_ini_file_option(ini_path(),"126mail_contactPersonPage","contactPersonPage.birth_day").split(">")
        birthday = find_element(self.driver, locate_method_birth_day, locate_exp_birth_day)
        birthday.clear()
        birthday.send_keys(bir_day)  # 输入生日天

        locate_method_homepage, locate_exp_homepage = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.homepage").split(">")
        user_hompage = find_element(self.driver, locate_method_homepage, locate_exp_homepage)
        user_hompage.clear()
        user_hompage.send_keys(homepage)  # 输入生日主页

        locate_method_organization, locate_exp_organization = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.organization").split(">")
        user_organization = find_element(self.driver, locate_method_organization, locate_exp_organization)
        user_organization.clear()
        user_organization.send_keys(organization)  # 输入组织

        locate_method_department, locate_exp_department = read_ini_file_option(ini_path(),"126mail_contactPersonPage","contactPersonPage.department").split(">")
        user_department = find_element(self.driver, locate_method_department, locate_exp_department)
        user_department.clear()
        user_department.send_keys(department)  # 输入部门

        locate_method_position, locate_exp_position = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.position").split(">")
        user_position = find_element(self.driver, locate_method_position, locate_exp_position)
        user_position.clear()
        user_position.send_keys(position)  # 输入职位

        locate_method_role, locate_exp_role = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.role").split(">")
        user_role = find_element(self.driver, locate_method_role, locate_exp_role)
        user_role.clear()
        user_role.send_keys(role)  # 输入角色

        locate_method_member, locate_exp_member = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.member").split(">")
        user_member = find_element(self.driver, locate_method_member, locate_exp_member)
        user_member.clear()
        user_member.send_keys(member)  # 输入成员

        locate_method_confirmButton, locate_exp_confirmButton = read_ini_file_option(ini_path(), "126mail_contactPersonPage","contactPersonPage.confirmButton").split(">")
        confirmButton = find_element(self.driver, locate_method_confirmButton, locate_exp_confirmButton)
        confirmButton.click()#点击保存按钮

        time.sleep(2)

if __name__=="__main__":
   driver=webdriver.Chrome()
   driver.get("https://126.com/")
   lo=login(driver)
   lo.login("xiaoxiao945","123456a")
   cc=create_contact(driver)
   cc.add_contact("xiaoxiao","172787078@qq.com","telphone","remark","fax1","fax2","fax3","address","popo","2021","05","07","homepage","organization","department","position","role","member")




















