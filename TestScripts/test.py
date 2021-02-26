from Conf.readexcel import ExcelUtil
from Conf import ConfigPath

file_path=ConfigPath.test_data_path()
def get_send_email_data():#发送邮件测试数据
    eu = ExcelUtil(file_path, "send_email")
    return eu.dict_data()
print(get_send_email_data())